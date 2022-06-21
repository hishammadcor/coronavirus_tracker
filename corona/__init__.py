#__init__.py file for maintaining the blue print.
from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = "hishammadcor"

    from . import corona_virues

    app.register_blueprint(corona_virues.bp)

    return app
