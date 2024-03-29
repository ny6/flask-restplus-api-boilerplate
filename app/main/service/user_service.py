import uuid
import datetime

from app.main import db
from app.main.model.user import User


def register_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        response_object = {'status': False, 'message': 'User already exists!'}
        return response_object, 409

    new_user = User(public_id=str(uuid.uuid4()),
                    email=data['email'],
                    username=data['username'],
                    password=data['password'],
                    created_at=datetime.datetime.utcnow(),
                    updated_at=datetime.datetime.utcnow())
    save_changes(new_user)

    return generate_token(new_user)


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': True,
            'message': 'Successfully registered!',
            'Authorization': auth_token.decode(),
        }
        return response_object, 201
    except Exception as e:
        response_object = {'status': False, 'message': 'Something went wrong!'}
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
