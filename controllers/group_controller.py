from flask import request, make_response
from models.database import db
from models.Group import Group
from models.User import User
import json
from middleware import login_required


@login_required
def create_group(user: User):
    req = request.get_data()
    # req = request.get_json()
    req = json.loads(req)

    group = Group(req['group_name'])
    user.groups.append(group)
    db.session.add(group)
    db.session.commit()

    return make_response('Success', 200)

# @login_required
# def add_to_group(user: User, group_id: str):
#     req = request.get_data()
#     req = json.loads(req)
#
#     new_user = req['new_user_id']
#
#     group = Group.query.join(User, Group.users).filter(
#         User.uuid == user.uuid, Group.uuid == group_id).first()
#
#     if group is None:
#         return make_response('Either the group does not exist or the user does not belong to the group', 400)
#
#     user.groups.append(new_user)
#     db.session.add(group)
#     db.session.commit()
#
#     return make_response('Success', 200)


@login_required
def add_to_group(user: User, group_id: str):
    req = request.get_data()
    req = json.loads(req)

    new_user = req['userId']

    group = Group.query.filter_by(uuid=group_id).first()

    if not group:
        return make_response('Either the group does not exist or the user does not belong to the group', 400)

    new_user = User.query.filter_by(uuid=req['userId']).first()

    if new_user is None:
        return make_response('User does not exist', 400)

    new_user.groups.append(group)
    db.session.add(new_user)
    db.session.commit()

    return make_response('Success', 200)


@login_required
def get_groups(user: User):
    user_groups = User.query.join(
        Group, User.groups).filter(User.uuid == user.uuid).all()

    user_groups = [user_group.deserialize_groups()
                   for user_group in user_groups]

    return make_response(user_groups, 200)

@login_required
def get_group(user: User, group_id: str):
    # Find the group with the given group id
    group = Group.query.join(User, Group.users).filter(
        User.uuid == user.uuid, Group.uuid == group_id).first()

    # Get the list of members in the group
    users = User.query.join(User, Group.users).filter(
        Group.uuid == group_id).all()

    print(users)

    if not group:
        return make_response('Group not found', 404)

    if user not in users:
        return make_response('Forbidden: Group Access Denied', 403)

    # Return the group information
    return make_response({
        'group_name': group.group_name,
        'users': [{'email': user.email,
                   'user_name': user.username,
                   'first_name': user.first_name,
                   'last_name': user.last_name} for user in users]
    }, 200)


@login_required
def get_group(user: User, group_id: str):
    # Find the group with the given group id
    group = Group.query.join(User, Group.users).filter(
        User.uuid == user.uuid, Group.uuid == group_id).first()

    # Get the list of members in the group
    users = User.query.join(User, Group.users).filter(
        Group.uuid == group_id).all()

    print(users)

    if not group:
        return make_response('Group not found', 404)

    if user not in users:
        return make_response('Forbidden: Group Access Denied', 403)

    # Return the group information
    return make_response({
        'group_name': group.group_name,
        'users': [{'email': user.email,
                   'user_name': user.username,
                   'first_name': user.first_name,
                   'last_name': user.last_name} for user in users]
    }, 200)


@login_required
def update_group(user: User, group_id: str):
    req = request.get_json()
    group = Group.query.join(User, Group.users).filter(
        User.uuid == user.uuid, Group.uuid == group_id).first()

    if group is None:
        return make_response('Either the group does not exist or the user does not belong to the group', 400)

    if 'group_name' in req:
        group.group_name = req['group_name']

    db.session.add(group)
    db.session.commit()

    return make_response('Success', 200)


@login_required
def delete_group(user: User, group_id: str):
    group = Group.query.join(User, Group.users).filter(
        User.uuid == user.uuid, Group.uuid == group_id).first()

    if group is None:
        return make_response('Either the group does not exist or the user does not belong to the group', 400)

    db.session.delete(group)
    db.session.commit()

    return make_response('Success', 200)
