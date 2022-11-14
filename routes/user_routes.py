from flask import Blueprint
from controllers.user_controller import signup, login

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/signup', methods=['POST'])(signup)
user_routes.route('/login', methods=['POST'])(login)
