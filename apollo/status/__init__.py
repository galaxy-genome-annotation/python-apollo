"""
Contains possible interactions with the Apollo Status Module
"""
from apollo.client import Client


class StatusClient(Client):
    CLIENT_BASE = '/availableStatus/'

    def add_status(self, status):
        """
        Add a status value

        :type status: str
        :param status: New status

        :rtype: dict
        :return: A dictionnary containing status description
        """
        data = {
            'value': status
        }

        return self.post('createStatus', data)

    def get_statuses(self):
        """
        Get all statuses available in this Apollo instance

        :rtype: list of dicts
        :return: list of status info dictionaries
        """
        return self.post('showStatus', {})

    def show_status(self, status):
        """
        Get a specific status

        :type status: str
        :param status: Status to show

        :rtype: dict
        :return: A dictionnary containing status description
        """
        statuses = self.get_statuses()
        statuses = [x for x in statuses if x['value'] == status]
        if len(statuses) == 0:
            raise Exception("Unknown status value")
        else:
            return statuses[0]

    def update_status(self, id_number, new_value):
        """
        Update a status name

        :type id_number: int
        :param id_number: status ID number

        :type new_value: str
        :param new_value: The new status name

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number,
            'new_value': new_value
        }

        return self.post('updateStatus', data)

    def delete_status(self, id_number):
        """
        Delete a status

        :type id_number: int
        :param id_number: status ID number

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number,
        }

        return self.post('deleteStatus', data)
