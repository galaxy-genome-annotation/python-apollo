from BCBio import GFF

from . import ApolloTestCase, wa
from apollo import util


class AnnotationsTest(ApolloTestCase):

    def test_features_to_apollo_schema(self):
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
        # print(str(len(feature_data)))
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
