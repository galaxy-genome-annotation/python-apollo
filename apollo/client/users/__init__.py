"""
Contains possible interactions with the Apollo Users Module
"""
from apollo.client import Client
from apollo.objects import UserObj


class UsersClient(Client):
    CLIENT_BASE = '/user/'

    # Real one
    # def getOrganismPermissionsForUser(self, user):
    # data = {
    # 'userId': user.userId,
    # }
    # return self.request('getOrganismPermissionsForUser', data)

    # Utter frigging hack
    def getOrganismPermissionsForUser(self, user):
        return self.loadUser(user).organismPermissions

    def updateOrganismPermission(self, user, organism, administrate=False,
                                 write=False, export=False, read=False):
        data = {
            'userId': user.userId,
            'organism': organism,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        return self.request('updateOrganismPermission', data)

    def loadUser(self, user):
        return self.loadUserById(user.userId)

    def loadUserById(self, userId):
        res = self.request('loadUsers', {'userId': userId})
        if isinstance(res, list):
            # We can only match one, right?
            return UserObj(**res[0])
        else:
            return res

    def loadUsers(self, email=None):
        res = self.request('loadUsers', {})
        data = [UserObj(**x) for x in res]
        if email is not None:
            data = [x for x in data if x.username == email]

        return data

    def addUserToGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.request('addUserToGroup', data)

    def removeUserFromGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.request('removeUserFromGroup', data)

    def createUser(self, email, firstName, lastName, newPassword, role="user", groups=None):
        data = {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'role': role,
            'groups': [] if groups is None else groups,
            # 'availableGroups': [],
            'newPassword': newPassword,
            # 'organismPermissions': [],
        }
        return self.request('createUser', data)

    def deleteUser(self, user):
        return self.request('deleteUser', {'userId': user.userId})

    def updateUser(self, user, email, firstName, lastName, newPassword):
        data = {
            'userId': user.userId,
            'email': email,
            'firstName': firstName,
            'lastName': lastName,
            'newPassword': newPassword,
        }
        return self.request('updateUser', data)

