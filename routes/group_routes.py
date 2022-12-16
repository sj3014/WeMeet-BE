from flask import Blueprint
from controllers.group_controller import *

group_routes = Blueprint('group_routes', __name__)

group_routes.route('/', methods=['POST'])(create_group)
group_routes.route('/list', methods=['GET'])(get_groups)
group_routes.route('/<group_id>', methods=['PUT'])(update_group)
group_routes.route('/<group_id>', methods=['DELETE'])(delete_group)
