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
        tries = 1
        while 'directory' in org_info and tries < 10:
            time.sleep(1)
            org_info = wa.organisms.show_organism(org_id)
            tries += 1

        return org_info

    def waitOrgCreated(self, org_id):
        """
        Wait for an organism to be really created from Apollo
        """

        org_info = wa.organisms.show_organism(org_id)
        tries = 1
        while 'directory' not in org_info and tries < 10:
            time.sleep(1)
            org_info = wa.organisms.show_organism(org_id)
            tries += 1

        return org_info

    def waitUserDeleted(self, user_id):
        """
        Wait for an user to be really deleted from Apollo
        """

        user_info = wa.users.show_user(user_id)
        tries = 1
        while 'userId' in user_info and tries < 10:
            time.sleep(1)
            user_info = wa.users.show_user(user_id)
            tries += 1

        return user_info

    def waitUserCreated(self, user_id):
        """
        Wait for an user to be really created from Apollo
        """

        user_info = wa.users.show_user(user_id)
        tries = 1
        while 'userId' not in user_info and tries < 10:
            time.sleep(1)
            user_info = wa.users.show_user(user_id)
            tries += 1

        return user_info
