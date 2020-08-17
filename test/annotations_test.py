import time
import unittest

from . import ApolloTestCase, wa
from apollo import util


class AnnotationsTest(ApolloTestCase):

    def test_inclusion(self):
        assert ("gene" in util.gene_types)

    def test_mrna_top(self):
        path = 'test-data/mrna-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        print("output feature data" + str(feature_data))

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

    @unittest.skip("temporarily disabled until we get the data correctly")
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

        # print("gff content")
        # print(gff_content)

        ## NOTE: official GFF3
        ###gff-version 3
        ##sequence-region Merlin 1 172788
        # Merlin	.	gene	13066	14796	.	-	.	owner=nathandunn@lbl.gov;ID=095526e1-e79f-4db0-bb52-630f4ec126fa;date_last_modified=2020-08-17;Name=Merlin_58_mRNA;date_creation=2020-08-17
        # Merlin	.	mRNA	13066	14796	.	-	.	owner=nathandunn@lbl.gov;Parent=095526e1-e79f-4db0-bb52-630f4ec126fa;ID=efec3854-efd8-47c0-b41f-0d8ad5e3c17e;date_last_modified=2020-08-17;Name=Merlin_58_mRNA-00001;date_creation=2020-08-17
        # Merlin	.	non_canonical_five_prime_splice_site	14364	14364	.	-	.	Parent=efec3854-efd8-47c0-b41f-0d8ad5e3c17e;ID=efec3854-efd8-47c0-b41f-0d8ad5e3c17e-non_canonical_five_prime_splice_site-14363;Name=efec3854-efd8-47c0-b41f-0d8ad5e3c17e-non_canonical_five_prime_splice_site-14363
        # Merlin	.	exon	13066	14296	.	-	.	Parent=efec3854-efd8-47c0-b41f-0d8ad5e3c17e;ID=481aebac-24c1-4816-ac9a-ddd697902161;Name=481aebac-24c1-4816-ac9a-ddd697902161
        # Merlin	.	CDS	13096	13230	.	-	0	Parent=efec3854-efd8-47c0-b41f-0d8ad5e3c17e;ID=efec3854-efd8-47c0-b41f-0d8ad5e3c17e-CDS;Name=efec3854-efd8-47c0-b41f-0d8ad5e3c17e-CDS
        # Merlin	.	exon	14366	14796	.	-	.	Parent=efec3854-efd8-47c0-b41f-0d8ad5e3c17e;ID=2abc490c-d813-4295-b86f-f74c012dad5d;Name=2abc490c-d813-4295-b86f-f74c012dad5d
        # Merlin	.	mRNA	13066	14796	.	-	.	owner=nathandunn@lbl.gov;Parent=095526e1-e79f-4db0-bb52-630f4ec126fa;ID=c84ed483-a2d9-41ed-96f9-96675ab8a477;date_last_modified=2020-08-17;Name=Merlin_58_mRNA-00002;date_creation=2020-08-17
        # Merlin	.	non_canonical_five_prime_splice_site	14464	14464	.	-	.	Parent=c84ed483-a2d9-41ed-96f9-96675ab8a477;ID=c84ed483-a2d9-41ed-96f9-96675ab8a477-non_canonical_five_prime_splice_site-14463;Name=c84ed483-a2d9-41ed-96f9-96675ab8a477-non_canonical_five_prime_splice_site-14463
        # Merlin	.	CDS	13096	13230	.	-	0	Parent=c84ed483-a2d9-41ed-96f9-96675ab8a477;ID=c84ed483-a2d9-41ed-96f9-96675ab8a477-CDS;Name=c84ed483-a2d9-41ed-96f9-96675ab8a477-CDS
        # Merlin	.	exon	13066	14096	.	-	.	Parent=c84ed483-a2d9-41ed-96f9-96675ab8a477;ID=75fa77c0-6e3b-4843-916e-bfac9bf466b0;Name=75fa77c0-6e3b-4843-916e-bfac9bf466b0
        # Merlin	.	exon	14466	14796	.	-	.	Parent=c84ed483-a2d9-41ed-96f9-96675ab8a477;ID=c7a8bac5-37c6-4d97-9102-d66b56d23b93;Name=c7a8bac5-37c6-4d97-9102-d66b56d23b93
        # Merlin	.	non_canonical_three_prime_splice_site	14097	14097	.	-	.	Parent=c84ed483-a2d9-41ed-96f9-96675ab8a477;ID=c84ed483-a2d9-41ed-96f9-96675ab8a477-non_canonical_three_prime_splice_site-14096;Name=c84ed483-a2d9-41ed-96f9-96675ab8a477-non_canonical_three_prime_splice_site-14096
        ###


        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t13066\t14796\t.\t-\t.' in gff_content
        assert 'Merlin\t.\tmRNA\t13066\t14796\t.\t-\t.' in gff_content
        assert 'Merlin\t.\texon\t13066\t14296\t.\t-\t.' in gff_content
        # TODO: this is wrong for some reason
        assert 'Merlin\t.\texon\t14466\t14796\t.\t-\t.' in gff_content
        # this is correct
        assert 'Merlin\t.\tCDS\t13096\t13230\t.\t-\t0' in gff_content

    def test_create_pseudogene(self):
        path = 'test-data/pseudogene-top.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)

        assert 'Merlin_564' in feature_data

        feature_data = feature_data['Merlin_564']

        # del feature_data['location']
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
        print("B info: " + str(temp_org_info))
        if 'directory' in temp_org_info:
            wa.organisms.delete_organism(temp_org_info['id'])
            self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('alt_org')
        print("org info: " + str(org_info))
        if 'directory' not in org_info:
            # Should not happen, but let's be tolerant...
            # Error received when it fails: {'error': 'No row with the given identifier exists: [org.bbop.apollo.Organism#1154]'}
            time.sleep(1)
            org_info = wa.organisms.show_organism('alt_org')

        print("organism " + str(org_info))
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
