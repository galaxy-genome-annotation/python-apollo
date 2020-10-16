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

    # @unittest.skip("temporarily disabled until we get the data correctly")
    def test_isoforms(self):
        path = 'test-data/mrna-isoforms.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)
        print('feature data')
        print(str(feature_data))

        assert 'Merlin_58_mRNA' in feature_data

        # NOTE: this feature data seems to be correct
        feature_data = feature_data['Merlin_58_mRNA']

        # del feature_data['location']['id']
        print(f"output feature data: {feature_data}")
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

        print("gff content")
        print(gff_content)

        ## NOTE: official GFF3 for Apollo 2
        ###
        ###gff-version 3
        ##sequence-region Merlin 1 172788
        # Merlin	.	gene	13066	14796	.	-	.	owner=nathandunn@lbl.gov;ID=a4096c9b-91b2-46bf-948f-904eaf586999;date_last_modified=2020-08-31;Name=Merlin_58_mRNA;date_creation=2020-08-31
        # Merlin	.	mRNA	13066	14796	.	-	.	owner=nathandunn@lbl.gov;Parent=a4096c9b-91b2-46bf-948f-904eaf586999;ID=f86ce011-ac9e-4726-8051-88acc77cd76d;orig_id=Merlin_58_mRNA;date_last_modified=2020-08-31;Name=Merlin_58_mRNA-00001;date_creation=2020-08-31
        # Merlin	.	exon	13066	14296	.	-	.	Parent=f86ce011-ac9e-4726-8051-88acc77cd76d;ID=ea826d5c-46f8-4753-804d-eb5e0b737b35;Name=ea826d5c-46f8-4753-804d-eb5e0b737b35
        # Merlin	.	CDS	13096	13230	.	-	0	Parent=f86ce011-ac9e-4726-8051-88acc77cd76d;ID=f86ce011-ac9e-4726-8051-88acc77cd76d-CDS;Name=f86ce011-ac9e-4726-8051-88acc77cd76d-CDS
        # Merlin	.	non_canonical_five_prime_splice_site	14364	14364	.	-	.	Parent=f86ce011-ac9e-4726-8051-88acc77cd76d;ID=f86ce011-ac9e-4726-8051-88acc77cd76d-non_canonical_five_prime_splice_site-14363;Name=f86ce011-ac9e-4726-8051-88acc77cd76d-non_canonical_five_prime_splice_site-14363
        # Merlin	.	exon	14366	14796	.	-	.	Parent=f86ce011-ac9e-4726-8051-88acc77cd76d;ID=13fbd1ab-0a8f-490b-8535-f3a9c330cc70;Name=13fbd1ab-0a8f-490b-8535-f3a9c330cc70
        # Merlin	.	mRNA	13066	14796	.	-	.	owner=nathandunn@lbl.gov;Parent=a4096c9b-91b2-46bf-948f-904eaf586999;ID=7d536c77-0593-470e-ad4c-44aebeab8ecb;orig_id=Merlin_58b_mRNA;date_last_modified=2020-08-31;Name=Merlin_58_mRNA-00002;date_creation=2020-08-31
        # Merlin	.	non_canonical_three_prime_splice_site	14097	14097	.	-	.	Parent=7d536c77-0593-470e-ad4c-44aebeab8ecb;ID=7d536c77-0593-470e-ad4c-44aebeab8ecb-non_canonical_three_prime_splice_site-14096;Name=7d536c77-0593-470e-ad4c-44aebeab8ecb-non_canonical_three_prime_splice_site-14096
        # Merlin	.	non_canonical_five_prime_splice_site	14464	14464	.	-	.	Parent=7d536c77-0593-470e-ad4c-44aebeab8ecb;ID=7d536c77-0593-470e-ad4c-44aebeab8ecb-non_canonical_five_prime_splice_site-14463;Name=7d536c77-0593-470e-ad4c-44aebeab8ecb-non_canonical_five_prime_splice_site-14463
        # Merlin	.	exon	14466	14796	.	-	.	Parent=7d536c77-0593-470e-ad4c-44aebeab8ecb;ID=a54e5e66-e0dc-4181-9e76-c12105f4bc87;Name=a54e5e66-e0dc-4181-9e76-c12105f4bc87
        # Merlin	.	exon	13066	14096	.	-	.	Parent=7d536c77-0593-470e-ad4c-44aebeab8ecb;ID=c3fe6b30-3f66-4be7-ab5e-7984a8bb7634;Name=c3fe6b30-3f66-4be7-ab5e-7984a8bb7634
        # Merlin	.	CDS	13096	13230	.	-	0	Parent=7d536c77-0593-470e-ad4c-44aebeab8ecb;ID=7d536c77-0593-470e-ad4c-44aebeab8ecb-CDS;Name=7d536c77-0593-470e-ad4c-44aebeab8ecb-CDS
        ###

        assert '##gff-version 3' in gff_content
        # TODO: check that it shows up twice
        assert gff_content.count('Merlin\t.\tgene\t13066\t14796\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t13066\t14796\t.\t-\t.') == 2
        assert gff_content.count('Merlin\t.\texon\t13066\t14296\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t14366\t14796\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t14466\t14796\t.\t-\t.') == 1
        # this is correct
        assert gff_content.count('Merlin\t.\texon\t13066\t14096\t.\t-\t.') == 1

        # TODO: validate the non_canonical_five_prime_splice_site
        assert gff_content.count('Merlin\t.\tnon_canonical_five_prime_splice_site\t14364\t14364\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tnon_canonical_five_prime_splice_site\t14464\t14464\t.\t-\t.') == 1

        # TODO: validate the non_canonical_three_prime_splice_site
        assert gff_content.count('Merlin\t.\tnon_canonical_three_prime_splice_site\t14097\t14097\t.\t-\t.') == 1

        # TODO: validate the CDS  (2)
        assert gff_content.count('Merlin\t.\tCDS\t13096\t13230\t.\t-\t0') == 2

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
        print(gff_content)

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\trepeat_region\t2\t691\t.\t+\t.' in gff_content

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
