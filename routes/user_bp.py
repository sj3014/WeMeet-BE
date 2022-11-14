from flask import Blueprint
from controllers.UserController import signup, login

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/signup', methods=['POST'])(signup)
user_bp.route('/login', methods=['POST'])(login)
