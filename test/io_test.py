import unittest

from . import ApolloTestCase, wa
import time


class IoTest(ApolloTestCase):

    def test_export_gff3(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_gff = wa.io.write_downloadable(org['commonName'], 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")
        print("gff content: " + str(gff_content))
        out_file = open("test_gff.gff", 'w')
        out_file.write(gff_content)
        out_file.close()

        assert '##gff-version 3' in gff_content
        assert 'Merlin\t.\tgene\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tmRNA\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\texon\t2\t691\t.\t+\t.' in gff_content
        assert 'Merlin\t.\tCDS\t2\t691\t.\t+\t0' in gff_content

        # we don't capture the score in the uploaded GFF3 unless it is passed in column 9
        # assert 'score=["-1335.034872"]' in gff_content
        # assert 'Merlin\t.\tnon_canonical_three_prime_splice_site\t4297\t4297\t.\t-\t.' in gff_content
        # assert 'Merlin\t.\tnon_canonical_five_prime_splice_site\t4364\t4364\t.\t-\t.' in gff_content

        # input:
        # ##gff-version 3
        # ##sequence-region Merlin 1 172788
        # Merlin	GeneMark.hmm	gene	2	691	-856.563659	+	.	ID=Merlin_1;seqid=Merlin
        # Merlin	GeneMark.hmm	mRNA	2	691	.	+	.	ID=Merlin_1_mRNA;Parent=Merlin_1;seqid=Merlin;color=#00ff00
        # Merlin	GeneMark.hmm	exon	2	691	.	+	.	ID=Merlin_1_exon;Parent=Merlin_1_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	2	691	.	+	0	ID=Merlin_1_CDS;Parent=Merlin_1_exon;seqid=Merlin
        # Merlin	GeneMark.hmm	gene	752	1039	-339.046618	+	.	ID=Merlin_2;seqid=Merlin
        # Merlin	GeneMark.hmm	mRNA	752	1039	.	+	.	ID=Merlin_2_mRNA;Parent=Merlin_2;seqid=Merlin;Name=mrna-name
        # Merlin	GeneMark.hmm	exon	752	1039	.	+	.	ID=Merlin_2_exon;Parent=Merlin_2_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	852	939	.	+	0	ID=Merlin_2_CDS;Parent=Merlin_2_exon;seqid=Merlin
        # Merlin	GeneMark.hmm	gene	1067	2011	-1229.683915	-	.	ID=Merlin_3;seqid=Merlin
        # Merlin	GeneMark.hmm	mRNA	1067	2011	.	-	.	ID=Merlin_3_mRNA;Parent=Merlin_3;seqid=Merlin
        # Merlin	GeneMark.hmm	exon	1067	2011	.	-	.	ID=Merlin_3_exon;Parent=Merlin_3_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	1367	1811	.	-	0	ID=Merlin_3_CDS;Parent=Merlin_3_exon;seqid=Merlin
        # Merlin	GeneMark.hmm	gene	2011	3066	-1335.034872	-	.	ID=Merlin_4;seqid=Merlin
        # Merlin	GeneMark.hmm	mRNA	2011	3066	.	-	.	ID=Merlin_4_mRNA;Parent=Merlin_4;seqid=Merlin
        # Merlin	GeneMark.hmm	exon	2011	3066	.	-	.	ID=Merlin_4_exon;Parent=Merlin_4_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	2011	3066	.	-	0	ID=Merlin_4_CDS;Parent=Merlin_4_exon;seqid=Merlin
        # Merlin	GeneMark.hmm	gene	3066	4796	-2177.374893	-	.	ID=Merlin_5;seqid=Merlin;Name=multiexongene
        # Merlin	GeneMark.hmm	mRNA	3066	4796	.	-	.	ID=Merlin_5_mRNA;Parent=Merlin_5;seqid=Merlin
        # Merlin	GeneMark.hmm	exon	3066	4296	.	-	.	ID=Merlin_5_exon;Parent=Merlin_5_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	3066	4296	.	-	0	ID=Merlin_5_CDS;Parent=Merlin_5_exon;seqid=Merlin
        # Merlin	GeneMark.hmm	exon	4366	4796	.	-	.	ID=Merlin_5_exon2;Parent=Merlin_5_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	4366	4796	.	-	0	ID=Merlin_5_CDS2;Parent=Merlin_5_exon2;seqid=Merlin
        # Merlin	GeneMark.hmm	gene	5011	6066	-1335.034872	-	.	ID=Merlin_42;seqid=Merlin;Name=cds-not-under-exon
        # Merlin	GeneMark.hmm	mRNA	5011	6066	.	-	.	ID=Merlin_42_mRNA;Parent=Merlin_42;seqid=Merlin
        # Merlin	GeneMark.hmm	exon	5011	6066	.	-	.	ID=Merlin_42_exon;Parent=Merlin_42_mRNA;seqid=Merlin
        # Merlin	GeneMark.hmm	CDS	5011	6066	.	-	0	ID=Merlin_42_CDS;Parent=Merlin_42_mRNA;seqid=Merlin

        index1 = gff_content.index('##gff-version 3')
        index2 = gff_content.index('Merlin\t.\tgene\t2\t691\t.\t+\t.')

        gene_count = gff_content.count('Merlin\t.\tgene')
        mrna_count = gff_content.count('Merlin\t.\tmRNA')
        exon_count = gff_content.count('Merlin\t.\texon')
        cds_count = gff_content.count('Merlin\t.\tCDS')

        print(f'gene_count {gene_count}')
        print(f'mrna_count {mrna_count}')
        print(f'exon_count {exon_count}')
        print(f'cds_count {cds_count}')

        assert gene_count == 6
        assert gff_content.count('Merlin\t.\tgene\t2\t691\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\tgene\t752\t1039\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\tgene\t1067\t2011\t') == 1
        assert gff_content.count('Merlin\t.\tgene\t2011\t3066\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tgene\t3066\t4796\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tgene\t5011\t6066\t') == 1
        assert mrna_count == 6
        assert gff_content.count('Merlin\t.\tmRNA\t2\t691\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t752\t1039\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t1067\t2011\t') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t2011\t3066\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t3066\t4796\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tmRNA\t5011\t6066\t') == 1
        assert exon_count == 7
        assert cds_count == 7 # or 7, but I think its 6

        # assert gff_content.count('Merlin\t.\tmRNA\t2\t691\t.\t+\t.') == 1
        # assert gff_content.count('Merlin\t.\texon\t2\t691\t.\t+\t.') == 1
        # assert gff_content.count('Merlin\t.\tCDS\t2\t691\t.\t+\t0') == 1
        # assert gff_content.count('Merlin\t.\tnon_canonical_three_prime_splice_site\t4297\t4297\t.\t-\t.') == 1
        # assert gff_content.count('Merlin\t.\tnon_canonical_five_prime_splice_site\t4364\t4364\t.\t-\t.') == 1
        index3 = gff_content.index('Merlin\t.\tmRNA\t2\t691\t.\t+\t.')
        index4 = gff_content.index('Merlin\t.\texon\t2\t691\t.\t+\t.')
        index5 = gff_content.index('Merlin\t.\tCDS\t2\t691\t.\t+\t0')
        # index6 = gff_content.index('Merlin\t.\tnon_canonical_three_prime_splice_site\t4297\t4297\t.\t-\t.')
        # index7 = gff_content.index('Merlin\t.\tnon_canonical_five_prime_splice_site\t4364\t4364\t.\t-\t.')

        # TODO: uncomment all
        assert index1 < index2
        assert index2 < index3
        assert index3 < index4
        # assert index4 < index5
        # assert index5 < index6
        # assert index6 < index7

        # TODO: verify that we just see once, i.e., no duplications
        # TODO: assert that there are 6 genes, 6 mRNA's exons, CDS, etc.

    @unittest.skip("temporarily disabled")
    def test_export_vcf(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_vcf = wa.io.write_downloadable(org['commonName'], 'VCF')
        if 'error' in uuid_vcf or 'uuid' not in uuid_vcf:
            raise Exception("Apollo failed to prepare the VCF file for download: %s" % uuid_vcf)

        vcf_content = wa.io.download(uuid_vcf['uuid'], output_format="text")
        assert '##fileformat=VCFv4.2' in vcf_content
        assert '##fileDate=' in vcf_content
        assert '##source=.' in vcf_content
        assert '#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO' in vcf_content

    @unittest.skip("temporarily disabled")
    def test_export_fa_cds(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='cds')
        if 'error' in uuid_fa or 'uuid' not in uuid_fa:
            raise Exception("Apollo failed to prepare the cds FASTA file for download: %s" % uuid_fa)

        fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
        assert 'CGTTTAGACAAAGGTACATTATTGTATCGTGGCCAAAAATTAGACCTTCCTACATTCGAG' in fa_content
        assert 'ATGAAATCAATTTTTCGTATCAACGGTGTAGAAATTGTAGTTGAAGATGTAGTTCCTATG' in fa_content
        assert 'ATGAGCATTAAAGTCAGAGAATTAGATGATAAGACTGATGCTTTAATTAGCGGAGTTAAA' in fa_content
        assert 'ATGAAAAGCGAAAACATGTCCACAATGAGACGTCGTAAAGTTATCGCTGATTCAAAGGGT' in fa_content
        assert '(mRNA) 690 residues [Merlin:2-691 + strand] [cds]' in fa_content
        assert '(mRNA) 945 residues [Merlin:1067-2011 - strand] [cds]' in fa_content
        assert '(mRNA) 1662 residues [Merlin:3066-4796 - strand] [cds]' in fa_content

    @unittest.skip("temporarily disabled")
    def test_export_fa_cdna(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='cdna')
        if 'error' in uuid_fa or 'uuid' not in uuid_fa:
            raise Exception("Apollo failed to prepare the cdna FASTA file for download: %s" % uuid_fa)

        fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
        assert 'CGTTTAGACAAAGGTACATTATTGTATCGTGGCCAAAAATTAGACCTTCCTACATTCGAG' in fa_content
        assert 'ATGAAATCAATTTTTCGTATCAACGGTGTAGAAATTGTAGTTGAAGATGTAGTTCCTATG' in fa_content
        assert 'ATGCTAACTTTAGATGAATTTAAAAACCAAGCGGGTAATATAGACTTTCAGCGTACTAAT' in fa_content
        assert 'ATGAGCATTAAAGTCAGAGAATTAGATGATAAGACTGATGCTTTAATTAGCGGAGTTAAA' in fa_content
        assert '(mRNA) 690 residues [Merlin:2-691 + strand] [cdna]' in fa_content
        assert '(mRNA) 945 residues [Merlin:1067-2011 - strand] [cdna]' in fa_content
        assert '(mRNA) 1662 residues [Merlin:3066-4796 - strand] [cdna]' in fa_content

    @unittest.skip("temporarily disabled")
    def test_export_fa_peptide(self):

        org = wa.organisms.show_organism('test_organism')

        uuid_fa = wa.io.write_downloadable(org['commonName'], 'FASTA', seq_type='peptide')
        if 'error' in uuid_fa or 'uuid' not in uuid_fa:
            raise Exception("Apollo failed to prepare the peptide FASTA file for download: %s" % uuid_fa)

        fa_content = wa.io.download(uuid_fa['uuid'], output_format="text")
        assert 'RLDKGTLLYRGQKLDLPTFEHNAENKLFYFRNYVSTSLKPLIFGEFGRMFMALDDDTTIY' in fa_content
        assert 'MLTLDEFKNQAGNIDFQRTNMFSCVFATTPSAKSQQLLDQFGGMLFNNLPLNNDWLGLTQ' in fa_content
        assert 'MSIKVRELDDKTDALISGVKTSAGQSSQSAKIKSTITAQYPSERSAGNDTSGSLRVHDLY' in fa_content
        assert 'MKSENMSTMRRRKVIADSKGERDAASTASDQVDSLELIGLKLDDVQSANELVAEVIEEKG' in fa_content
        assert '(mRNA) 229 residues [Merlin:2-691 + strand] [peptide]' in fa_content
        assert '(mRNA) 314 residues [Merlin:1067-2011 - strand] [peptide]' in fa_content
        assert '(mRNA) 553 residues [Merlin:3066-4796 - strand] [peptide]' in fa_content

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
