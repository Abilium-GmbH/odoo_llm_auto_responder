import pytest
from flask_server.app import app, db


@pytest.fixture
def client():
    """
    Create a test client using the app fixture.
    """
    # Set up the test configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.sqlite'

    # Create the test database tables
    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client
