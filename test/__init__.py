import unittest

from arrow.apollo import get_apollo_instance
wa = get_apollo_instance()


def setup_package():
    global wa


class ApolloTestCase(unittest.TestCase):
    pass
