"""
Teams module.

This module provides routes for viewing and actioning teams.
"""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict

from scorecard.models.team import Team, TeamSchema

schema = TeamSchema()


class TeamsResource(MethodView):
    """Dispatches request methods to retrieve or create teams."""

    def get(self, tournament_id):
        """Return a list of teams participating in the tournament."""
        return jsonify(schema.dump(Team.query.all(), many=True)), HTTPStatus.OK

    def post(self, tournament_id):
        """Create a new team to participate in the tournament."""
        team = schema.load(request.get_json())

        if Team.query.filter_by(name=team.name).count() > 0:
            raise Conflict(description="The team already exists")

        team.save()
        return jsonify(schema.dump(team)), HTTPStatus.CREATED


class TeamResource(MethodView):
    """Dispatches request methods to retrieve or delete an existing team."""

    def get(self, tournament_id, team_id):
        """Return the team with the given ID."""
        team = Team.query.get_or_404(team_id, "The team does not exist")
        return jsonify(schema.dump(team)), HTTPStatus.OK

    def delete(self, tournament_id, team_id):
        """Delete the team with the given ID."""
        team = Team.query.get_or_404(team_id, "The team does not exist")
        team.delete()
        return jsonify(message="The team has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/tournaments/<int:tournament_id>/teams", view_func=TeamsResource.as_view("teams_resource"))
    bp.add_url_rule(
        "/tournaments/<int:tournament_id>/teams/<int:team_id>", view_func=TeamResource.as_view("team_resource")
    )
