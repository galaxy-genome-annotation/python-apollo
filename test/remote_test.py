import json
import glob
import tarfile
import tempfile
import time

from . import ApolloTestCase, wa


class RemoteTest(ApolloTestCase):

    def test_delete_organism(self):

        time.sleep(3)

        # FIXME add a test with commonName too (broken in 2.4.1, should be fixed in 2.4.2)
        wa.remote.delete_organism('temp_org')

        time.sleep(3)

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    # FIXME only available starting with Apollo 2.4.2
    """def test_update_organism(self):

        org_info = wa.organisms.show_organism('temp_org')

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', metadata=meta)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'"""

    def test_add_organism(self):

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))
            res = wa.remote.add_organism('some_new_org', archive, species='newspecies', genus='newgenus', metadata=meta)

        res = res[0]
        assert res['species'] == 'newspecies'
        assert res['genus'] == 'newgenus'
        meta_back = json.loads(res['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        time.sleep(3)

        org_info = wa.organisms.show_organism('some_new_org')

        wa.remote.delete_organism(res['id'])

        assert org_info['species'] == 'newspecies'
        assert org_info['genus'] == 'newgenus'
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

    def setUp(self):
        org_info = wa.organisms.show_organism('alt_org')
        wa.organisms.add_organism('temp_org', org_info['directory'])

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])
