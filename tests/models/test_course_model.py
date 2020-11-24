"""Test the Course model and schema."""

import pytest
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models.course import Course, CourseSchema


@pytest.fixture(scope="module")
def schema():
    return CourseSchema()


def test_create_new_course():
    course = Course("course name")
    assert course.name == "course name"


def test_course_schema_load_course_returns_course_instance(schema):
    course = schema.load(dict(name="course name"))
    assert isinstance(course, Course)


def test_course_schema_dump(schema, rollback_db):
    course = Course("name").save()
    dict = schema.dump(course)

    assert dict["id"] is not None and dict["id"] == course.id
    assert dict["name"] is not None and dict["name"] == course.name


def test_course_schema_load_course_raises_validation_error_if_dictionary_has_no_name_property(schema):
    with pytest.raises(ValidationError):
        schema.load(dict())


def test_saving_course_with_duplicate_name_raises_sqlalchemy_integrity_error(rollback_db):
    Course("course name").save()
    course = Course("course name")

    with pytest.raises(IntegrityError):
        course.save()
