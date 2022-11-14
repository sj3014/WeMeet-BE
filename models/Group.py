from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Group(db.Model):
    __tablename__ = 'group'

    group_id = db.Column(db.String(25), primary_key=True)
    group_name = db.Column(db.String(25))

if __name__ == "__main__":
    pass