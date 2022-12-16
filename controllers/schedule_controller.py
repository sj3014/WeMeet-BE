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


@login_required
def get_schedule(user: User):
    schedules = Schedule.query.filter_by(user_id=user.uuid).all()
    if schedules:
        schedules_list = [{
            'schedule_name': schedule.schedule_name,
            'start_time': schedule.start_time,
            'end_time': schedule.end_time,
            'description': schedule.description
        } for schedule in schedules]
        return make_response(schedules_list, 200)
    else:
        return make_response('No schedules found', 404)

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

@login_required
def delete_schedule(user: User, schedule_id: str):
    req = request.get_data()

    schedule = Schedule.query.filter_by(uuid=schedule_id, user_id=user.uuid).first()
    if schedule:
        db.session.delete(schedule)
        db.session.commit()
        return make_response('Success', 200)
    else:
        return make_response('Schedule not found', 404)

@login_required
def update_schedule(user: User, schedule_id: str):
    req = request.get_data()
    req = json.loads(req)
    start_time = req['start_time']
    end_time = req['end_time']
    description = req['description']

    schedule = Schedule.query.filter_by(uuid=schedule_id, user_id=user.uuid).first()
    if schedule:
        schedule.start_time = start_time
        schedule.end_time = end_time
        schedule.description = description
        db.session.commit()
        return make_response('Success', 200)
    else:
        return make_response('Schedule not found', 404)