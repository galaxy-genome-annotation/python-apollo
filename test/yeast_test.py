import time

from . import ApolloTestCase, wa


class YeastLoadTest(ApolloTestCase):

    def test_single_trna(self):
        path = 'test-data/yeastI/raw/single_trna_yeastI.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))
        assert '##gff-version 3' in gff_content
        assert 'I\t.\tgene\t166267\t166339\t.\t+\t.\t' in gff_content
        assert 'I	.	tRNA	166267	166339	.	+	.	' in gff_content
        assert 'I	.	exon	166267	166339	.	+	.	' in gff_content


    def test_single_mrna_yeast(self):
        path = 'test-data/yeastI/raw/single_mrna_yeastI.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)
        assert 'transcript:YAL069W_mRNA' in feature_data
        feature_data = feature_data['transcript:YAL069W_mRNA']
        assert feature_data['location'] == {'strand': 1, 'fmin': 334, 'fmax': 649}
        assert feature_data['type'] == {'name': 'mRNA', 'cv': {'name': 'sequence'}}
        assert feature_data['parent_type']['name'] == 'gene'
        assert feature_data['parent_name'] == 'transcript:YAL069W_mRNA'
        assert feature_data['name'] == 'transcript:YAL069W_mRNA-00001'
        assert len(feature_data['children']) == 2

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))
        assert '##gff-version 3' in gff_content
        assert 'I\t.\tgene\t335\t649\t.\t+\t.\t' in gff_content
        assert 'I	.	mRNA	335	649	.	+	.	' in gff_content
        assert 'I	.	exon	335	649	.	+	.	' in gff_content
        assert 'I	.	CDS	335	649	.	+	0	' in gff_content

    def test_bulk_mix_transcript(self):
        path = 'test-data/yeastI/raw/mix_transcripts_types.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)
        print("output feature data" + str(feature_data))

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\tgene\t') == 23
        assert gff_content.count('I\t.\tmRNA\t') == 20
        assert gff_content.count('I\t.\texon\t') == 25
        assert gff_content.count('I\t.\tCDS\t') == 20
        assert gff_content.count('I\t.\tncRNA\t') == 0
        assert gff_content.count('I\t.\ttRNA\t') == 3

    def test_transposable_elements(self):
        path = 'test-data/yeastI/raw/transposable_elements.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)
        print("output feature data" + str(feature_data))
        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\ttransposable_element\t') == 2
        assert 'I\t.\ttransposable_element\t160597\t164187\t.\t-\t.' in gff_content
        assert 'I\t.\ttransposable_element\t164544\t165866\t.\t-\t.' in gff_content


    def test_mix_bulk_safe(self):
        path = 'test-data/yeastI/raw/safe_other_types.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)

        print("output feature data" + str(feature_data))

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\tgene\t') == 23

        assert gff_content.count('I\t.\tmRNA\t') == 20
        assert gff_content.count('I\t.\texon\t') == 25
        assert gff_content.count('I\t.\tCDS\t') == 20
        assert gff_content.count('I\t.\ttransposable_element\t') == 2
        assert 'I\t.\ttransposable_element\t160597\t164187\t.\t-\t.' in gff_content
        assert 'I\t.\ttransposable_element\t164544\t165866\t.\t-\t.' in gff_content
        # TODO: this gets cast as an ncRNA, whgich is incorrect
        assert gff_content.count('I\t.\tncRNA\t') == 0
        assert gff_content.count('I\t.\ttRNA\t') == 3

    def test_bulk_mrna_yeast(self):
        path = 'test-data/yeastI/raw/bulk_load_yeastI.gff'
        feature_data = wa.annotations.load_gff3('temp_org', path)
        print("output feature data" + str(feature_data))
        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\tgene\t') == 51
        assert gff_content.count('I\t.\tmRNA\t') == 51
        assert gff_content.count('I\t.\texon\t') == 51
        assert gff_content.count('I\t.\tCDS\t') == 51

    def test_other_yeast_types_bulk(self):
        path = 'test-data/yeastI/raw/other_types_yeastI.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path)
        print("output feature data" + str(feature_data))
        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")

        print(str(gff_content))
        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\tgene\t') == 23
        assert gff_content.count('I\t.\tmRNA\t') == 20
        assert gff_content.count('I\t.\texon\t') == 25
        assert gff_content.count('I\t.\tCDS\t') == 20
        assert gff_content.count('I\t.\ttransposable_element\t') == 2
        assert 'I\t.\ttransposable_element\t160597\t164187\t.\t-\t.' in gff_content
        assert 'I\t.\ttransposable_element\t164544\t165866\t.\t-\t.' in gff_content
        # TODO: this gets cast as an ncRNA, whgich is incorrect
        assert gff_content.count('I\t.\tncRNA\t') == 0
        assert gff_content.count('I\t.\ttRNA\t') == 3

    def test_multiexon_yeastI(self):
        path = 'test-data/yeastI/raw/multiexon_yeastI.gff'

        feature_data = wa.annotations.load_gff3('temp_org', path, batch_size=10)
        print("output feature data" + str(feature_data))

        # Now download back the gff
        uuid_gff = wa.io.write_downloadable('temp_org', 'GFF3')
        if 'error' in uuid_gff or 'uuid' not in uuid_gff:
            raise Exception("Apollo failed to prepare the GFF3 file for download: %s" % uuid_gff)

        time.sleep(1)

        gff_content = wa.io.download(uuid_gff['uuid'], output_format="text")
        print(str(gff_content))

        assert '##gff-version 3' in gff_content
        assert gff_content.count('I\t.\tgene\t') == 1
        assert gff_content.count('I\t.\tmRNA\t') == 1
        assert gff_content.count('I\t.\texon\t') == 2
        assert gff_content.count('I\t.\tCDS\t') == 1

    def setUp(self):
        # Make sure the organism is not already there
        temp_org_info = wa.organisms.show_organism('temp_org')
        if 'directory' in temp_org_info:
            wa.organisms.delete_organism(temp_org_info['id'])
            self.waitOrgDeleted('temp_org')

        org_info = wa.organisms.show_organism('yeastI')
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
