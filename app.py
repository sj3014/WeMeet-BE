from flask import Flask
from routes.user_bp import user_bp
from models.database import db
from models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        app.register_blueprint(user_bp, url_prefix='/users')
        db.create_all()

        return app