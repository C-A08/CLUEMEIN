from flask import Flask
from website.views import viewss


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config['SECRET_KEY'] = "Testing"

    app.register_blueprint(viewss)

    return app
