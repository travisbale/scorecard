"""
Configuration module for pytest.

Define test fixtures that create and configure an instance of the app and
initialize a new database for testing.
"""

from datetime import datetime

import pytest

from scorecard import create_app, db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet
from scorecard.models.tournament import Tournament


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


@pytest.fixture(scope="session")
def pebble_beach(init_db):
    course = Course("Pebble Beach").save()
    tee_colors = {
        "White": TeeColor("White").save(),
        "Gold": TeeColor("Gold").save(),
        "Blue": TeeColor("Blue").save(),
    }

    TeeSet(tee_colors["White"].id, 132, 71.3, course.id).save()
    TeeSet(tee_colors["Gold"].id, 136, 72.6, course.id).save()
    TeeSet(tee_colors["Blue"].id, 143, 74.7, course.id).save()

    Hole(1, 4, 8, 332, course.id, tee_colors["White"].id).save()
    Hole(2, 5, 10, 428, course.id, tee_colors["White"].id).save()
    Hole(3, 4, 12, 334, course.id, tee_colors["White"].id).save()
    Hole(4, 4, 16, 295, course.id, tee_colors["White"].id).save()
    Hole(5, 3, 14, 130, course.id, tee_colors["White"].id).save()
    Hole(6, 5, 2, 467, course.id, tee_colors["White"].id).save()
    Hole(7, 3, 18, 94, course.id, tee_colors["White"].id).save()
    Hole(8, 4, 6, 373, course.id, tee_colors["White"].id).save()
    Hole(9, 4, 4, 435, course.id, tee_colors["White"].id).save()
    Hole(10, 4, 7, 409, course.id, tee_colors["White"].id).save()
    Hole(11, 4, 5, 340, course.id, tee_colors["White"].id).save()
    Hole(12, 3, 17, 179, course.id, tee_colors["White"].id).save()
    Hole(13, 4, 9, 372, course.id, tee_colors["White"].id).save()
    Hole(14, 5, 1, 548, course.id, tee_colors["White"].id).save()
    Hole(15, 4, 13, 340, course.id, tee_colors["White"].id).save()
    Hole(16, 4, 11, 368, course.id, tee_colors["White"].id).save()
    Hole(17, 3, 15, 163, course.id, tee_colors["White"].id).save()
    Hole(18, 5, 3, 509, course.id, tee_colors["White"].id).save()

    Hole(1, 4, 8, 346, course.id, tee_colors["Gold"].id).save()
    Hole(2, 5, 10, 460, course.id, tee_colors["Gold"].id).save()
    Hole(3, 4, 12, 374, course.id, tee_colors["Gold"].id).save()
    Hole(4, 4, 16, 307, course.id, tee_colors["Gold"].id).save()
    Hole(5, 3, 14, 142, course.id, tee_colors["Gold"].id).save()
    Hole(6, 5, 2, 496, course.id, tee_colors["Gold"].id).save()
    Hole(7, 3, 18, 98, course.id, tee_colors["Gold"].id).save()
    Hole(8, 4, 6, 400, course.id, tee_colors["Gold"].id).save()
    Hole(9, 4, 4, 460, course.id, tee_colors["Gold"].id).save()
    Hole(10, 4, 7, 429, course.id, tee_colors["Gold"].id).save()
    Hole(11, 4, 5, 349, course.id, tee_colors["Gold"].id).save()
    Hole(12, 3, 17, 187, course.id, tee_colors["Gold"].id).save()
    Hole(13, 4, 9, 391, course.id, tee_colors["Gold"].id).save()
    Hole(14, 5, 1, 560, course.id, tee_colors["Gold"].id).save()
    Hole(15, 4, 13, 377, course.id, tee_colors["Gold"].id).save()
    Hole(16, 4, 11, 376, course.id, tee_colors["Gold"].id).save()
    Hole(17, 3, 15, 170, course.id, tee_colors["Gold"].id).save()
    Hole(18, 5, 3, 532, course.id, tee_colors["Gold"].id).save()

    Hole(1, 4, 8, 377, course.id, tee_colors["Blue"].id).save()
    Hole(2, 5, 10, 511, course.id, tee_colors["Blue"].id).save()
    Hole(3, 4, 12, 390, course.id, tee_colors["Blue"].id).save()
    Hole(4, 4, 16, 326, course.id, tee_colors["Blue"].id).save()
    Hole(5, 3, 14, 192, course.id, tee_colors["Blue"].id).save()
    Hole(6, 5, 2, 506, course.id, tee_colors["Blue"].id).save()
    Hole(7, 3, 18, 106, course.id, tee_colors["Blue"].id).save()
    Hole(8, 4, 6, 427, course.id, tee_colors["Blue"].id).save()
    Hole(9, 4, 4, 481, course.id, tee_colors["Blue"].id).save()
    Hole(10, 4, 7, 446, course.id, tee_colors["Blue"].id).save()
    Hole(11, 4, 5, 373, course.id, tee_colors["Blue"].id).save()
    Hole(12, 3, 17, 201, course.id, tee_colors["Blue"].id).save()
    Hole(13, 4, 9, 403, course.id, tee_colors["Blue"].id).save()
    Hole(14, 5, 1, 572, course.id, tee_colors["Blue"].id).save()
    Hole(15, 4, 13, 396, course.id, tee_colors["Blue"].id).save()
    Hole(16, 4, 11, 401, course.id, tee_colors["Blue"].id).save()
    Hole(17, 3, 15, 177, course.id, tee_colors["Blue"].id).save()
    Hole(18, 5, 3, 543, course.id, tee_colors["Blue"].id).save()

    # Commit the course so data isn't rolled back between tests
    db.session.commit()

    return course


@pytest.fixture(scope="session")
def pga_championship(init_db):
    return Tournament("PGA Championship", datetime(2021, 6, 17), datetime(2021, 6, 21))


@pytest.fixture
def rollback_db(init_db):
    # Run the tests using this fixture
    yield
    # Rollback all the changes to the database
    db.session.rollback()
