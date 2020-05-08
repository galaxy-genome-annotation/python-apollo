import json
import time

from . import ApolloTestCase, wa


class OrganismTest(ApolloTestCase):

    def test_get_organisms(self):

        orgs = wa.organisms.get_organisms()

        assert len(orgs) >= 3

        first_org = orgs[0]

        assert 'nonDefaultTranslationTable' in first_org
        assert 'annotationCount' in first_org
        assert 'commonName' in first_org
        assert 'obsolete' in first_org
        assert 'id' in first_org
        assert 'publicMode' in first_org
        assert 'valid' in first_org
        assert 'currentOrganism' in first_org
        assert 'sequences' in first_org
        assert 'directory' in first_org
        assert 'blatdb' in first_org
        assert 'genus' in first_org
        assert 'species' in first_org
        assert 'metadata' in first_org

        assert '/data/org' in first_org['directory']
        assert first_org['commonName'] in ['test_organism', 'alt_org', 'org3', 'org4']

    def test_get_organism_creator(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        creator = wa.organisms.get_organism_creator(str(org_id))

        assert 'creator' in creator

    def test_show_organism(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        org_info = wa.organisms.show_organism(org_id)

        assert org_info == orgs[0]

    def test_show_organism_cn(self):

        orgs = wa.organisms.get_organisms()

        org_cn = orgs[0]['commonName']

        org_info = wa.organisms.show_organism(org_cn)

        assert org_info == orgs[0]

    def test_get_sequences(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        seqs = wa.organisms.get_sequences(org_id)

        assert 'sequences' in seqs
        assert seqs['sequences'][0]['name'] == 'Merlin'
        assert seqs['sequences'][0]['length'] == 172788
        assert seqs['sequences'][0]['start'] == 0
        assert seqs['sequences'][0]['end'] == 172788

    def test_update_metadata(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        res = wa.organisms.update_metadata(org_id, {'some': 'metadata'})

        assert res == {}

        time.sleep(3)

        org_info = wa.organisms.show_organism(org_id)

        assert json.loads(org_info['metadata']) == {'some': 'metadata'}

    def test_delete_organism(self):

        org_info = self.waitOrgCreated('temp_org')

        wa.organisms.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_delete_organism_cn(self):

        wa.organisms.delete_organism('temp_org')

        self.waitOrgDeleted('temp_org')

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'temp_org'

    def test_delete_features(self):

        wa.annotations.load_gff3('temp_org', 'test-data/merlin.gff')

        org_info = wa.organisms.show_organism('temp_org')

        feats_before = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_before
        assert len(feats_before['features']) > 0

        wa.organisms.delete_features(org_info['id'])

        feats_after = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_after
        assert len(feats_after['features']) == 0

    def test_delete_features_cn(self):

        wa.annotations.load_gff3('temp_org', 'test-data/merlin.gff')

        org_info = wa.organisms.show_organism('temp_org')

        feats_before = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_before
        assert len(feats_before['features']) > 0

        wa.organisms.delete_features('temp_org')

        feats_after = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_after
        assert len(feats_after['features']) == 0

    def test_update_organism(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        wa.organisms.update_organism(org_info['id'], 'temp_org', other_org_info['directory'], species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 1

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_noreload(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        wa.organisms.update_organism(org_info['id'], 'temp_org', other_org_info['directory'], species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False, no_reload_sequences=True)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 1

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_newseq(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        new_dir = org_info['directory'].replace('org2', 'org_update_newseq')
        wa.organisms.update_organism(org_info['id'], 'temp_org', new_dir, species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 2

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 2

        seq = seqs[0]
        assert seq['name'] == 'Anotherseq'
        assert seq['length'] == 4730

        seq = seqs[1]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_changedseq(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        new_dir = org_info['directory'].replace('org2', 'org_update_changedseq')
        wa.organisms.update_organism(org_info['id'], 'temp_org', new_dir, species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 2

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 2

        seq = seqs[0]
        assert seq['name'] == 'Anotherseq'
        assert seq['length'] == 4730

        seq = seqs[1]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172188

    def test_update_organism_newseq_noreload(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        new_dir = org_info['directory'].replace('org2', 'org_update_newseq')
        wa.organisms.update_organism(org_info['id'], 'temp_org', new_dir, species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False, no_reload_sequences=True)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 1

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_update_organism_changedseq_noreload(self):

        other_org_info = wa.organisms.show_organism('test_organism')

        org_info = wa.organisms.show_organism('temp_org')

        new_dir = org_info['directory'].replace('org2', 'org_update_changedseq')
        wa.organisms.update_organism(org_info['id'], 'temp_org', new_dir, species='updatedspecies', genus='updatedgenus', blatdb=other_org_info['directory'] + "/seq/genome.2bit", public=False, no_reload_sequences=True)
        # Returns useless stuff

        time.sleep(3)
        org_info = wa.organisms.show_organism('temp_org')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == other_org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        assert org_info['sequences'] == 1

        seqs = wa.organisms.get_sequences(org_info['id'])['sequences']
        assert len(seqs) == 1

        seq = seqs[0]
        assert seq['name'] == 'Merlin'
        assert seq['length'] == 172788

    def test_add_organism(self):

        org_info = wa.organisms.show_organism('test_organism')

        meta = {"bla": "bli"}
        res = wa.organisms.add_organism('some_new_org', org_info['directory'], species='newspecies', genus='newgenus', blatdb=org_info['directory'] + "/seq/genome.2bit", metadata=meta)

        assert res['species'] == 'newspecies'
        assert res['genus'] == 'newgenus'
        assert res['blatdb'] == org_info['directory'] + "/seq/genome.2bit"
        meta_back = json.loads(res['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

        org_info = self.waitOrgCreated('some_new_org')

        wa.organisms.delete_organism(org_info['id'])

        assert org_info['species'] == 'newspecies'
        assert org_info['genus'] == 'newgenus'
        assert org_info['blatdb'] == org_info['directory'] + "/seq/genome.2bit"
        assert not org_info['publicMode']
        meta_back = json.loads(org_info['metadata'])
        assert 'bla' in meta_back and meta_back['bla'] == 'bli'

    def setUp(self):
        # Make sure the organism is not already there
        temp_org_info = wa.organisms.show_organism('temp_org')
        if 'directory' in temp_org_info:
            wa.organisms.delete_organism(temp_org_info['id'])
            self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('alt_org')
        if 'directory' not in org_info:
            # Should not happen, but let's be tolerant...
            # Error received when it fails: {'error': 'No row with the given identifier exists: [org.bbop.apollo.Organism#1154]'}
            time.sleep(1)
            org_info = wa.organisms.show_organism('alt_org')

        wa.organisms.add_organism('temp_org', org_info['directory'])
        self.waitOrgCreated('temp_org')

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('some_new_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_organism(org_info['id'])
            self.waitOrgDeleted('some_new_org')
