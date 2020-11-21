"""
Configuration module for pytest.

Define test fixtures that create and configure an instance of the app and
initialize a new database for testing.
"""

import pytest

from scorecard import create_app, db


@pytest.fixture(scope="session")
def test_client():
    # Create a new app using the testing configuration
    app = create_app("scorecard.config.TestConfig")

    # Create a test client using the Werkzeug test client exposed by Flask
    client = app.test_client()
    # Establish an application context before running the tests
    ctx = app.app_context()
    ctx.push()

    # Run the tests using this fixture with the testing client
    yield client

    # Pop the context to clean up the test environment
    ctx.pop()


@pytest.fixture(scope="session")
def init_db(test_client):
    # Create the database and all the database tables
    db.create_all()
    # Run the tests using this fixture
    yield
    # Destroy the database to clean up the test environment
    db.drop_all()


@pytest.fixture
def rollback_db(init_db):
    # Run the tests using this fixture
    yield
    # Rollback all the changes to the database
    db.session.rollback()
