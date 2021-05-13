"""Teeing areas module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.course import Course
from scorecard.models.tee_set import TeeSet, TeeSetSchema
from scorecard.resources.view_decorators import permission_required

schema = TeeSetSchema()


class TeeSetsResource(MethodView):
    """Dispatches request methods to retrieve or create sets of teeing areas."""

    def get(self, course_id):
        """Return a list of all sets of teeing areas on a golf course."""
        course = Course.query.get_or_404(course_id, "The course does not exist")
        return jsonify(schema.dump(course.tee_sets, many=True)), HTTPStatus.OK

    @permission_required("create:tee_sets")
    def post(self, course_id):
        """Add new tee sets to a golf course."""
        Course.query.get_or_404(course_id, "The course does not exist")
        tee_sets = schema.load(request.get_json(), many=True)

        for tee_set in tee_sets:
            tee_set.course_id = course_id
            tee_set.merge()

        return jsonify(message="The tee sets have been added to the golf course"), HTTPStatus.CREATED

    @permission_required("delete:tee_sets")
    def delete(self, course_id):
        """Delete tee sets from a golf course."""
        course = Course.query.get_or_404(course_id, "The course does not exist")

        for tee_set in course.tee_sets:
            tee_set.delete()

        return jsonify(message="The tee sets have been deleted from the golf course"), HTTPStatus.OK


class TeeSetResource(MethodView):
    """Dispatches request methods to retrieve or delete a set of teeing areas."""

    def get(self, course_id, tee_color_id):
        """Return the set of tees with the given color from the given course."""
        tee_set = TeeSet.query.get_or_404((course_id, tee_color_id), "The tees do not exist")
        return jsonify(schema.dump(tee_set)), HTTPStatus.OK

    @permission_required("delete:tee_sets")
    def delete(self, course_id, tee_color_id):
        """Delete the set of tees with the given color from the given course."""
        tee_set = TeeSet.query.get_or_404((course_id, tee_color_id), "The tees do not exist")
        tee_set.delete()
        return jsonify(message="The tees have been deleted")


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/courses/<int:course_id>/tees", view_func=TeeSetsResource.as_view("tee_sets_resource"))
    bp.add_url_rule(
        "/courses/<int:course_id>/tees/<int:tee_color_id>", view_func=TeeSetResource.as_view("tee_set_resource")
    )
