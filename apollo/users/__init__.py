"""
Contains possible interactions with the Apollo Users Module
"""
import json

from apollo.client import Client
from apollo.objects import UserObj


class UsersClient(Client):
    CLIENT_BASE = '/user/'

    # Real one
    # def getOrganismPermissionsForUser(self, user):
    # data = {
    # 'userId': user.userId,
    # }
    # return self.post('getOrganismPermissionsForUser', data)

    # Utter frigging hack
    def getOrganismPermissionsForUser(self, user):
        """
        Display a user's organism permissions

        :type user: str
        :param user: User's email

        :rtype: dict
        :return: a dictionary containing user's organism permissions
        """
        uop = self.loadUser(user).organismPermissions
        for org in uop:
            org['permissions'] = json.loads(org['permissions'])
        return uop

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
        return self.post('updateOrganismPermission', data)

    def loadUser(self, user):
        if isinstance(user, UserObj):
            return self.loadUserById(user.userId)
        else:
            return self.loadUserById(user)

    def loadUserById(self, userId):
        res = self.post('loadUsers', {'userId': userId})
        if isinstance(res, list):
            # We can only match one, right?
            return UserObj(**res[0])
        else:
            return res

    def loadUsers(self, email=None):
        res = self.post('loadUsers', {})
        data = [UserObj(**x) for x in res]
        if email is not None:
            data = [x for x in data if x.username == email]

        return data

    def addUserToGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.post('addUserToGroup', data)

    def removeUserFromGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.post('removeUserFromGroup', data)

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
        return self.post('createUser', data)

    def deleteUser(self, user):
        return self.post('deleteUser', {'userId': user.userId})

    def updateUser(self, user, email, firstName, lastName, newPassword):
        data = {
            'userId': user.userId,
            'email': email,
            'firstName': firstName,
            'lastName': lastName,
            'newPassword': newPassword,
        }
        return self.post('updateUser', data)

