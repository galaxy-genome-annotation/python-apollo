import glob
import json
import tarfile
import tempfile
import time

from . import ApolloTestCase, wa


class RemoteTest(ApolloTestCase):

    def test_delete_organism(self):

        time.sleep(3)

        org_info = wa.organisms.show_organism('temp_org')

        wa.remote.delete_organism(org_info['id'])

        time.sleep(3)

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_delete_organism_cn(self):

        time.sleep(3)

        wa.remote.delete_organism('temp_org')

        time.sleep(3)

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_update_organism(self):

        time.sleep(3)

        org_info = wa.organisms.show_organism('temp_org')

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 1
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

    def test_add_organism(self):

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))
            res = wa.remote.add_organism('some_new_org_remote', archive, species='newspecies', genus='newgenus', metadata=meta)

        res = res[0]
        assert res['species'] == 'newspecies'
        assert res['genus'] == 'newgenus'
        assert not res['publicMode']
        meta_back = json.loads(res['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        time.sleep(3)

        org_info = wa.organisms.show_organism('some_new_org_remote')

        wa.remote.delete_organism(org_info['id'])

        assert org_info['species'] == 'newspecies'
        assert org_info['genus'] == 'newgenus'
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

    def setUp(self):
        org_info = wa.organisms.show_organism('alt_org')
        if 'directory' not in org_info:
            # Should not happen, but let's be tolerant...
            # Error received when it fails: {'error': 'No row with the given identifier exists: [org.bbop.apollo.Organism#1154]'}
            time.sleep(1)
            org_info = wa.organisms.show_organism('alt_org')

        wa.organisms.add_organism('temp_org', org_info['directory'])

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])

        org_info = wa.organisms.show_organism('some_new_org_remote')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])
