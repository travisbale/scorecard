"""matchs module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import BadRequest

from scorecard.models.match import Match, MatchSchema
from scorecard.models.player import Player
from scorecard.models.tee_set import TeeSet
from scorecard.models.tournament import Tournament

schema = MatchSchema()


class TournamentMatchesResource(MethodView):
    """Dispatches request methods to retrieve or create matches."""

    def get(self, tournament_id):
        """Return a list of all the matches played in the tournament."""
        tournament = Tournament.query.get_or_404(tournament_id, "The tournament does not exist")
        return jsonify(schema.dump(tournament.matches, many=True)), HTTPStatus.OK

    def post(self, tournament_id):
        """Create a new match played from the tee color at the golf course."""
        Tournament.query.get_or_404(tournament_id, "The tournament does not exist")
        match = schema.load(request.get_json())
        match.tournament_id = tournament_id

        if TeeSet.query.get((match.course_id, match.tee_color_id)) is None:
            raise BadRequest(description="Those tees do not exist")

        match.save()
        return jsonify(schema.dump(match)), HTTPStatus.CREATED


class PlayerMatchesResource(MethodView):
    """Dispatches request methods to retrieve the matches for a player."""

    def get(self, player_id):
        """Return the matches that the player has played in."""
        player = Player.query.get_or_404(player_id, "The player does not exist")
        return jsonify(schema.dump(player.matches, many=True)), HTTPStatus.OK


class MatchResource(MethodView):
    """Dispatches request methods to retrieve and delete matches."""

    def get(self, match_id):
        """Return the match with the given ID."""
        match = Match.query.get_or_404(match_id, "The match does not exist")
        return jsonify(schema.dump(match)), HTTPStatus.OK

    def delete(self, match_id):
        """Delete the match with the given ID."""
        match = Match.query.get_or_404(match_id, "The match does not exist")
        match.delete()
        return jsonify(message="The match has been deleted")


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule(
        "/tournaments/<int:tournament_id>/matches",
        view_func=TournamentMatchesResource.as_view("tournament_matches_resource"),
    )
    bp.add_url_rule("/matches/<int:match_id>", view_func=MatchResource.as_view("match_resource"))
    bp.add_url_rule(
        "/players/<int:player_id>/matches", view_func=PlayerMatchesResource.as_view("player_matches_resource")
    )
