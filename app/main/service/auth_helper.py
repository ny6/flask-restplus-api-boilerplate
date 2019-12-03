from app.main.model.user import User
from ..service.blacklist_service import save_token


class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': True,
                        'message': 'Login successfully!',
                        'Authorization': auth_token.decode(),
                    }
                    return response_object, 200

            response_object = {'status': False, 'message': 'Invalid credentials!'}
            return response_object, 401
        except Exception as e:
            response_object = {'status': False, 'message': 'Something went wrong!'}
            return response_object, 500

    @staticmethod
    def logout_user(data):
        auth_token = None
        if data:
            auth_token = data.split(' ')[1]

        if not auth_token:
            response_object = {'status': False, 'message': 'Invalid auth token!'}
            return response_object, 403

        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            return save_token(token=auth_token)

        response_object = {'status': False, 'message': resp}
        return response_object, 401
