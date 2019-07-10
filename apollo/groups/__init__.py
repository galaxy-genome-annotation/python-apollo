"""
Contains possible interactions with the Apollo Groups
"""
import json

from apollo.client import Client
from apollo.users import _fix_user as _fix_group


class GroupsClient(Client):
    CLIENT_BASE = '/group/'

    def create_group(self, name):
        """
        Create a new group

        :type name: str
        :param name: Group name (or a list of groups to create)

        :rtype: dict
        :return: Group information dictionary
        """
        if isinstance(name, list):
            name = ','.join(name)

        data = {'name': name}
        return self.post('createGroup', data)

    def delete_group(self, group):
        """
        Delete a group

        :type group: str
        :param group: Group name (or a list of groups to delete)

        :rtype: dict
        :return: an empty dictionary
        """
        if isinstance(group, list):
            group = ','.join(group)

        data = {
            'name': group,
        }
        return self.post('deleteGroup', data)

    def show_group(self, group_id):
        """
        Get information about a group

        :type group_id: int
        :param group_id: Group ID Number

        :rtype: dict
        :return: a dictionary containing group information
        """
        res = self.post('loadGroups', {'groupId': group_id})
        if isinstance(res, list):
            return _fix_group(res[0])
        else:
            return _fix_group(res)

    def get_groups(self):
        """
        Get all the groups

        :rtype: list of dicts
        :return: list of a dictionaries containing group information
        """
        res = self.post('loadGroups', {})
        return [_fix_group(group) for group in res]

    def update_group(self, group_id, new_name):
        """
        Update the name of a group

        :type group_id: int
        :param group_id: group ID number

        :type new_name: str
        :param new_name: New name for the group

        :rtype: dict
        :return: a dictionary containing group information
        """
        data = {
            'id': group_id,
            'name': new_name,
        }
        try:
            response = self.post('updateGroup', data)
        except Exception:
            pass

        # Apollo returns a 404 here for some unholy reason, despite actually
        # renaming the group.
        response = self.post('loadGroups', {'groupId': group_id})[0]
        return _fix_group(response)

    def get_organism_permissions(self, group):
        """
        Get the group's organism permissions

        :type group: str
        :param group: group name

        :rtype: list
        :return: a list containing organism permissions (if any)
        """
        data = {
            'name': group,
        }
        response = _fix_group(self.post('getOrganismPermissionsForGroup', data))
        return response

    def update_organism_permissions(self, group, organism_name,
                                    administrate=False, write=False,
                                    read=False, export=False):
        """
        Update the group's permissions on an organism

        :type group: str
        :param group: group name

        :type organism_name: str
        :param organism_name: Organism name

        :type administrate: bool
        :param administrate: Should the group have administrate privileges

        :type read: bool
        :param read: Should the group have read privileges

        :type write: bool
        :param write: Should the group have write privileges

        :type export: bool
        :param export: Should the group have export privileges

        :rtype: list
        :return: list of group organism permissions
        """
        data = {
            'name': group,
            'organism': organism_name,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        response = self.post('updateOrganismPermission', data)
        response['permissions'] = json.loads(response['permissions'])
        return response

    def update_membership(self, group_id=None, users=[], memberships=[]):
        """
        Update the group's membership

        :type group_id: int
        :param group_id: Group ID Number

        :type users: list of str
        :param users: List of emails

        :type memberships: list
        :param memberships: Bulk memberships to update of the form: [ {groupId: <groupId>,users: ["user1", "user2", "user3"]}, {groupId:<another-groupId>, users: ["user2", "user8"]} (users and groupId will be ignored)

        :rtype: dict
        :return: dictionary of group information
        """

        if not group_id and not memberships:
            raise Exception("group_id+users or memberships is required")
        elif len(memberships) > 0:
            data = {
                'memberships': memberships
            }
        else:
            data = {
                'groupId': group_id,
                'users': users,
            }

        return _fix_group(self.post('updateMembership', data))

    def update_group_admin(self, group_id, users=[]):
        """
        Update the group's admins

        :type group_id: int
        :param group_id: Group ID Number

        :type users: list of str
        :param users: List of emails

        :rtype: dict
        :return: dictionary of group information
        """
        data = {
            'groupId': group_id,
            'users': users,
        }
        return _fix_group(self.post('updateGroupAdmin', data))

    def get_group_admin(self, group):
        """
        Get the group's admins

        :type group: str
        :param group: group name

        :rtype: list
        :return: a list containing group admins
        """
        data = {
            'name': group,
        }
        response = _fix_group(self.post('getGroupAdmin', data))
        return response

    def get_group_creator(self, group):
        """
        Get the group's creator

        :type group: str
        :param group: group name

        :rtype: list
        :return: creator userId
        """
        data = {
            'name': group,
        }
        response = _fix_group(self.post('getGroupCreator', data))
        return response
