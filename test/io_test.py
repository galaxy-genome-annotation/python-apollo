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

        ## actual annotated merlin:
        # ##gff-version 3
        # ##sequence-region Merlin 1 172788
        # Merlin	.	gene	5011	6066	.	-	.	owner=nathandunn@lbl.gov;ID=1f1b5522-180d-49e6-b8f1-db835d85894e;date_last_modified=2020-10-13;Name=Merlin_42_mRNA;date_creation=2020-10-13
        # Merlin	.	mRNA	5011	6066	.	-	.	owner=nathandunn@lbl.gov;Parent=1f1b5522-180d-49e6-b8f1-db835d85894e;ID=5fc2cc4e-2dce-40ce-88c4-243e7339c059;orig_id=Merlin_42_mRNA;date_last_modified=2020-10-13;Name=Merlin_42_mRNA-00001;date_creation=2020-10-13
        # Merlin	.	CDS	5289	6065	.	-	0	Parent=5fc2cc4e-2dce-40ce-88c4-243e7339c059;ID=5fc2cc4e-2dce-40ce-88c4-243e7339c059-CDS;Name=5fc2cc4e-2dce-40ce-88c4-243e7339c059-CDS
        # Merlin	.	exon	5011	6066	.	-	.	Parent=5fc2cc4e-2dce-40ce-88c4-243e7339c059;ID=3cc921e5-b61e-4040-a42d-ca31b07840a7;Name=3cc921e5-b61e-4040-a42d-ca31b07840a7
        # ###
        # Merlin	.	gene	2	691	.	+	.	owner=nathandunn@lbl.gov;ID=e597dee3-e427-472d-b060-2e86db6ca530;date_last_modified=2020-10-13;Name=Merlin_1_mRNA;date_creation=2020-10-13
        # Merlin	.	mRNA	2	691	.	+	.	owner=nathandunn@lbl.gov;Parent=e597dee3-e427-472d-b060-2e86db6ca530;ID=5a071d42-9dc4-4f78-b585-44b0fa3f8dd3;orig_id=Merlin_1_mRNA;date_last_modified=2020-10-13;Name=Merlin_1_mRNA-00001;date_creation=2020-10-13
        # Merlin	.	CDS	2	691	.	+	0	Parent=5a071d42-9dc4-4f78-b585-44b0fa3f8dd3;ID=5a071d42-9dc4-4f78-b585-44b0fa3f8dd3-CDS;Name=5a071d42-9dc4-4f78-b585-44b0fa3f8dd3-CDS
        # Merlin	.	exon	2	691	.	+	.	Parent=5a071d42-9dc4-4f78-b585-44b0fa3f8dd3;ID=49a16f9f-5a43-4456-b21f-24b6b91edcdd;Name=49a16f9f-5a43-4456-b21f-24b6b91edcdd
        # ###
        # Merlin	.	gene	3066	4796	.	-	.	owner=nathandunn@lbl.gov;ID=c648c204-d858-40e0-b812-58d6193939b7;date_last_modified=2020-10-13;Name=Merlin_5_mRNA;date_creation=2020-10-13
        # Merlin	.	mRNA	3066	4796	.	-	.	owner=nathandunn@lbl.gov;Parent=c648c204-d858-40e0-b812-58d6193939b7;ID=d7be3b48-a7d1-430f-9a28-3af2c3340df6;orig_id=Merlin_5_mRNA;date_last_modified=2020-10-13;Name=Merlin_5_mRNA-00001;date_creation=2020-10-13
        # Merlin	.	non_canonical_three_prime_splice_site	4297	4297	.	-	.	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=d7be3b48-a7d1-430f-9a28-3af2c3340df6-non_canonical_three_prime_splice_site-4296;Name=d7be3b48-a7d1-430f-9a28-3af2c3340df6-non_canonical_three_prime_splice_site-4296
        # Merlin	.	non_canonical_five_prime_splice_site	4364	4364	.	-	.	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=d7be3b48-a7d1-430f-9a28-3af2c3340df6-non_canonical_five_prime_splice_site-4363;Name=d7be3b48-a7d1-430f-9a28-3af2c3340df6-non_canonical_five_prime_splice_site-4363
        # Merlin	.	exon	4366	4796	.	-	.	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=6b6cc027-a3b0-4459-a61c-e05638be1b64;Name=6b6cc027-a3b0-4459-a61c-e05638be1b64
        # Merlin	.	CDS	4366	4796	.	-	0	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=d7be3b48-a7d1-430f-9a28-3af2c3340df6-CDS;Name=d7be3b48-a7d1-430f-9a28-3af2c3340df6-CDS
        # Merlin	.	CDS	3066	4296	.	-	1	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=d7be3b48-a7d1-430f-9a28-3af2c3340df6-CDS;Name=d7be3b48-a7d1-430f-9a28-3af2c3340df6-CDS
        # Merlin	.	exon	3066	4296	.	-	.	Parent=d7be3b48-a7d1-430f-9a28-3af2c3340df6;ID=8f2f37f4-c43f-47dc-8fd3-7d801a8655bc;Name=8f2f37f4-c43f-47dc-8fd3-7d801a8655bc
        # ###
        # Merlin	.	gene	752	1039	.	+	.	owner=nathandunn@lbl.gov;ID=3eccda32-4c57-426a-9edf-09d89823aaae;date_last_modified=2020-10-13;Name=mrna-name;date_creation=2020-10-13
        # Merlin	.	mRNA	752	1039	.	+	.	owner=nathandunn@lbl.gov;Parent=3eccda32-4c57-426a-9edf-09d89823aaae;ID=ab10df73-c4fb-4c7f-a5c4-dc6ebfd9a471;orig_id=Merlin_2_mRNA;date_last_modified=2020-10-13;Name=mrna-name-00001;date_creation=2020-10-13
        # Merlin	.	CDS	752	1039	.	+	0	Parent=ab10df73-c4fb-4c7f-a5c4-dc6ebfd9a471;ID=ab10df73-c4fb-4c7f-a5c4-dc6ebfd9a471-CDS;Name=ab10df73-c4fb-4c7f-a5c4-dc6ebfd9a471-CDS
        # Merlin	.	exon	752	1039	.	+	.	Parent=ab10df73-c4fb-4c7f-a5c4-dc6ebfd9a471;ID=b04a1271-0843-4ee2-87ce-da9c2f70d0e3;Name=b04a1271-0843-4ee2-87ce-da9c2f70d0e3
        # ###
        # Merlin	.	gene	1067	2011	.	-	.	owner=nathandunn@lbl.gov;ID=fe20fc72-c779-47d9-868a-0ff488d88709;date_last_modified=2020-10-13;Name=Merlin_3_mRNA;date_creation=2020-10-13
        # Merlin	.	mRNA	1067	2011	.	-	.	owner=nathandunn@lbl.gov;Parent=fe20fc72-c779-47d9-868a-0ff488d88709;ID=e7fecff7-4f5a-42e9-add2-20e365c20b0a;orig_id=Merlin_3_mRNA;date_last_modified=2020-10-13;Name=Merlin_3_mRNA-00001;date_creation=2020-10-13
        # Merlin	.	exon	1067	2011	.	-	.	Parent=e7fecff7-4f5a-42e9-add2-20e365c20b0a;ID=f89259fb-2a21-46c8-9670-765d16d5f1ac;Name=f89259fb-2a21-46c8-9670-765d16d5f1ac
        # Merlin	.	CDS	1067	2011	.	-	0	Parent=e7fecff7-4f5a-42e9-add2-20e365c20b0a;ID=e7fecff7-4f5a-42e9-add2-20e365c20b0a-CDS;Name=e7fecff7-4f5a-42e9-add2-20e365c20b0a-CDS
        # ###
        # Merlin	.	gene	2011	3066	.	-	.	owner=nathandunn@lbl.gov;ID=74026405-34f3-4b5b-a0b4-4502a0e6aeea;date_last_modified=2020-10-13;Name=Merlin_4_mRNA;date_creation=2020-10-13
        # Merlin	.	mRNA	2011	3066	.	-	.	owner=nathandunn@lbl.gov;Parent=74026405-34f3-4b5b-a0b4-4502a0e6aeea;ID=4e49251c-1140-444d-a2c2-55617fa4665d;orig_id=Merlin_4_mRNA;date_last_modified=2020-10-13;Name=Merlin_4_mRNA-00001;date_creation=2020-10-13
        # Merlin	.	exon	2011	3066	.	-	.	Parent=4e49251c-1140-444d-a2c2-55617fa4665d;ID=e0e6b1a5-ffb3-42aa-a4be-f79aa058673c;Name=e0e6b1a5-ffb3-42aa-a4be-f79aa058673c
        # Merlin	.	CDS	2011	3066	.	-	0	Parent=4e49251c-1140-444d-a2c2-55617fa4665d;ID=4e49251c-1140-444d-a2c2-55617fa4665d-CDS;Name=4e49251c-1140-444d-a2c2-55617fa4665d-CDS
        # ###

        gene_count = gff_content.count('Merlin\t.\tgene')
        mrna_count = gff_content.count('Merlin\t.\tmRNA')
        exon_count = gff_content.count('Merlin\t.\texon')
        cds_count = gff_content.count('Merlin\t.\tCDS')
        non_canonical_three_prime_splice_site_count = gff_content.count(
            'Merlin\t.\tnon_canonical_three_prime_splice_site')
        non_canonical_five_prime_splice_site_count = gff_content.count('Merlin\t.\tnon_canonical_five_prime_splice_site')

        print(f'gene_count {gene_count}')
        print(f'mrna_count {mrna_count}')
        print(f'exon_count {exon_count}')
        print(f'cds_count {cds_count}')
        print(f'owner_count {gff_content.count("owner=")}')
        print(f'Parent_count {gff_content.count("Parent=")}')
        print(f'ID_count {gff_content.count("ID=")}')
        print(f'Name_count {gff_content.count("Name=")}')
        print(f'non_canonical_three_prime_splice_site_count {non_canonical_three_prime_splice_site_count}')
        print(f'non_canonical_five_prime_splice_site {non_canonical_five_prime_splice_site_count}')


        assert non_canonical_five_prime_splice_site_count == 1
        assert non_canonical_three_prime_splice_site_count == 1

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


        assert cds_count == 7  # splits up output of CDS acress the two two exons
        assert gff_content.count('Merlin\t.\tCDS\t2\t691\t.\t+\t0') == 1
        assert gff_content.count('Merlin\t.\tCDS\t752\t1039\t.\t+\t0') == 1
        assert gff_content.count('Merlin\t.\tCDS\t1067\t2011\t.\t-\t0') == 1
        assert gff_content.count('Merlin\t.\tCDS\t2011\t3066\t.\t-\t0') == 1
        assert gff_content.count('Merlin\t.\tCDS\t3066\t4296\t.\t-\t1') == 1
        assert gff_content.count('Merlin\t.\tCDS\t4366\t4796\t.\t-\t0') == 1
        assert gff_content.count('Merlin\t.\tCDS\t5011\t6066\t.\t-\t0') == 1

        assert exon_count == 7
        assert gff_content.count('Merlin\t.\texon\t2\t691\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t752\t1039\t.\t+\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t1067\t2011\t') == 1
        assert gff_content.count('Merlin\t.\texon\t2011\t3066\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t3066\t4296\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\texon\t4366\t4796\t') == 1
        assert gff_content.count('Merlin\t.\texon\t5011\t6066\t') == 1


        assert gff_content.count('Merlin\t.\tnon_canonical_three_prime_splice_site\t4297\t4297\t.\t-\t.') == 1
        assert gff_content.count('Merlin\t.\tnon_canonical_five_prime_splice_site\t4364\t4364\t.\t-\t.') == 1

        assert gff_content.count('ID=') == 28
        assert gff_content.count('Name=') == 28
        assert gff_content.count('owner=') == 12 # just for gene and mRNA or other top-level ones
        assert gff_content.count('Parent=') == 22 # all but genes should have parent

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
