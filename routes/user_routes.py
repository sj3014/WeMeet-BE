from flask import Blueprint
from controllers.user_controller import *
from flask_cors import CORS

user_routes = Blueprint('user_routes', __name__)
CORS(user_routes)

user_routes.route('/signup', methods=['POST'])(signup)
user_routes.route('/login', methods=['POST'])(login)
user_routes.route('/list', methods=['GET'])(get_users)
user_routes.route('/info', methods=['GET'])(info)
user_routes.route('/profile', methods=['PUT'])(update_user)
user_routes.route('/profile', methods=['DELETE'])(delete_user)
