from models.database import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(25))
    user_name = db.Column(db.String(25))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    group_id = db.Column(db.String(25))