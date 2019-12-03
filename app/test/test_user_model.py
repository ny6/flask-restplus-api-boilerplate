import unittest
import datetime

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    @staticmethod
    def save_user_to_db_and_get_token():
        user = User(email='test@test.com',
                    password='password',
                    created_at=datetime.datetime.utcnow(),
                    updated_at=datetime.datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        return auth_token

    def test_encode_auth_token(self):
        auth_token = self.save_user_to_db_and_get_token()
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        auth_token = self.save_user_to_db_and_get_token()
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()
