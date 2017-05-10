"""
Contains possible interactions with the Apollo Status Module
"""
from apollo.client import Client


class StatusClient(Client):
    CLIENT_BASE = '/availableStatus/'

    def addStatus(self, value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'value': value
        }

        return self.post('createStatus', data)

    def findAllStatuses(self):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        return self.post('showStatus', {})

    def findStatusByValue(self, value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        statuses = self.findAllStatuses()
        statuses = [x for x in statuses if x['value'] == value]
        if len(statuses) == 0:
            raise Exception("Unknown status value")
        else:
            return statuses[0]

    def findStatusById(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        statuses = self.findAllStatuses()
        statuses = [x for x in statuses if str(x['id']) == str(id_number)]
        if len(statuses) == 0:
            raise Exception("Unknown ID")
        else:
            return statuses[0]

    def updateStatus(self, id_number, new_value):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number,
            'new_value': new_value
        }

        return self.post('updateStatus', data)

    def deleteStatus(self, id_number):
        """
        TODO: Undocumented

        :rtype: dict
        :return: ???
        """
        data = {
            'id': id_number
        }

        return self.post('deleteStatus', data)
