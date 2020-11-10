"""Tee colors module."""

from http import HTTPStatus

from flask.json import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict

from scorecard.models.tee_color import TeeColor, TeeColorSchema

schema = TeeColorSchema()


class TeeColorsResource(MethodView):
    """Dispatches requests to retrieve or create tee colors."""

    def get(self):
        """Return a list of available tee colors for golf courses."""
        return jsonify(schema.dump(TeeColor.query.all(), many=True)), HTTPStatus.OK

    def post(self):
        """Create a new tee color."""
        tee_color = schema.load(request.get_json())

        if TeeColor.query.filter_by(color=tee_color.color).count() > 0:
            raise Conflict(description="The tee color already exists")

        tee_color.save()
        return jsonify(schema.dump(tee_color)), HTTPStatus.CREATED


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/tee-colors", view_func=TeeColorsResource.as_view("tee_colors_resource"))
