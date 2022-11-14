from flask import Blueprint
from controllers.UserController import signup

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/signup', methods=['POST'])(signup)
