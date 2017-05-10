"""
Contains possible interactions with the Apollo Canned Keys Module
"""
from apollo.client import Client


class CannedKeysClient(Client):
    CLIENT_BASE = '/cannedKey/'

    def addKey(self, key, metadata=""):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'key': key,
            'metadata': metadata
        }

        return self.post('createKey', data)

    def findAllKeys(self):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        return self.post('showKey', {})

    def findKeyByValue(self, value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        keys = self.findAllKeys()
        keys = [x for x in keys if x['label'] == value]
        if len(keys) == 0:
            raise Exception("Unknown key")
        else:
            return keys[0]

    def findKeyById(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        keys = self.findAllKeys()
        keys = [x for x in keys if str(x['id']) == str(id_number)]
        if len(keys) == 0:
            raise Exception("Unknown ID")
        else:
            return keys[0]

    def updateKey(self, id_number, new_key, metadata=None):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number,
            'new_key': new_key
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateKey', data)

    def deleteKey(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number
        }

        return self.post('deleteKey', data)
