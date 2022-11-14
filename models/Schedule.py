from models.database import db
from datetime import datetime
import uuid


class Schedule(db.Model):
    __tablename__ = 'schedule'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    schedule_name = db.Column(db.String(25))
    start_time = db.Column(db.DateTime, default=datetime.now())
    end_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.String(36), db.ForeignKey('user.uuid'))


if __name__ == "__main__":
    print(Schedule.schedule_id)
