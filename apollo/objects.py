import json


class GroupObj(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']

        if 'id' in kwargs:
            self.groupId = kwargs['id']


class UserObj(object):
    ROLE_USER = 'USER'
    ROLE_ADMIN = 'ADMIN'

    def __init__(self, **kwargs):
        # Generally expect 'userId', 'firstName', 'lastName', 'username' (email)
        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

        if 'groups' in kwargs:
            groups = []
            for groupData in kwargs['groups']:
                groups.append(GroupObj(**groupData))
            self.groups = groups

        self.__props = kwargs.keys()

    def isAdmin(self):
        if hasattr(self, 'role'):
            return self.role == self.ROLE_ADMIN
        return False

    def refresh(self, wa):
        # This method requires some sleeping usually.
        newU = wa.users.loadUser(self).toDict()
        for prop in newU:
            setattr(self, prop, newU[prop])

    def toDict(self):
        data = {}
        for prop in self.__props:
            data[prop] = getattr(self, prop)
        return data

    def orgPerms(self):
        for orgPer in self.organismPermissions:
            if len(orgPer['permissions']) > 2:
                orgPer['permissions'] = json.loads(orgPer['permissions'])
                yield orgPer

    def __str__(self):
        return '<User %s: %s %s <%s>>' % (self.userId, self.firstName,
                                          self.lastName, self.username)



