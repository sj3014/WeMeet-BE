from models.database import db
import uuid


class Group(db.Model):
    __tablename__ = 'group'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    group_name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return '<Group {}>'.format(self.group_name)

    def __init__(self, group_name):
        self.group_name = group_name

    def deserialize(self):
        return {"group_id": self.uuid, "group_name": self.group_name}
