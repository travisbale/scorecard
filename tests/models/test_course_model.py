"""Test the Course model and schema."""

import pytest
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from scorecard.models.course import Course, CourseSchema


class TestCourse:
    @pytest.fixture
    def course(self):
        return Course("course name")

    def test_create_new_course(self, course):
        assert course.name == "course name"

    def test_course_schema_dump(self, course, rollback_db):
        course_dict = CourseSchema().dump(course.save())
        assert course_dict["id"] == course.id
        assert course_dict["name"] == course.name

    def test_saving_course_with_duplicate_name_raises_sqlalchemy_integrity_error(self, course, rollback_db):
        course.save()
        course = Course("course name")

        with pytest.raises(IntegrityError):
            course.save()


class TestCourseSchema:
    @pytest.fixture(scope="class")
    def schema(self):
        return CourseSchema()

    def test_load_course_returns_course_instance(self, schema):
        course = schema.load(dict(name="course name"))
        assert isinstance(course, Course)

    def test_load_course_raises_validation_error_if_dictionary_has_no_name_property(self, schema):
        with pytest.raises(ValidationError):
            schema.load(dict())
