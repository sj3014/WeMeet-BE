from flask import request, make_response
import jwt
from models.User import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json
from middleware import login_required
import config


def signup():
    req = request.get_data()
    # req = request.get_json()
    req = json.loads(req)
    print(req)
    username = req['username']
    email = req['email']
    password = req['password']
    first_name = req['first_name']
    last_name = req['last_name']

    user_exist = User.query.filter_by(email=email).first()

    if user_exist:
        return make_response('User already exists', 400)

    new_user = User(username, email, generate_password_hash(
        password, method='sha256'), first_name, last_name)
    db.session.add(new_user)
    db.session.commit()

    return make_response('Success', 200)


def login():
    req = request.get_data()
    req = json.loads(req)

    email = req['email']
    password = req['password']

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return make_response('Please enter a correct email and password', 400)

    token = jwt.encode(
        payload={'uuid': user.uuid, 'exp': datetime.utcnow() +
                 timedelta(days=1)},
        key=config.Config.SECRET_KEY, algorithm='HS256')

    return make_response({'token': token}, 200)


def get_users():
    users = [user.public_info() for user in User.query.all()]

    return make_response(users, 200)


@login_required
def update_user(user: User):
    req = request.get_json()

    if 'email' in req:
        user.email = req['email']
    if 'first_name' in req:
        user.first_name = req['first_name']

    if 'last_name' in req:
        user.last_name = req['last_name']

    if 'password' in req:
        user.password = generate_password_hash(req['password'])

    db.session.add(user)
    db.session.commit()

    return make_response('Success', 200)

@login_required
def info(user: User):
    return make_response({
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    }, 200)

@login_required
def delete_user(user: User):
    db.session.delete(user)
    db.session.commit()

    return make_response('Success', 200)
