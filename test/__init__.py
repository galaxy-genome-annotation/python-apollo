import time
import unittest

from arrow.apollo import get_apollo_instance
wa = get_apollo_instance()


def setup_package():
    global wa


class ApolloTestCase(unittest.TestCase):

    def waitOrgDeleted(self, org_id):
        """
        Wait for an organism to be really deleted from Apollo
        """

        org_info = wa.organisms.show_organism(org_id)
        if 'directory' in org_info:
            time.sleep(1)
            org_info = wa.organisms.show_organism(org_id)

        return org_info

    def waitOrgCreated(self, org_id):
        """
        Wait for an organism to be really created from Apollo
        """

        org_info = wa.organisms.show_organism(org_id)
        if 'directory' not in org_info:
            time.sleep(1)
            org_info = wa.organisms.show_organism(org_id)

        return org_info
