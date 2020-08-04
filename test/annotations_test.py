import time

from . import ApolloTestCase, wa
from apollo import util


class AnnotationsTest(ApolloTestCase):

    def test_inclusion(self):
        assert ("gene" in util.gene_types)

    def test_mrna_top(self):
        path = 'test-data/mrna-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        print("output feature data"+str(feature_data))

        assert 'Merlin_1_mRNA' in feature_data

        feature_data = feature_data['Merlin_1_mRNA']

        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        assert feature_data['parent_name'] == 'Merlin_1_mRNA'
        assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

    def test_gene_top(self):
        path = 'test-data/gene-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_123_mRNA' in feature_data

        feature_data = feature_data['Merlin_123_mRNA']

        # del feature_data['location']['id']
        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        assert feature_data['parent_name'] == 'Merlin_123_mRNA'
        assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

    def test_batch_size(self):
        path = 'test-data/gene-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path, batch_size=10)

        assert 'Merlin_123_mRNA' in feature_data

        feature_data = feature_data['Merlin_123_mRNA']

        # del feature_data['location']['id']
        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        assert feature_data['parent_name'] == 'Merlin_123_mRNA'
        assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

    def test_isoforms(self):
        path = 'test-data/mrna-isoforms.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_58_mRNA' in feature_data

        feature_data = feature_data['Merlin_58_mRNA']

        # del feature_data['location']['id']
        assert feature_data['location'] == {'strand': -1, 'fmin': 13065, 'fmax': 14796}
        assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        assert feature_data['parent_name'] == 'Merlin_58_mRNA'
        assert len(feature_data['children']) == 4

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t13066\t14796\t.\t-\t.' in gff_content
        assert 'Merlin\t.\tmRNA\t13066\t14796\t.\t-\t.' in gff_content
        assert 'Merlin\t.\texon\t13066\t14296\t.\t-\t.' in gff_content
        assert 'Merlin\t.\tCDS\t13096\t13230\t.\t-\t0' in gff_content
        assert 'Merlin\t.\texon\t14466\t14796\t.\t-\t.' in gff_content

    def test_create_pseudogene(self):
        path = 'test-data/pseudogene-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_564' in feature_data

        feature_data = feature_data['Merlin_564']

        del feature_data['location']
        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'transcript', 'cv': {'name': 'sequence'}}
        assert len(feature_data['children']) == 1

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tpseudogene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content

    def test_create_ncRNA(self):
        path = 'test-data/ncrna-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_100_ncRNA' in feature_data

        feature_data = feature_data['Merlin_100_ncRNA']

        # del feature_data['location']['id']
        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'ncRNA', 'cv': {'name': 'sequence'}}
        assert len(feature_data['children']) == 1

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tncRNA\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content

    def test_create_repeat_region(self):
        path = 'test-data/repeat-region-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_800' in feature_data

        feature_data = feature_data['Merlin_800']

        # del feature_data['location']['id']
        assert feature_data['location'] == {'strand': 1, 'fmin': 1, 'fmax': 691}
        assert feature_data['type'] == {'name': 'repeat_region', 'cv': {'name': 'sequence'}}
        assert 'children' not in feature_data

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\trepeat_region\t2\t691\t.\t+\t.' in gff_content

    def setUp(self):
        # Make sure the organism is not already there
        temp_org_info = wa.organisms.show_organism('temp_org')
        print("B info: "+str(temp_org_info))
        if 'directory' in temp_org_info:
            wa.organisms.delete_organism(temp_org_info['id'])
            self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('alt_org')
        print("org info: "+str(org_info))
        if 'directory' not in org_info:
            # Should not happen, but let's be tolerant...
            # Error received when it fails: {'error': 'No row with the given identifier exists: [org.bbop.apollo.Organism#1154]'}
            time.sleep(1)
            org_info = wa.organisms.show_organism('alt_org')

        print("organism "+str(org_info))
        wa.organisms.add_organism('temp_org', org_info['directory'])
        self.waitOrgCreated('temp_org')
        org_info = wa.organisms.show_organism('temp_org')
        print("org info: " + str(org_info))
        assert org_info['commonName'] == 'temp_org'

    def tearDown(self):
        org_info = wa.organisms.show_organism('temp_org')

        if org_info and 'id' in org_info:
            wa.organisms.delete_features(org_info['id'])
            wa.organisms.delete_organism(org_info['id'])

        self.waitOrgDeleted('temp_org')
