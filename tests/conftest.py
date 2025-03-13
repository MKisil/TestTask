import pytest
from app import create_app, db
from app.users.models import User


@pytest.fixture
def app():
    app = create_app('testing')

    with app.app_context():
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def init_database(app):
    with app.app_context():
        user1 = User(name="Test User 1", email="test1@example.com")
        user2 = User(name="Test User 2", email="test2@example.com")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        yield
