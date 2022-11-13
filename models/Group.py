import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

class Group(declarative_base()):
    __name__ = 'group'

    group_id = db.Column(db.String(25), primary_key=True)
    group_name = db.Column(db.String(25))

if __name__ == "__main__":
    print(
        Group.__table__
    )