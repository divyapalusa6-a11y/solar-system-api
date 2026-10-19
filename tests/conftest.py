from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
import pytest
from app.models.planet import Planet

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet = Planet(
        name="Foo",
        description="A test planet",
        year_length="1.0"
    )
    db.session.add(planet)
    db.session.commit()
    return planet

