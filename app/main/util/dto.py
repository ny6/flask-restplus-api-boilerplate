from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description="User email address"),
        'username': fields.String(required=True, description="User username"),
        'password': fields.String(required=True, description="User password"),
        # 'public_id': fields.String(description="User Identifier"),
    })
