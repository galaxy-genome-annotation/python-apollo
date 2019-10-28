from . import ApolloTestCase, wa


class OrganismTest(ApolloTestCase):

    def test_get_organisms(self):

        orgs = wa.organisms.get_organisms()

        assert len(orgs) == 4
