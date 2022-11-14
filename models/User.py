from models.database import db
import uuid

user_group = db.Table('user_group', db.Column('user_id', db.String(36), db.ForeignKey(
    'user.uuid')), db.Column('group_id', db.String(36), db.ForeignKey('group.uuid')))


class User(db.Model):

    __tablename__ = 'user'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    schedules = db.relationship('Schedule', backref='user')
    groups = db.relationship('Group', secondary=user_group, backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.user)

    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
