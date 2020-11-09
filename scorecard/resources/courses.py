"""Courses module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict

from scorecard.models.course import Course, CourseSchema

from .view_decorators import permission_required

schema = CourseSchema()


class CoursesResource(MethodView):
    """Dispatches request methdos to retrieve or create courses."""

    def get(self):
        """Return a list of all the courses."""
        return jsonify(schema.dump(Course.query.all(), many=True)), HTTPStatus.OK

    @permission_required("create:courses")
    def post(self):
        """Create a new course."""
        course = schema.load(request.get_json())

        if Course.query.filter_by(name=course.name).count() > 0:
            raise Conflict(description="The course already exists")

        course.save()
        return jsonify(schema.dump(course)), HTTPStatus.CREATED


class CourseResource(MethodView):
    """Dispatches request methods to retrieve, delete, or modify an existing course."""

    def get(self, id):
        """Return the course with the given ID."""
        course = Course.query.get_or_404(id, "The course does not exist")
        return jsonify(schema.dump(course)), HTTPStatus.OK

    @permission_required("delete:courses")
    def delete(self, id):
        """Delete the course with the given ID."""
        course = Course.query.get_or_404(id, "The course does not exist")
        course.delete()
        return jsonify(message="The course has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/courses", view_func=CoursesResource.as_view("courses_resource"))
    bp.add_url_rule("/courses/<int:id>", view_func=CourseResource.as_view("course_resource"))
