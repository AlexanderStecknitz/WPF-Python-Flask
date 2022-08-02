from flask import Flask

from rest.kunde_get_controller import kunde_getcontroller
from container import Container


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)
    app.container = container
    app.register_blueprint(kunde_getcontroller)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
