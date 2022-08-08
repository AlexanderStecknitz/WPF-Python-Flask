from flask import Flask

from rest.kunde_get_controller import kunde_getcontroller
from container import Container
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] [%(levelname)s] %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)
    app.container = container
    app.register_blueprint(kunde_getcontroller)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
