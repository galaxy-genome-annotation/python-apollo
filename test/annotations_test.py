from BCBio import GFF

from . import ApolloTestCase, wa
from apollo import util


class AnnotationsTest(ApolloTestCase):

    def test_features_to_apollo_schema(self):
        path = 'test-data/mrna-top.gff'
        with open(path) as file:
            print(file.read())
            file.close()
        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            feature_data = util.features_to_apollo_schema(rec.features, feature_list, transcript_list)

        in_handle.close()
        print(str(feature_data))
        print(str(len(feature_data)))

        assert(len(feature_data)==1)



    def test_create_mrna(self):
        # org_info = self.waitOrgCreated('temp_org')
        # assert org_info['commonName'] == 'temp_org'
        path = 'test-data/mrna-top.gff'

        with open(path) as file:
            print(file.read())
            file.close()

        # entries = GFF.parse(in_handle)
        # print(entries.features.__sizeof__())
        feature_list = []
        transcript_list = []
        in_handle = open(path)
        for rec in GFF.parse(in_handle):
            print("A")
            wa.annotations._process_gff_entry(rec, feature_list, transcript_list)
            print("B")

        in_handle.close()
        assert (len(feature_list) == 0)
        assert (len(transcript_list) == 1)
        print(transcript_list)
        assert(len(transcript_list[0]) == 1)
        transcript = transcript_list[0]
        assert(len(transcript['children']) == 2)
        # assert(len(transcript_list[0][0]) == 1)
        # for feature in rec.features:
        #     print ("A.1")
        # print(entries)
        # print("B")
        # print(str(entries))
        # print("C")
        # # assert(len(entries)==1)
        # print("D")
        # assert(len(entries.features)==3)

    # def setUp(self):
    # # Make sure the organism is not already there
    # temp_org_info = wa.organisms.show_organism('temp_org')
    # if 'directory' in temp_org_info:
    #     wa.organisms.delete_organism(temp_org_info['id'])
    #     self.waitOrgDeleted('temp_org')
    #
    # with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
    #     with tarfile.open(archive.name, mode="w:gz") as tar:
    #         for file in glob.glob('test-data/dataset_1_files/data/'):
    #             tar.add(file, arcname=file.replace('test-data/dataset_1_files/data/', './'))
    #     wa.remote.add_organism('temp_org', archive)
    # self.waitOrgCreated('temp_org')

    # def tearDown(self):
    # org_info = wa.organisms.show_organism('temp_org')
    #
    # if org_info and 'id' in org_info:
    #     wa.organisms.delete_organism(org_info['id'])
    #
    # self.waitOrgDeleted('temp_org')
    #
    # org_info = wa.organisms.show_organism('some_new_org_remote')
    #
    # if org_info and 'id' in org_info:
    #     wa.organisms.delete_organism(org_info['id'])
    #     self.waitOrgDeleted('some_new_org_remote')
