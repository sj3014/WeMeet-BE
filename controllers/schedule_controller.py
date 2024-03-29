from flask import request, make_response
import jwt
from models.Schedule import Schedule
from models.database import db
from models.User import User
from models.Group import Group
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import json
from middleware import login_required
import config
from controllers.email_lambda import send_email_sns


@login_required
def get_schedule(user: User):
    schedules = Schedule.query.filter_by(user_id=user.uuid).all()
    if schedules:
        schedules_list = [{
            'schedule_name': schedule.schedule_name,
            'start_time': schedule.start_time,
            'end_time': schedule.end_time,
            'description': schedule.description,
            'all_day': schedule.all_day,
            'recurrence_rule': schedule.recurrence_rule,
            'meta_data': schedule.meta_data,
            'uuid': schedule.uuid
        } for schedule in schedules]
        return make_response(schedules_list, 200)
    else:
        return make_response([], 200)


@login_required
def get_group_schedule(user: User, group_id: str):
    users = User.query.join(User, Group.users).filter(
        Group.uuid == group_id).all()
    group_schedules = []

    for user in users:
        user_schedules = Schedule.query.filter_by(user_id=user.uuid).all()
        for schedule in user_schedules:
            group_schedules.append({
                'schedule_name': schedule.schedule_name,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'description': schedule.description,
                'all_day': schedule.all_day,
                'recurrence_rule': schedule.recurrence_rule,
                'meta_data': schedule.meta_data,
                'uuid': schedule.uuid
            }
            )
    return make_response(group_schedules, 200)


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
    all_day = req['all_day']
    recurrence_rule = req['recurrence_rule']
    meta_data = req['meta_data']

    user_id = user.uuid

    schedule_exist = Schedule.query.filter_by(
        schedule_name=schedule_name).first()

    if schedule_exist:
        return make_response('Schedule already exists', 400)

    new_schedule = Schedule(schedule_name, start_time, end_time,
                            description, all_day, recurrence_rule,  meta_data, user_id)
    db.session.add(new_schedule)
    db.session.commit()

    email_to = f"{user.email}"
    email_subject = "A new schedule has been created"
    email_body = f"{user.first_name} created a new schedule {schedule_name} between {start_time} and {end_time}"
    response = send_email_sns(email_to, email_subject, email_body)
    print(response)

    return make_response('Success', 200)


@login_required
def delete_schedule(user: User, schedule_id: str):
    req = request.get_data()

    schedule = Schedule.query.filter_by(
        uuid=schedule_id, user_id=user.uuid).first()
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
    all_day = req['all_day']
    recurrence_rule = req['recurrence_rule']
    meta_data = req['meta_data']

    schedule = Schedule.query.filter_by(
        uuid=schedule_id, user_id=user.uuid).first()
    if schedule:
        schedule.start_time = start_time
        schedule.end_time = end_time
        schedule.description = description
        schedule.all_day = all_day
        schedule.recurrence_rule = recurrence_rule
        schedule.meta_data = meta_data
        db.session.commit()
        return make_response('Success', 200)
    else:
        return make_response('Schedule not found', 404)
