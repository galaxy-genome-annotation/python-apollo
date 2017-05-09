"""
Contains possible interactions with the Apollo Users Module
"""
import json

from apollo.client import Client


def _fix_single_user(user):
    if 'organismPermissions' in user:
        org_perms = []
        for org in user['organismPermissions']:
            org['permissions'] = json.loads(org['permissions'])
            if len(org['permissions']) > 0:
                org_perms.append(org)
        user['organismPermissions'] = org_perms
    elif 'permissions' in user:
        user['permissions'] = json.loads(user['permissions'])
    return user


def _fix_user(user):
    # Fix the stupid empty permissions that inflate the response
    # unneccessarily.
    if isinstance(user, list):
        data = [_fix_single_user(u) for u in user]
        # Remove empty
        # data = [
        # x for x in data if
        # ('permissions' in x and len(x['permissions']) != 0)
        # ]
        return data
    else:
        return _fix_single_user(user)


class UsersClient(Client):
    CLIENT_BASE = '/user/'

    def _handle_empty(self, user, response):
        """Apollo likes to return empty user arrays, even when you REALLY
        want a user response back... like creating a user."""
        if len(response.keys()) == 0:
            return self.show_user(user)
        return response

    def get_users(self):
        """
        Get all users known to this Apollo instance

        :rtype: list of dicts
        :return: list of user info dictionaries
        """
        res = self.post('loadUsers', {})
        data = [_fix_user(user) for user in res]
        return data

    def show_user(self, user):
        """
        Get a specific user

        :type user: str
        :param user: User Email

        :rtype: dict
        :return: a dictionary containing user information
        """
        res = self.post('loadUsers', {'userId': user})
        if isinstance(res, list):
            res = res[0]
        return _fix_user(res)

    def get_organism_permissions(self, user):
        """
        Display a user's organism permissions

        :type user: str
        :param user: User's email

        :rtype: dict
        :return: a dictionary containing user's organism permissions
        """
        uop = self.show_user(user)['organismPermissions']
        return uop

    def update_organism_permissions(self, user, organism, administrate=False,
                                    write=False, export=False, read=False):
        """
        Update the permissions of a user on a specified organism

        :type user: str
        :param user: User's email

        :type organism: str
        :param organism: organism common name

        :type administrate: bool
        :param administrate: Grants administrative privileges

        :type write: bool
        :param write: Grants write privileges

        :type read: bool
        :param read: Grants read privileges

        :type export: bool
        :param export: Grants export privileges

        :rtype: dict
        :return: a dictionary containing user's organism permissions
        """
        data = {
            'userId': user,
            'organism': organism,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        response = self.post('updateOrganismPermission', data)
        response['permissions'] = json.loads(response['permissions'])
        return response

    def add_to_group(self, group, user):
        """
        Add a user to a group

        :type user: str
        :param user: User's email

        :type group: str
        :param group: Group name

        :rtype: dict
        :return: an empty dictionary
        """
        data = {'group': group, 'user': user}
        return self.post('addUserToGroup', data)

    def remove_from_group(self, group, user):
        """
        Remove a user from a group

        :type user: str
        :param user: User's email

        :type group: str
        :param group: Group name

        :rtype: dict
        :return: an empty dictionary
        """
        data = {'group': group, 'user': user}
        return self.post('removeUserFromGroup', data)

    def create_user(self, email, first_name, last_name, password, role="user", metadata={}):
        """
        Create a new user

        :type email: str
        :param email: User's email

        :type first_name: str
        :param first_name: User's first name

        :type last_name: str
        :param last_name: User's last name

        :type password: str
        :param password: User's password

        :type role: str
        :param role: User's default role, one of "admin" or "user"

        :type metadata: dict
        :param metadata: User metadata

        :rtype: dict
        :return: an empty dictionary
        """
        data = {
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'metadata': metadata,
            'role': role.upper() if role else role,
            'newPassword': password,
        }
        response = self.post('createUser', data)
        return self._handle_empty(email, response)

    def delete_user(self, user):
        """
        Delete a user

        :type user: str
        :param user: User's email

        :rtype: dict
        :return: an empty dictionary
        """
        return self.post('deleteUser', {'userToDelete': user})

    def update_user(self, email, first_name, last_name, password, metadata={}):
        """
        Update an existing user

        :type email: str
        :param email: User's email

        :type first_name: str
        :param first_name: User's first name

        :type last_name: str
        :param last_name: User's last name

        :type password: str
        :param password: User's password

        :type metadata: dict
        :param metadata: User metadata

        :rtype: dict
        :return: a dictionary containing user information
        """
        data = {
            'email': email,
            'firstName': first_name,
            'lastName': last_name,
            'newPassword': password,
            'metadata': metadata,
        }
        response = self.post('updateUser', data)
        return self._handle_empty(email, response)
