from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """ User Login Resource """

    @api.doc('User login')
    @api.expect(user_auth, validate=True)
    def post(self):
        return Auth.login_user(data=request.json)


@api.route('/logout')
class LogoutAPI(Resource):
    """ Logout Resource """

    @api.doc('Logout user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
