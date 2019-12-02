from app.main import db
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()

        response_object = {'status': True, 'message': 'Successfully logged out!'}
        return response_object, 200
    except Exception as e:
        response_object = {'status': False, 'message': e}
        return response_object, 200
