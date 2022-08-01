from flask import Flask
from flaskr.rest.controller.get_controller import kunde_getcontroller
"""Hi"""
def create_app():
    app = Flask(__name__)
    app.register_blueprint(kunde_getcontroller)
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
