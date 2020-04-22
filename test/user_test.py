import time

from . import ApolloTestCase, wa


class UserTest(ApolloTestCase):

    def test_get_users(self):

        users = wa.users.get_users()

        # We at least have admin + junior + temp from setup
        assert len(users) >= 3

        first_user = users[0]

        assert 'firstName' in first_user
        assert 'lastName' in first_user
        assert 'inactive' in first_user
        assert 'role' in first_user
        assert 'availableGroups' in first_user
        assert 'userCount' in first_user
        assert 'searchName' in first_user
        assert 'groups' in first_user
        assert 'userId' in first_user
        assert 'organismPermissions' in first_user
        assert 'username' in first_user

    def test_show_user(self):

        users = wa.users.get_users()

        user_id = users[0]['userId']

        user_info = wa.users.show_user(user_id)

        # userCount changes depending on what was requested to Apollo
        del user_info['userCount']
        del users[0]['userCount']

        assert user_info == users[0]

    def test_create_user(self):

        meta = {"bla": "bli"}
        res = wa.users.create_user("trash@bx.psu.edu", 'Poutrelle', 'Lapinou', 'superpassword', role="user", metadata=meta)
        self.waitUserCreated(res['userId'])

        res = wa.users.show_user('trash@bx.psu.edu')

        assert res['username'] == 'trash@bx.psu.edu'
        assert res['firstName'] == 'Poutrelle'
        assert res['lastName'] == 'Lapinou'
        assert res['role'] == 'USER'

    def test_delete_user(self):

        user_info = wa.users.create_user("trash@bx.psu.edu", 'Tempxx', 'oraryxx', 'coolpasswordxx', role="user")
        self.waitUserCreated(user_info['userId'])

        wa.users.delete_user(user_info['username'])
        self.waitUserDeleted(user_info['userId'])

        users = wa.users.get_users()

        for user in users:
            assert user['username'] != 'trash@bx.psu.edu'

    def test_update_user(self):

        user_info = wa.users.create_user("trash@bx.psu.edu", 'Tempxx', 'oraryxx', 'coolpasswordxx', role="user")
        self.waitUserCreated(user_info['userId'])

        wa.users.update_user(user_info['username'], 'firstname2', 'lastname2')

        time.sleep(3)
        res = wa.users.show_user('trash@bx.psu.edu')

        assert res['username'] == 'trash@bx.psu.edu'
        assert res['firstName'] == 'firstname2'
        assert res['lastName'] == 'lastname2'
        assert res['role'] == 'USER'

    def test_update_user_email(self):

        user_info = wa.users.create_user("trash@bx.psu.edu", 'Tempxx', 'oraryxx', 'coolpasswordxx', role="user")
        self.waitUserCreated(user_info['userId'])

        wa.users.update_user(user_info['username'], 'firstname2', 'lastname2', new_email='updated@bx.psu.edu')

        time.sleep(3)
        res = wa.users.show_user('updated@bx.psu.edu')

        assert res['username'] == 'updated@bx.psu.edu'
        assert res['firstName'] == 'firstname2'
        assert res['lastName'] == 'lastname2'
        assert res['role'] == 'USER'

    def setUp(self):
        # Make sure the user is not already there
        temp_user_info = wa.users.show_user('test_temp@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        temp_user_info = wa.users.show_user('trash@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        temp_user_info = wa.users.show_user('updated@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        wa.users.create_user("test_temp@bx.psu.edu", 'Temp', 'orary', 'coolpassword', role="user")

    def tearDown(self):
        temp_user_info = wa.users.show_user('test_temp@bx.psu.edu')
        if temp_user_info and 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        temp_user_info = wa.users.show_user('trash@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])

        temp_user_info = wa.users.show_user('updated@bx.psu.edu')
        if 'username' in temp_user_info:
            wa.users.delete_user(temp_user_info['username'])
            self.waitUserDeleted(temp_user_info['userId'])
