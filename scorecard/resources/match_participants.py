"""Match participants module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import BadRequest, NotFound

from scorecard.models.match import Match
from scorecard.models.match_participant import MatchParticipant, MatchParticipantSchema
from scorecard.models.player import Player, PlayerSchema

player_schema = PlayerSchema()
participant_schema = MatchParticipantSchema()


class MatchParticipantsResource(MethodView):
    """Dispatches request methods to view or modify the players in a match."""

    def get(self, tournament_id, match_id):
        """Return all the players playing in the given match."""
        match = self._check_route_parameters(tournament_id, match_id)
        return jsonify(player_schema.dump(match.players, many=True)), HTTPStatus.OK

    def post(self, tournament_id, match_id):
        """Add the players to the match."""
        players = self._get_players(tournament_id, match_id)

        for player in players:
            participant = MatchParticipant(tournament_id, match_id, player.id)
            participant.merge()

        return jsonify(message="The players were assigned to the match"), HTTPStatus.CREATED

    def delete(self, tournament_id, match_id):
        """Delete the players from the match."""
        players = self._get_players(tournament_id, match_id)
        participants = MatchParticipant.query.filter(
            MatchParticipant.player_id.in_(map(lambda player: player.id, players)),
            MatchParticipant.match_id == match_id,
        )

        for participant in participants:
            participant.delete()

        return jsonify(message="The players have been removed from the match"), HTTPStatus.OK

    def _check_route_parameters(self, tournament_id, match_id):
        match = Match.query.get_or_404(match_id, "The match does not exist")

        if match.tournament_id != tournament_id:
            raise NotFound("The match does not exist")

        return match

    def _get_players(self, tournament_id, match_id):
        self._check_route_parameters(tournament_id, match_id)

        request_json = participant_schema.load(request.get_json())
        players = Player.query.filter(Player.id.in_(request_json["player_ids"]))

        # Check that all the players exist
        if players.count() != len(request_json["player_ids"]):
            raise BadRequest(description="One of more of the players do not exist")

        return players


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule(
        "/tournaments/<int:tournament_id>/matches/<int:match_id>/players",
        view_func=MatchParticipantsResource.as_view("match_participants_resource"),
    )
