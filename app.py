from flask import Flask

from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == "__main__":
    app.run()