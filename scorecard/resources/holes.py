"""Holes module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView

from scorecard.models.course import Course
from scorecard.models.hole import Hole, HoleSchema
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet

schema = HoleSchema()


class HolesResource(MethodView):
    """Dispatches request methods to retrieve or create roles."""

    def get(self, course_id, tee_color_id):
        """Return a list of all the tees on the course with the given tee color."""
        tee_set = TeeSet.query.get_or_404((course_id, tee_color_id), "The tees do not exist")
        return jsonify(schema.dump(tee_set.holes, many=True)), HTTPStatus.OK

    def post(self, course_id, tee_color_id):
        """Add new tees to the golf course with the given color."""
        Course.query.get_or_404(course_id, "The course does not exist")
        TeeColor.query.get_or_404(tee_color_id, "The tee color does not exist")

        holes = schema.load(request.get_json(), many=True)

        for hole in holes:
            hole.course_id = course_id
            hole.tee_color_id = tee_color_id
            hole.merge()

        return jsonify(message="The tees have been added to the tee set"), HTTPStatus.CREATED


class HoleResource(MethodView):
    """Dispatches request methods to retrieve or delete an existing tee."""

    def get(self, course_id, tee_color_id, number):
        """Return the tee with the given color and hole number from the golf course."""
        hole = Hole.query.get_or_404((course_id, tee_color_id, number), "The hole does not exist")
        return jsonify(schema.dump(hole)), HTTPStatus.OK

    def delete(self, course_id, tee_color_id, number):
        """Delete the tee with the given color and hole number from the golf course."""
        hole = Hole.query.get_or_404((course_id, tee_color_id, number), "The hole does not exist")
        hole.delete()
        return jsonify(message="The tee has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule(
        "/courses/<int:course_id>/tees/<int:tee_color_id>/holes", view_func=HolesResource.as_view("holes_resource")
    )
    bp.add_url_rule(
        "/courses/<int:course_id>/tees/<int:tee_color_id>/holes/<int:number>",
        view_func=HoleResource.as_view("hole_resource"),
    )
