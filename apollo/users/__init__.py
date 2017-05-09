"""
Contains possible interactions with the Apollo Users Module
"""
import json

from apollo.client import Client


class UsersClient(Client):
    CLIENT_BASE = '/user/'

    def get_users(self):
        res = self.post('loadUsers', {})
        data = [self._fix_user_org_permissions(user) for user in res]
        return data

    def show_user(self, user):
        """
        Get a specific user

        :type user: str
        :param user: User Email

        :rtype: dict
        :return: a dictionary containing user information
        """
        return self._fix_user_org_permissions(self._loadUserById(user))

    def _fix_user_org_permissions(self, user):
        if 'organismPermissions' in user:
            orgPerms = []
            for org in user['organismPermissions']:
                org['permissions'] = json.loads(org['permissions'])
                if len(org['permissions']) > 0:
                    orgPerms.append(org)
            user['organismPermissions'] = orgPerms
        return user

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

    def _loadUserById(self, user_id):
        res = self.post('loadUsers', {'userId': user_id})
        if isinstance(res, list):
            # We can only match one, right?
            return res[0]
        else:
            return res

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
        if len(response.keys()) == 0:
            return self.show_user(email)
        else:
            # Error
            return response

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
        :return: an empty dictionary
        """
        data = {
            'email': email,
            'firstName': first_name,
            'lastName': last_name,
            'newPassword': password,
            'metadata': metadata,
        }
        return self.post('updateUser', data)
