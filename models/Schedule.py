from models.database import db
from datetime import datetime
import uuid


class Schedule(db.Model):
    __tablename__ = 'schedule'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    schedule_name = db.Column(db.String(100))
    start_time = db.Column(db.DateTime, default=datetime.now())
    end_time = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(500))
    all_day = db.Column(db.Boolean, default=False)
    recurrence_rule = db.Column(db.String(200))
    meta_data = db.Column(db.String(200))
    user_id = db.Column(db.String(36), db.ForeignKey('user.uuid'))


    def __repr__(self):
        return '<Schedule {}>'.format(self.schedule_name)

    def __init__(self, schedule_name, start_time, end_time, description, all_day, recurrence_rule, meta_data, user_id):
        self.schedule_name = schedule_name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.all_day = all_day
        self.recurrence_rule = recurrence_rule
        self.meta_data = meta_data
        self.user_id = user_id

    def public_info(self):
        return {'schedule_name': self.schedule_name, 'start_time': self.start_time, 'end_time': self.end_time, 'description': self.description}

