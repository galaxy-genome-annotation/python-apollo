from . import ApolloTestCase, wa


class OrganismTest(ApolloTestCase):

    def test_get_organisms(self):

        orgs = wa.organisms.get_organisms()

        assert len(orgs) == 4

        first_org = orgs[0]

        assert 'nonDefaultTranslationTable' in first_org
        assert 'annotationCount' in first_org
        assert 'commonName' in first_org
        assert 'obsolete' in first_org
        assert 'id' in first_org
        assert 'publicMode' in first_org
        assert 'valid' in first_org
        assert 'currentOrganism' in first_org
        assert 'sequences' in first_org
        assert 'directory' in first_org
        assert 'blatdb' in first_org
        assert 'genus' in first_org
        assert 'species' in first_org
        assert 'metadata' in first_org

        assert first_org['commonName'] == 'test_organism'
        assert 'apollo_shared_dir/org' in first_org['directory']
        assert first_org['genus'] == 'Testus'
        assert first_org['species'] == 'organus'
