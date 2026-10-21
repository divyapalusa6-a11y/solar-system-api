
import os
from dotenv import load_dotenv
from flask import Flask

# Import the existing routes blueprint.
from .routes.planet_routes import bp as planets_bp

# Import the database and migration extensions.
from .db import db, migrate

# Import both models so Flask-Migrate can discover their tables.
from .models import planet, moon

load_dotenv()


def create_app(config=None):
    app = Flask(__name__)

    # Disable unnecessary SQLAlchemy modification tracking.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Load the development database URL from the .env file.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI'
    )

    # Use the test database when a test configuration is provided.
    if config:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            'SQLALCHEMY_TEST_DATABASE_URI'
        )

    # Connect SQLAlchemy and Flask-Migrate to this application.
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the existing planets routes.
    app.register_blueprint(planets_bp)

    return app
