"""
Contains possible interactions with the Apollo Canned Values Module
"""
from apollo.client import Client


class CannedValuesClient(Client):
    CLIENT_BASE = '/cannedValue/'

    def addValue(self, value, metadata=""):
        data = {
            'value': value,
            'metadata': metadata
        }

        return self.request('createValue', data)

    def findAllValues(self):
        return self.request('showValue', {})

    def findValueByValue(self, value):
        values = self.findAllValues()
        values = [x for x in values if x['label'] == value]
        if len(values) == 0:
            raise Exception("Unknown value")
        else:
            return values[0]

    def findValueById(self, id_number):
        values = self.findAllValues()
        values = [x for x in values if str(x['id']) == str(id_number)]
        if len(values) == 0:
            raise Exception("Unknown ID")
        else:
            return values[0]

    def updateValue(self, id_number, new_value, metadata=None):
        data = {
            'id': id_number,
            'new_value': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.request('updateValue', data)

    def deleteValue(self, id_number):
        data = {
            'id': id_number
        }

        return self.request('deleteValue', data)

