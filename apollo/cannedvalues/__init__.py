"""
Contains possible interactions with the Apollo Canned Values Module
"""
from apollo.client import Client


class CannedValuesClient(Client):
    CLIENT_BASE = '/cannedValue/'

    def add_value(self, value, metadata=""):
        """
        Add a canned value

        :type value: str
        :param value: New canned value

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: A dictionnary containing canned value description
        """
        data = {
            'value': value,
            'metadata': metadata
        }

        return self.post('createValue', data)

    def get_values(self):
        """
        Get all canned values available in this Apollo instance

        :rtype: list of dicts
        :return: list of canned value info dictionaries
        """
        return self.post('showValue', {})

    def show_value(self, value):
        """
        Get a specific canned value

        :type value: str
        :param value: Canned value to show

        :rtype: dict
        :return: A dictionnary containing canned value description
        """
        values = self.get_values()
        values = [x for x in values if x['label'] == value]
        if len(values) == 0:
            raise Exception("Unknown value")
        else:
            return values[0]

    def update_value(self, id_number, new_value, metadata=None):
        """
        Update a canned value

        :type id_number: int
        :param id_number: canned value ID number

        :type new_value: str
        :param new_value: New canned value value

        :type metadata: str
        :param metadata: Optional metadata

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number,
            'new_value': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.post('updateValue', data)

    def delete_value(self, id_number):
        """
        Update a canned value

        :type id_number: int
        :param id_number: canned value ID number

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number
        }

        return self.post('deleteValue', data)
