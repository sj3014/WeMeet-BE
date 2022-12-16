from flask import Blueprint
from controllers.schedule_controller import *

schedule_routes = Blueprint('schedule_routes', __name__)

schedule_routes.route('/', methods=['GET'])(list_schedules)
schedule_routes.route('/', methods=['POST'])(create_schedule)
schedule_routes.route('/<schedule_id>', methods=['PUT'])(update_schedule)
schedule_routes.route('/<schedule_id>', methods=['DELETE'])(delete_schedule)

