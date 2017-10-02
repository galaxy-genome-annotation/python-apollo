"""
Contains possible interactions with the Apollo Canned Keys Module
"""
from apollo.client import Client


class CannedKeysClient(Client):
    CLIENT_BASE = '/cannedKey/'

    def add_key(self, key, metadata=""):
        """
        Add a canned key

        :type key: str
        :param key: New canned key

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: A dictionnary containing canned key description
        """
        data = {
            'key': key,
            'metadata': metadata
        }

        return self.post('createKey', data)

    def get_keys(self):
        """
        Get all canned keys available in this Apollo instance

        :rtype: list of dicts
        :return: list of canned key info dictionaries
        """
        return self.post('showKey', {})

    def show_key(self, value):
        """
        Get a specific canned key

        :type value: str
        :param value: Canned key to show

        :rtype: dict
        :return: A dictionnary containing canned key description
        """
        keys = self.get_keys()
        keys = [x for x in keys if x['label'] == value]
        if len(keys) == 0:
            raise Exception("Unknown key")
        else:
            return keys[0]

    def update_key(self, id_number, new_key, metadata=None):
        """
        Update a canned key

        :type id_number: int
        :param id_number: canned key ID number

        :type new_key: str
        :param new_key: New canned key value

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number,
            'new_key': new_key
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateKey', data)

    def delete_key(self, id_number):
        """
        Update a canned key

        :type id_number: int
        :param id_number: canned key ID number

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number
        }

        return self.post('deleteKey', data)
