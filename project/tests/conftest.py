# project/tests/conftest.py


import pytest

from project import create_app, db  # updated

from project.api.models import User #added for GET all routes

@pytest.fixture(scope='module')
def test_app():
    app = create_app()  # new
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()

#adding for GET all routes
@pytest.fixture(scope='function')
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user