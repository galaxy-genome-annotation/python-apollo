import time

from . import ApolloTestCase, wa


class YeastLoadTest(ApolloTestCase):

    def test_bulkmrna_yeast(self):
        path = 'test-data/yeastI/raw/bulk_load_yeastI.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)

        print("output feature data" + str(feature_data))
        #
        # assert 'Merlin_1_mRNA' in feature_data
        #
        # feature_data = feature_data['Merlin_1_mRNA']
        #
        # assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        # assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        # assert feature_data['parent_name'] == 'Merlin_1_mRNA'
        # assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        # assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

    def test_other_yeast_types_bulk(self):
        path = 'test-data/yeastI/raw/other_types_yeastI.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)
        print("output feature data" + str(feature_data))

        # assert 'Merlin_123_mRNA' in feature_data
        #
        # feature_data = feature_data['Merlin_123_mRNA']
        #
        # # del feature_data['location']['id']
        # assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        # assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        # assert feature_data['parent_name'] == 'Merlin_123_mRNA'
        # assert len(feature_data['children']) == 2
        #
        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))
        assert '##gff-version 3' in gff_content
        # assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

    def test_multiexon_yeastI(self):
        path = 'test-data/yeastI/raw/multiexon_yeastI.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path, batch_size=10)
        print("output feature data" + str(feature_data))

        # assert 'Merlin_123_mRNA' in feature_data
        # feature_data = feature_data['Merlin_123_mRNA']

        # del feature_data['location']['id']
        # assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        # assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        # assert feature_data['parent_name'] == 'Merlin_123_mRNA'
        # assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")
        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        # assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        # assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

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
        org_info = wa.organisms.show_organism('temp_org')
        assert org_info['commonName'] == 'temp_org'

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_features(org_info['id'])
            wa.organisms.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')
