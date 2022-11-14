from flask import request, jsonify, make_response
import jwt
from functools import wraps
from models.User import User
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json


def signup():
    req = request.get_data()
    req = json.loads(req)

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
    req = request.get_json()

    email = req['email']
    password = req['password']

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return make_response('Please enter a correct email and password', 400)

    token = jwt.encode(
        {'uuid': user.uuid, 'exp': datetime.utcnow() + timedelta(days=1)})

    return make_response(jsonify({'token': token.decode('UTF-8')}), 200)

# middleware for verifying the JWT


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 400

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(uuid=data['uuid']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 400

        # TODO: Check expiry
        # if data['exp'] > datetime.utcnow()

        return f(user, *args, **kwargs)

    return decorated
