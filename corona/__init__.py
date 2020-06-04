from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = "rocdammahsih"

    from . import corona_virues

    app.register_blueprint(corona_virues.bp)

    return app
