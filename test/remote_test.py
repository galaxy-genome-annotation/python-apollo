import glob
import json
import tarfile
import tempfile
import time

from . import ApolloTestCase, wa


class RemoteTest(ApolloTestCase):

    def test_delete_organism(self):

        org_info = self.waitOrgCreated('temp_org')

        wa.remote.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_delete_organism_cn(self):

        wa.remote.delete_organism('temp_org')

        self.waitOrgDeleted('temp_org')

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_update_organism(self):

        org_info = self.waitOrgCreated('temp_org')
        assert org_info['sequences'] == 1

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

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_noreload(self):

        org_info = self.waitOrgCreated('temp_org')
        assert org_info['sequences'] == 1

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta, no_reload_sequences=True)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 1
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_newseq(self):

        org_info = wa.organisms.show_organism('temp_org')
        assert org_info['sequences'] == 1

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_2_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_2_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 2
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 2

        seq = seqs[0]
        assert seq['name'] == 'Anotherseq'
        assert seq['length'] == 4730

        seq = seqs[1]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_changedseq(self):

        org_info = wa.organisms.show_organism('temp_org')
        assert org_info['sequences'] == 1

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_3_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_3_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 2
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 2

        seq = seqs[0]
        assert seq['name'] == 'Anotherseq'
        assert seq['length'] == 4730

        seq = seqs[1]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172188

    def test_update_organism_newseq_noreload(self):

        org_info = wa.organisms.show_organism('temp_org')
        assert org_info['sequences'] == 1

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_2_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_2_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta, no_reload_sequences=True)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 1
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_changedseq_noreload(self):

        org_info = wa.organisms.show_organism('temp_org')
        assert org_info['sequences'] == 1

        meta = {"bla": "bli"}

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_3_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_3_files/data/', './'))

            wa.remote.update_organism(org_info['id'], archive, species='updatedspecies', genus='updatedgenus', public=False, metadata=meta, no_reload_sequences=True)

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['sequences'] == 1
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

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

        org_info = self.waitOrgCreated('some_new_org_remote')

        wa.remote.delete_organism(org_info['id'])
        self.waitOrgDeleted('some_new_org_remote')

        assert org_info['species'] == 'newspecies'
        assert org_info['genus'] == 'newgenus'
        assert org_info['sequences'] == 1
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

    def setUp(self):
        # Make sure the organism is not already there
        temp_org_info = wa.organisms.show_organism('temp_org')
        if 'directory' in temp_org_info:
            wa.organisms.delete_organism(temp_org_info['id'])
            self.waitOrgDeleted('temp_org')

        with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
            with tarfile.open(archive.name, mode="w:gz") as tar:
                for file in glob.glob('test-data/dataset_1_files/data/'):
                    tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))
            wa.remote.add_organism('temp_org', archive)
        self.waitOrgCreated('temp_org')

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('some_new_org_remote')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])
            self.waitOrgDeleted('some_new_org_remote')
