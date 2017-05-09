"""
Contains possible interactions with the Apollo Groups
"""
from apollo.client import Client
from apollo.objects import GroupObj


class GroupsClient(Client):
    CLIENT_BASE = '/group/'

    def createGroup(self, name):
        data = {'name': name}
        return self.request('createGroup', data)

    def getOrganismPermissionsForGroup(self, group):
        data = {
            'id': group.groupId,
            'name': group.name,
        }
        return self.request('getOrganismPermissionsForGroup', data)

    def loadGroup(self, group):
        return self.loadGroupById(group.groupId)

    def loadGroupById(self, groupId):
        res = self.request('loadGroups', {'groupId': groupId})
        if isinstance(res, list):
            # We can only match one, right?
            return GroupObj(**res[0])
        else:
            return res

    def loadGroupByName(self, name):
        res = self.request('loadGroups', {'name': name})
        if isinstance(res, list):
            # We can only match one, right?
            return GroupObj(**res[0])
        else:
            return res

    def loadGroups(self, group=None):
        res = self.request('loadGroups', {})
        data = [GroupObj(**x) for x in res]
        if group is not None:
            data = [x for x in data if x.name == group]

        return data

    def deleteGroup(self, group):
        data = {
            'id': group.groupId,
            'name': group.name,
        }
        return self.request('deleteGroup', data)

    def updateGroup(self, group, newName):
        # TODO: Sure would be nice if modifying ``group.name`` would invoke
        # this?
        data = {
            'id': group.groupId,
            'name': newName,
        }
        return self.request('updateGroup', data)

    def updateOrganismPermission(self, group, organismName,
                                 administrate=False, write=False, read=False,
                                 export=False):
        data = {
            'groupId': group.groupId,
            'organism': organismName,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        return self.request('updateOrganismPermission', data)

    def updateMembership(self, group, users):
        data = {
            'groupId': group.groupId,
            'user': [user.email for user in users]
        }
        return self.request('updateMembership', data)

