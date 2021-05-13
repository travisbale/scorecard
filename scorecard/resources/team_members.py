"""Team members module."""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.player import Player, PlayerSchema
from scorecard.models.team import Team
from scorecard.models.team_member import TeamMember, TeamMemberSchema
from scorecard.models.tournament import Tournament
from scorecard.resources.view_decorators import permission_required
from werkzeug.exceptions import BadRequest

player_schema = PlayerSchema()
member_schema = TeamMemberSchema()


class TeamMembersResource(MethodView):
    """Dispatches request methods to view or modify the members of a team."""

    def get(self, tournament_id, team_id):
        """Return all the members of the team."""
        self._check_route_params(tournament_id, team_id)

        memberships = TeamMember.query.filter_by(tournament_id=tournament_id, team_id=team_id)
        players = map(lambda membership: membership.player, memberships)

        return jsonify(player_schema.dump(players, many=True)), HTTPStatus.OK

    @permission_required("update:tournament")
    def post(self, tournament_id, team_id):
        """Add new players to a team."""
        players = self._get_players(tournament_id, team_id)

        for player in players:
            member = TeamMember(tournament_id, team_id, player.id, False)
            member.merge()

        return jsonify(message="The players were added to the team"), HTTPStatus.CREATED

    @permission_required("update:tournament")
    def delete(self, tournament_id, team_id):
        """Remove the players from the team."""
        players = self._get_players(tournament_id, team_id)
        memberships = TeamMember.query.filter(
            TeamMember.player_id.in_(map(lambda player: player.id, players)),
            TeamMember.team_id == team_id,
        )

        for membership in memberships:
            membership.delete()

        return jsonify(message="The players have been removed from the team"), HTTPStatus.OK

    def _check_route_params(self, tournament_id, team_id):
        """Verify the route parameters refer to real objects."""
        Tournament.query.get_or_404(tournament_id, "The tournament does not exist")
        Team.query.get_or_404(team_id, "The team does not exist")

    def _get_players(self, tournament_id, team_id):
        """Retrieve the players based on the player IDs in the request."""
        self._check_route_params(tournament_id, team_id)
        # Get the list of players from the database
        request_json = member_schema.load(request.get_json())
        players = Player.query.filter(Player.id.in_(request_json["player_ids"]))

        # Check that all the players exist
        if players.count() != len(request_json["player_ids"]):
            raise BadRequest(description="One or more of the players do not exist")

        return players


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule(
        "/tournaments/<int:tournament_id>/teams/<int:team_id>/players",
        view_func=TeamMembersResource.as_view("team_members_resource"),
    )
