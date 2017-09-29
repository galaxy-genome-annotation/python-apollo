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
        :param status: New status new

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

    def update_status(self, old_value, new_value):
        """
        Update a status name

        :type old_value: str
        :param old_value: Name of the status to update

        :type new_value: str
        :param new_value: The new status name

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'old_value': old_value,
            'new_value': new_value
        }

        return self.post('updateStatus', data)

    def delete_status(self, status):
        """
        Delete a status

        :type status: str
        :param status: Name of the status to delete

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'id': id_number
        }

        return self.post('deleteStatus', data)
