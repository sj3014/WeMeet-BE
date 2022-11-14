from models.database import db
import uuid

user_group = db.Table('user_group', db.Column('user_id', db.String(36), db.ForeignKey(
    'user.uuid')), db.Column('group_id', db.String(36), db.ForeignKey('group.uuid')))


class User(db.Model):

    __tablename__ = 'user'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    user_name = db.Column(db.String(25))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    schedules = db.relationship('Schedule', backref='user')
    groups = db.relationship('Group', secondary=user_group, backref='users')
