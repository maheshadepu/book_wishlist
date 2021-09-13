import pytest
from flask_sqlalchemy import SQLAlchemy
from flaskapp.app import TestConfig, create_app
from sqlalchemy.sql import text

# initialize extensions below here

@pytest.fixture(scope="session")
def app():
    app = create_app(config_object=TestConfig)

    db = SQLAlchemy(app)
    file = open("./tests/integration/init_test_db.sql")
    query = text(file.read())
    db.session.execute(query)
    db.session.commit()

    with app.app_context():
        yield app
    clean_up(db)
    db.session.commit()

def clean_up(db):
    db.session.execute("delete from wish_list where user_id in (2,3)")
    db.session.execute("delete from book where isbn like '45%'")
    db.session.execute("delete from wl_user where first_name like 'TestUser%'")


@pytest.fixture
def flask_client(app):

    with app.test_client(use_cookies=False) as client:
        yield client
