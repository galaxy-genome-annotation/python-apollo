import time

from . import ApolloTestCase, wa


class GroupTest(ApolloTestCase):

    def test_get_groups(self):

        groups = wa.groups.get_groups()

        # We at least have the 2 from bootstrap + the one from setup
        assert len(groups) >= 3

        first_group = groups[0]

        assert 'public' in first_group
        assert 'numberOfUsers' in first_group
        assert 'name' in first_group
        assert 'admin' in first_group
        assert 'id' in first_group
        assert 'organismPermissions' in first_group
        assert 'users' in first_group

    def test_show_group(self):

        groups = wa.groups.get_groups()

        group_id = groups[0]['id']

        group_info = wa.groups.show_group(group_id)

        assert group_info == groups[0]

    def test_get_group_by_name(self):

        all_groups = wa.groups.get_groups()

        good_group = None
        for g in all_groups:
            if g['name'] == 'temp_group':
                good_group = g

        assert good_group is not None

        group_by_name = wa.groups.get_groups(name='temp_group')

        assert len(group_by_name) == 1
        assert good_group == group_by_name[0]

    def test_get_group_creator(self):

        creator = wa.groups.get_group_creator('temp_group')

        user_info = wa.users.show_user(creator)

        assert user_info['username'] == "admin@local.host"

    def test_get_group_admin(self):

        creator = wa.groups.get_group_admin('temp_group')

        user_info = wa.users.show_user(creator)

        assert user_info['username'] == "admin@local.host"

    def test_create_group(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        assert res[0]['name'] == 'trash_group'
        assert res[0]['admin'][0]['email'] == 'admin@local.host'

    def test_delete_group(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        wa.groups.delete_group('trash_group')
        self.waitGroupDeleted('trash_group')

        groups = wa.groups.get_groups()

        for group in groups:
            assert group['name'] != 'trash_group'

    def test_update_group(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        wa.groups.update_group(res[0]['id'], 'trash_group_updated')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 0

        res = wa.groups.get_groups('trash_group_updated')

        assert len(res) == 1

    def test_update_group_admin(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        wa.groups.update_group_admin(res[0]['id'], ['test_temp@bx.psu.edu'])

        time.sleep(1)

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1
        assert res[0]['admin'][0]['email'] == 'test_temp@bx.psu.edu'

    def test_update_membership_username(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        wa.groups.update_membership(res[0]['id'], ['test_temp@bx.psu.edu'])

        time.sleep(1)

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        assert res[0]['users'][0]['email'] == 'test_temp@bx.psu.edu'

    def test_update_membership_dict(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')
        assert len(res) == 1

        wa.groups.update_membership(memberships=[{'groupId': res[0]['id'], 'users': ['test_temp@bx.psu.edu']}])

        time.sleep(1)

        res = wa.groups.get_groups('trash_group')

        assert len(res) == 1

        assert res[0]['users'][0]['email'] == 'test_temp@bx.psu.edu'

    def test_update_permissions(self):

        res = wa.groups.create_group("trash_group")
        self.waitGroupCreated('trash_group')

        res = wa.groups.get_groups('trash_group')
        assert len(res) == 1

        res = wa.groups.get_organism_permissions('trash_group')

        assert res == []

        res = wa.groups.update_organism_permissions('trash_group', 'test_organism', True, False, True, False)

        assert res['class'] == 'org.bbop.apollo.GroupOrganismPermission'
        assert res['permissions'] == ['ADMINISTRATE', 'READ']

        time.sleep(1)

        res = wa.groups.get_organism_permissions('trash_group')

        assert res[0]['class'] == 'org.bbop.apollo.GroupOrganismPermission'
        assert res[0]['permissions'] == ['ADMINISTRATE', 'READ']

    def setUp(self):
        # Make sure the group is not already there
        temp_group_info = wa.groups.get_groups('temp_group')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('temp_group')
            self.waitGroupDeleted('temp_group')

        temp_group_info = wa.groups.get_groups('trash_group')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('trash_group')
            self.waitGroupDeleted('trash_group')

        temp_group_info = wa.groups.get_groups('trash_group_updated')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('trash_group_updated')
            self.waitGroupDeleted('trash_group_updated')

        temp_user_info = wa.users.show_user('test_temp@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        wa.groups.create_group("temp_group")
        self.waitGroupCreated('temp_group')

        user_info = wa.users.create_user("test_temp@bx.psu.edu", 'Temp', 'orary', 'coolpassword', role="user")
        self.waitUserCreated(user_info['userId'])

    def tearDown(self):
        temp_group_info = wa.groups.get_groups('temp_group')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('temp_group')
            self.waitGroupDeleted('temp_group')

        temp_group_info = wa.groups.get_groups('trash_group')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('trash_group')
            self.waitGroupDeleted('trash_group')

        temp_group_info = wa.groups.get_groups('trash_group_updated')
        if temp_group_info and 'name' in temp_group_info[0]:
            wa.groups.delete_group('trash_group_updated')
            self.waitGroupDeleted('trash_group_updated')

        temp_user_info = wa.users.show_user('test_temp@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])
