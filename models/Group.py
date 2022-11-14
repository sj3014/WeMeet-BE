from models.database import db
import uuid


class Group(db.Model):
    __tablename__ = 'group'

    uuid = db.Column(db.String(36),
                     default=lambda: str(uuid.uuid4()), primary_key=True)
    group_name = db.Column(db.String(25))


if __name__ == "__main__":
    pass
