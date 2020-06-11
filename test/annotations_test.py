from BCBio import GFF
from BCBio.GFF import GFFExaminer
# from gffutils import inspect


from . import ApolloTestCase, wa
from apollo import util

def parse(path):
    in_handle = open(path)
    for rec in GFF.parse(in_handle):
        print("rec -> "+str(rec)+"\n")
        for f in rec.features:
            print("feature ->" + str(f)+"\n")


class AnnotationsTest(ApolloTestCase):

    def test_inclusion(self):
        assert ("gene" in util.gene_types)

    def test_features_to_apollo_schema_mrna(self):
        path = 'test-data/mrna-top.gff'
        with open(path) as file:
            print(file.read())
            file.close()
        in_handle = open(path)
        feature_data = None
        for rec in GFF.parse(in_handle):
            # feature_data = util.features_to_apollo_schema(rec.features, feature_list, transcript_list)
            feature_data = util._yieldApolloData(rec.features)

        in_handle.close()
        print(str(feature_data))
        assert (feature_data['location'] is not None)
        assert (len(feature_data['children']) == 2)

    def test_features_to_apollo_schema_gene(self):
        path = 'test-data/gene-top.gff'
        print("inspecting")
        output = parse(path)
        print(str(output))
        for o in output:
            print("AAA")
            print(str(o))
            print("BBB")
        print("inspected")

        with open(path) as file:
            print(file.read())
            file.close()
        in_handle = open(path)
        feature_data = None
        examiner = GFFExaminer()
        print(examiner.parent_child_map(in_handle))
        in_handle.close()
        in_handle = open(path)
        new_feature_list = []
        new_transcript_list = []
        for rec in GFF.parse(in_handle):
            print(str(rec))
            for f in rec.features:
                print("feature ===== start")
                print(f)
                print("feature ===== end")
            feature_data = wa.annotations._process_gff_entry(rec, new_feature_list=new_feature_list,
                                                             new_transcript_list=new_transcript_list)
            print("feature list " + str(new_feature_list))
            print("transcript list " + str(new_transcript_list))
            print("feature data" + str(feature_data))
            # assert (subfeatures is not None and len(subfeatures) > 0)
            # # feature_data = util.features_to_apollo_schema(rec.features, feature_list, transcript_list)
            # feature_data = util._yieldApolloData(rec.features)

        in_handle.close()
        print(str(feature_data))
        print("final feature list " + str(new_feature_list))
        print("final transcript list " + str(new_transcript_list))
        assert (feature_data['location'] is not None)
        assert (len(feature_data['children']) == 2)

    def test_create_mrna(self):
        path = 'test-data/mrna-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)

        in_handle.close()
        assert (len(feature_list) == 0)
        assert (len(transcript_list) == 1)
        print(transcript_list)

    def test_create_gene(self):
        path = 'test-data/gene-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)

        in_handle.close()
        print(feature_list)
        print(transcript_list)
        # assert (len(feature_list) == 0)
        # assert (len(transcript_list) == 1)

    def test_create_pseudogene(self):
        path = 'test-data/pseudogene-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)

        in_handle.close()
        assert (len(feature_list) == 1)
        assert (len(transcript_list) == 0)
        print(transcript_list)

    def test_create_ncRNA(self):
        path = 'test-data/ncrna-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)

        in_handle.close()
        assert (len(feature_list) == 0)
        assert (len(transcript_list) == 1)
        print(transcript_list)

    def test_create_repeat_region(self):
        path = 'test-data/repeat-region-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)

        in_handle.close()
        print(feature_list)
        print(transcript_list)
        assert (len(feature_list) == 1)
        assert (len(transcript_list) == 0)
