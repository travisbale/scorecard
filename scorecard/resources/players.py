"""
Players module.

This module provides routes for viewing and performing actions on players.
"""

from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.player import Player, PlayerSchema
from werkzeug.exceptions import Conflict

from .view_decorators import permission_required

# Schema used to serialize and deserialize user input into player objects
schema = PlayerSchema()


class PlayersResource(MethodView):
    """Dispatches request methods to retrieve or create players."""

    def get(self):
        """Return the list of all players."""
        return jsonify(schema.dump(Player.query.all(), many=True)), HTTPStatus.OK

    @permission_required("create:players")
    def post(self):
        """Create a new player."""
        player = schema.load(request.get_json())

        if Player.query.filter_by(email=player.email).count() > 0:
            raise Conflict(description="A player with this email address already exists")

        player.save()
        return jsonify(schema.dump(player)), HTTPStatus.CREATED


class PlayerResource(MethodView):
    """Dispatches request methods to retrieve or delete an existing player."""

    def get(self, id):
        """Return the player with the given ID."""
        return jsonify(schema.dump(Player.query.get_or_404(id))), HTTPStatus.OK

    @permission_required("delete:players")
    def delete(self, id):
        """Delete the player with the given ID."""
        player = Player.query.get_or_404(id, "The player does not exist")
        player.delete()
        return jsonify(message="The player has been deleted"), HTTPStatus.OK


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/players", view_func=PlayersResource.as_view("players_resource"))
    bp.add_url_rule("/players/<int:id>", view_func=PlayerResource.as_view("player_resource"))
