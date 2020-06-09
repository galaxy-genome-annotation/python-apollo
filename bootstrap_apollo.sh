#!/bin/bash

SHOULD_LAUNCH_DOCKER=1
ARROW_GLOBAL_CONFIG_PATH=`pwd`/test-data/arrow.yml
APOLLO_DATA_DIRECTORY="/data"
GALAXY_SHARED_DIR=`pwd`/apollo_shared_dir
for arg in "$@"
do
    case $arg in
        --nodocker)
        SHOULD_LAUNCH_DOCKER=0
        ARROW_GLOBAL_CONFIG_PATH=`pwd`/test-data/local-arrow.yml
        APOLLO_DATA_DIRECTORY=$GALAXY_SHARED_DIR
        mkdir -p $APOLLO_DATA_DIRECTORY
        shift
        ;;
        *)
        shift
        ;;
    esac
done

export ARROW_GLOBAL_CONFIG_PATH GALAXY_SHARED_DIR
mkdir -p "$GALAXY_SHARED_DIR"

if ! [[ $SHOULD_LAUNCH_DOCKER -eq 0 ]]; then
    docker run --memory=4g -d -p 8888:8080 -v `pwd`/apollo_shared_dir/:/data/ -e "WEBAPOLLO_DEBUG=true" quay.io/gmod/apollo:fix-default-apollo-test
fi

echo "[BOOTSTRAP] Waiting while Apollo starts up..."
# Wait for apollo to be online
for ((i=0;i<30;i++))
do
  echo "Checking Apollo ..."
  APOLLO_UP=$(arrow users get_users 2> /dev/null | head -1 | grep '^\[$' -q; echo "$?")
	if [[ $APOLLO_UP -eq 0 ]]; then
		break
	fi
  echo "Not up yet, trying again in 10 seconds"
  sleep 10
done

if ! [[ $APOLLO_UP -eq 0 ]]; then
    echo "Cannot connect to apollo for bootstrapping"
    arrow users get_users
    exit "${APOLLO_UP}"
fi

echo "[BOOTSTRAP] Apollo is up, bootstrapping for tests"

# Create some groups
arrow groups create_group one_group
arrow groups create_group another_group

# Create a user
arrow users create_user "test@bx.psu.edu" Junior Galaxy password

# Add some organisms
cp -r test-data/dataset_1_files/data/ "${GALAXY_SHARED_DIR}/org1"
cp -r test-data/dataset_1_files/data/ "${GALAXY_SHARED_DIR}/org2"
cp -r test-data/dataset_1_files/data/ "${GALAXY_SHARED_DIR}/org3"
cp -r test-data/dataset_1_files/data/ "${GALAXY_SHARED_DIR}/org4"
cp -r test-data/dataset_2_files/data/ "${GALAXY_SHARED_DIR}/org_update_newseq"
cp -r test-data/dataset_3_files/data/ "${GALAXY_SHARED_DIR}/org_update_changedseq"
arrow organisms add_organism --genus Testus --species organus test_organism $APOLLO_DATA_DIRECTORY/org1
arrow organisms add_organism --genus Foo --species barus alt_org $APOLLO_DATA_DIRECTORY/org2
arrow organisms add_organism --genus Foo3 --species barus org3 $APOLLO_DATA_DIRECTORY/org3
arrow organisms add_organism --genus Foo4 --species barus org4 $APOLLO_DATA_DIRECTORY/org4

# Give access to organisms for test user
arrow users update_organism_permissions --write --read --export "test@bx.psu.edu" test_organism
arrow users update_organism_permissions --write --read --export "test@bx.psu.edu" alt_org
arrow users update_organism_permissions --write --read --export "test@bx.psu.edu" org3
arrow users update_organism_permissions --write --read --export "test@bx.psu.edu" org4

# Load some annotations
arrow annotations load_gff3 test_organism test-data/merlin.gff
arrow annotations load_gff3 alt_org test-data/merlin.gff
arrow annotations load_gff3 org3 test-data/merlin.gff
arrow annotations load_gff3 org4 test-data/merlin.gff
#arrow annotations load_legacy_gff3 org4 test-data/merlin.gff
