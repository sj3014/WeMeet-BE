from flask import Blueprint
from controllers.schedule_controller import *
from flask_cors import CORS

schedule_routes = Blueprint('schedule_routes', __name__)
CORS(schedule_routes)

schedule_routes.route('/', methods=['GET'])(get_schedule)
schedule_routes.route('/', methods=['POST'])(create_schedule)
schedule_routes.route('/<schedule_id>', methods=['PUT'])(update_schedule)
schedule_routes.route('/<schedule_id>', methods=['DELETE'])(delete_schedule)
schedule_routes.route('/group/<group_id>', methods=['GET'])(get_group_schedule)
