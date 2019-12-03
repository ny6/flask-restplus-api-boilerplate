import unittest
import json

from app.test.base import BaseTestCase

email = 'test@test.com'
pwd = 'password'
un = 'username'
c_t = 'application/json'


def register_user(self):
    return self.client.post('/user/', data=json.dumps(dict(email=email, username=un, password=pwd)), content_type=c_t)


def login_user(self):
    return self.client.post('/auth/login', data=json.dumps(dict(email=email, password=pwd)), content_type=c_t)


class TestAuthBlueprint(BaseTestCase):
    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            # valid token logout
            response = self.client.post('/auth/logout',
                                        headers=dict(
                                            Authorization=
                                            f"Bearer {json.loads(login_response.data.decode())['Authorization']}"
                                        )
                                        )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'])
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
