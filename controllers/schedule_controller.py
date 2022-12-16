from flask import request, make_response
import jwt
from models.Schedule import Schedule
from models.database import db
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json
from middleware import login_required
import config


def list_schedules():
    schedules = [schedule.public_info() for schedule in Schedule.query.all()]

    return make_response(schedules, 200)

@login_required
def create_schedule(user: User):
    req = request.get_data()
    # req = request.get_json()
    req = json.loads(req)
    print(req)
    schedule_name = req['schedule_name']
    start_time = req['start_time']
    end_time = req['end_time']
    description = req['description']

    user_id = user.uuid

    schedule_exist = Schedule.query.filter_by(schedule_name=schedule_name).first()

    if schedule_exist:
        return make_response('Schedule already exists', 400)

    new_schedule = Schedule(schedule_name, start_time, end_time, description, user_id)
    db.session.add(new_schedule)
    db.session.commit()

    return make_response('Success', 200)