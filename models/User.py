from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    user_id = db.Column(db.String(25), primary_key=True)
    user_name = db.Column(db.String(25))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    group_id = db.Column(db.String(25), db.ForeignKey("group.gorup_id"))

if __name__ == "__main__":
    print(User.user_id)
    
    