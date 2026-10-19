import os
from dotenv import load_dotenv
from flask import Flask
from .routes.planet_routes import planets_bp
from .db import db, migrate
from .models import planet

load_dotenv()


def create_app(config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI'
    )

    if config:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            'SQLALCHEMY_TEST_DATABASE_URI'
        )

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(planets_bp)
    return app
