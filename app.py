from flask import Flask
from routes.user_routes import user_routes
# from routes.schedule_routes import schedule_routes
from routes.group_routes import group_routes
from models.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        app.register_blueprint(user_routes, url_prefix='/api/user')
        # app.register_blueprint(schedule_routes, url_prefix='/api/schedule')
        app.register_blueprint(group_routes, url_prefix='/api/group')

        from models import User, Group, Schedule
        db.create_all()

        return app
