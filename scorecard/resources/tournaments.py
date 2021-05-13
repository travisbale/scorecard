"""
Tournaments module.

This module provides routes for viewing and actioning tournaments.
"""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.player import Player
from scorecard.models.tournament import Tournament, TournamentSchema

from .view_decorators import permission_required

schema = TournamentSchema()


class TournamentsResource(MethodView):
    """Dispatches request methods to retrieve or create tournaments."""

    def get(self):
        """Return a list of the tournaments."""
        return jsonify(schema.dump(Tournament.query.order_by(Tournament.start_date).all(), many=True)), HTTPStatus.OK

    @permission_required("create:tournaments")
    def post(self):
        """Create a new tournament."""
        tournament = schema.load(request.get_json())
        tournament.save()
        return jsonify(schema.dump(tournament)), HTTPStatus.CREATED


class PlayerTournamentsResource(MethodView):
    """Dispatches request methods to retrieve tournaments a player has played in."""

    def get(self, player_id):
        """Return a list of the tournaments the player has played in."""
        player = Player.query.get_or_404(player_id, "The player does not exist")
        return jsonify(schema.dump(player.tournaments, many=True)), HTTPStatus.OK


class TournamentResource(MethodView):
    """Dispatches request methods to retrieve or delete an existing tournament."""

    def get(self, id):
        """Return the tournament with the given ID."""
        tournament = Tournament.query.get_or_404(id, "The tournament does not exist")
        return jsonify(schema.dump(tournament)), HTTPStatus.OK

    @permission_required("update:tournaments")
    def put(self, id):
        """Update an existing tournament."""
        tournament = Tournament.query.get_or_404(id, "The tournament does not exist")
        tournament.update(schema.load(request.get_json(), partial=True))

        return jsonify(schema.dump(tournament)), HTTPStatus.OK

    @permission_required("delete:tournaments")
    def delete(self, id):
        """Delete the tournament with the given ID."""
        tournament = Tournament.query.get_or_404(id, "The tournament does not exist")
        tournament.delete()
        return jsonify(message="The tournament has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/tournaments", view_func=TournamentsResource.as_view("tournaments_resource"))
    bp.add_url_rule("/tournaments/<int:id>", view_func=TournamentResource.as_view("tournament_resource"))
    bp.add_url_rule(
        "/players/<int:player_id>/tournaments",
        view_func=PlayerTournamentsResource.as_view("player_tournaments_resource"),
    )
