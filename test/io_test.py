import re

from . import ApolloTestCase, wa
import time


class IoTest(ApolloTestCase):

    def test_export_gff3(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_gff = wa.io.write_downloadable(org['commonName'], 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tmRNA\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content
        # assert 'score=["-1335.034872"]' in gff_content
        assert 'Merlin\t.\tnon_canonical_three_prime_splice_site\t4297\t4297\t.\t-\t.' in gff_content
        assert 'Merlin\t.\tnon_canonical_five_prime_splice_site\t4364\t4364\t.\t-\t.' in gff_content

    # def test_export_vcf(self):
    #
    #     org = wa.organisms.show_organism('test_organism')
    #
    #     uuid_vcf = wa.io.write_downloadable(org['commonName'], 'VCF')
    #     if 'error' in uuid_vcf or 'uuid' not in uuid_vcf:
    #         raise Exception("Apollo failed to prepare the VCF file for download: %s" % uuid_vcf)
    #
    #     vcf_content = wa.io.download(uuid_vcf['uuid'], output_format="text")
    #     assert '##fileformat=VCFv4.2' in vcf_content
    #     assert '##fileDate=20200608' in vcf_content
    #     assert '##source=.' in vcf_content
    #     assert '#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO' in vcf_content
    #
    # def test_export_fa_cds(self):
    #
    #     org = wa.organisms.show_organism('test_organism')
    #
    #     uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='cds')
    #     if 'error' in uuid_fa or 'uuid' not in uuid_fa:
    #         raise Exception("Apollo failed to prepare the cds FASTA file for download: %s" % uuid_fa)
    #
    #     fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
    #     assert 'CGTTTAGACAAAGGTACATTATTGTATCGTGGCCAAAAATTAGACCTTCCTACATTCGAG' in fa_content
    #     assert 'CACCTCAATTATCACTGCCGGTACTCAACAGCTGGTAAGAAAGTCTGGTGTATCGAAATA' in fa_content
    #     assert 'ATGAGCATTAAAGTCAGAGAATTAGATGATAAGACTGATGCTTTAATTAGCGGAGTTAAA' in fa_content
    #     assert 'ATGAAAAGCGAAAACATGTCCACAATGAGACGTCGTAAAGTTATCGCTGATTCAAAGGGT' in fa_content
    #     assert '(mRNA) 690 residues [Merlin:2-691 + strand] [cds]' in fa_content
    #     assert '(mRNA) 108 residues [Merlin:1067-2011 - strand] [cds]' in fa_content
    #     assert '(mRNA) 1662 residues [Merlin:3066-4796 - strand] [cds]' in fa_content
    #
    # def test_export_fa_cdna(self):
    #
    #     org = wa.organisms.show_organism('test_organism')
    #
    #     uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='cdna')
    #     if 'error' in uuid_fa or 'uuid' not in uuid_fa:
    #         raise Exception("Apollo failed to prepare the cdna FASTA file for download: %s" % uuid_fa)
    #
    #     fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
    #     assert 'CGTTTAGACAAAGGTACATTATTGTATCGTGGCCAAAAATTAGACCTTCCTACATTCGAG' in fa_content
    #     assert 'ATGAAATCAATTTTTCGTATCAACGGTGTAGAAATTGTAGTTGAAGATGTAGTTCCTATG' in fa_content
    #     assert 'ATGCTAACTTTAGATGAATTTAAAAACCAAGCGGGTAATATAGACTTTCAGCGTACTAAT' in fa_content
    #     assert 'ATGAGCATTAAAGTCAGAGAATTAGATGATAAGACTGATGCTTTAATTAGCGGAGTTAAA' in fa_content
    #     assert '(mRNA) 690 residues [Merlin:2-691 + strand] [cdna]' in fa_content
    #     assert '(mRNA) 945 residues [Merlin:1067-2011 - strand] [cdna]' in fa_content
    #     assert '(mRNA) 1662 residues [Merlin:3066-4796 - strand] [cdna]' in fa_content
    #
    # def test_export_fa_peptide(self):
    #
    #     org = wa.organisms.show_organism('test_organism')
    #
    #     uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='peptide')
    #     if 'error' in uuid_fa or 'uuid' not in uuid_fa:
    #         raise Exception("Apollo failed to prepare the peptide FASTA file for download: %s" % uuid_fa)
    #
    #     fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
    #     assert 'RLDKGTLLYRGQKLDLPTFEHNAENKLFYFRNYVSTSLKPLIFGEFGRMFMALDDDTTIY' in fa_content
    #     assert 'HLNYHCRYSTAGKKVWCIEISYWSNEQSCCSVFIR' in fa_content
    #     assert 'MSIKVRELDDKTDALISGVKTSAGQSSQSAKIKSTITAQYPSERSAGNDTSGSLRVHDLY' in fa_content
    #     assert 'MKSENMSTMRRRKVIADSKGERDAASTASDQVDSLELIGLKLDDVQSANELVAEVIEEKG' in fa_content
    #     assert '(mRNA) 229 residues [Merlin:2-691 + strand] [peptide]' in fa_content
    #     assert '(mRNA) 35 residues [Merlin:1067-2011 - strand] [peptide]' in fa_content
    #     assert '(mRNA) 553 residues [Merlin:3066-4796 - strand] [peptide]' in fa_content

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
