"""
Contains possible interactions with the Apollo Canned Values Module
"""
from apollo.client import Client


class CannedValuesClient(Client):
    CLIENT_BASE = '/cannedValue/'

    def addValue(self, value, metadata=""):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'value': value,
            'metadata': metadata
        }

        return self.post('createValue', data)

    def findAllValues(self):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        return self.post('showValue', {})

    def findValueByValue(self, value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        values = self.findAllValues()
        values = [x for x in values if x['label'] == value]
        if len(values) == 0:
            raise Exception("Unknown value")
        else:
            return values[0]

    def findValueById(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        values = self.findAllValues()
        values = [x for x in values if str(x['id']) == str(id_number)]
        if len(values) == 0:
            raise Exception("Unknown ID")
        else:
            return values[0]

    def updateValue(self, id_number, new_value, metadata=None):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number,
            'new_value': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateValue', data)

    def deleteValue(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number
        }

        return self.post('deleteValue', data)
