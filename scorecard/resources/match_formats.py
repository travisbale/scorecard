"""Match formats module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict

from scorecard.models.match_format import MatchFormat, MatchFormatSchema

# Schema for match format serialization and deserialization
schema = MatchFormatSchema()


class MatchFormatsResource(MethodView):
    """Dispatches request methods to retrieve or create match formats."""

    def get(self):
        """Return a list of all the match formats."""
        return jsonify(schema.dump(MatchFormat.query.all(), many=True)), HTTPStatus.OK

    def post(self):
        """Create a new match format."""
        match_format = schema.load(request.get_json())

        if MatchFormat.query.filter_by(name=match_format.name).count() > 0:
            raise Conflict(description="The match format already exists")

        match_format.save()
        return jsonify(schema.dump(match_format)), HTTPStatus.CREATED


class MatchFormatResource(MethodView):
    """Dispatches request methods to retrieve, update, or delete match formats."""

    def get(self, id):
        """Return the match format with the given ID."""
        match_format = MatchFormat.query.get_or_404(id, "The match format does not exist")
        return jsonify(schema.dump(match_format)), HTTPStatus.OK

    def delete(self, id):
        """Delete the match format with the given ID."""
        match_format = MatchFormat.query.get_or_404(id, "The match format does not exist")
        match_format.delete()
        return jsonify(message="The match format has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/match-formats", view_func=MatchFormatsResource.as_view("match_formats_resource"))
    bp.add_url_rule("/match-formats/<int:id>", view_func=MatchFormatResource.as_view("match_format_resource"))
