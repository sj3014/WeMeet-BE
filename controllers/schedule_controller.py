from flask import request, make_response
import jwt
from models.Schedule import Schedule
from models.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json
from middleware import login_required
import config


def list_schedules():
    schedules = [schedule.public_info() for schedule in Schedule.query.all()]

    return make_response(schedules, 200)


def create_schedule():
    req = request.get_data()
    # req = request.get_json()
    req = json.loads(req)
    print(req)
    schedule_name = req['schedule_name']
    start_time = req['start_time']
    end_time = req['end_time']
    description = req['description']

    user_id = "7e1c6019-2f94-4281-938a-82c89eb28cb6"

    schedule_exist = Schedule.query.filter_by(schedule_name=schedule_name).first()

    if schedule_exist:
        return make_response('Schedule already exists', 400)

    new_schedule = Schedule(schedule_name, start_time, end_time, description, user_id)
    db.session.add(new_schedule)
    db.session.commit()

    return make_response('Success', 200)