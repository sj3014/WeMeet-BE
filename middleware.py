from flask import request, jsonify
import jwt
from functools import wraps
from models.User import User
from models.database import db
from datetime import datetime, timedelta
import config


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Token is missing'}), 400

        token = token.split()

        if len(token) != 2 or token[0] != 'Bearer':
            return jsonify({'message': 'Authorization form is invalid'}), 400

        try:
            data = jwt.decode(
                token[1], config.Config.SECRET_KEY, algorithms='HS256')
            user = User.query.filter_by(uuid=data['uuid']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 400

        # TODO: Check expiry
        # if data['exp'] > datetime.utcnow()

        return f(user, *args, **kwargs)

    return decorated
