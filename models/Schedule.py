from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Schedule(db.Model):
    __tablename__ = 'Schedule'

    schedule_id = db.Column(db.String(25), primary_key=True)
    schedule_name = db.Column(db.String(25))
    start_time = db.Column(db.DateTime, default=datetime.now())
    end_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.String(25), db.ForeignKey("user.user_id"))


if __name__ == "__main__":
    print(Schedule.schedule_id)

