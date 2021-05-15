"""
Players module.

This module provides routes for viewing and performing actions on players.
"""

import os
import uuid
from http import HTTPStatus

from flask import jsonify, request
from flask.views import MethodView
from scorecard.models.player import Player, PlayerSchema
from scorecard.services.message_service import MessageService
from werkzeug.exceptions import BadRequest, Conflict

from .view_decorators import permission_required

# Schema used to serialize and deserialize user input into player objects
schema = PlayerSchema()

message_service = MessageService()


class PlayersResource(MethodView):
    """Dispatches request methods to retrieve or create players."""

    def get(self):
        """Return the list of all players."""
        query = Player.query.order_by(Player.first_name.asc())

        if request.args and request.args.get("email"):
            query = query.filter_by(email=request.args.get("email"))

        return jsonify(schema.dump(query.all(), many=True)), HTTPStatus.OK

    @permission_required("create:players")
    def post(self):
        """Create a new player."""
        player = schema.load(request.get_json())

        if Player.query.filter_by(email=player.email).count() > 0:
            raise Conflict(description="A player with this email address already exists")

        player.save()

        # Send an email, inviting the player to create an account
        message_service.send_invitation(player)

        return jsonify(schema.dump(player)), HTTPStatus.CREATED


class PlayerResource(MethodView):
    """Dispatches request methods to retrieve or delete an existing player."""

    def get(self, id):
        """Return the player with the given ID."""
        return jsonify(schema.dump(Player.query.get_or_404(id))), HTTPStatus.OK

    @permission_required("update:players")
    def put(self, id):
        """Update the player with the given ID."""
        player = Player.query.get_or_404(id, "The player does not exist")
        player.update(schema.load(request.get_json(), partial=True))

        return jsonify(schema.dump(player)), HTTPStatus.OK

    @permission_required("delete:players")
    def delete(self, id):
        """Delete the player with the given ID."""
        player = Player.query.get_or_404(id, "The player does not exist")
        player.delete()
        return jsonify(message="The player has been deleted"), HTTPStatus.OK


class PlayerPhotoResource(MethodView):
    """Dispatches a request method to upload player profile photos."""

    @permission_required("update:players")
    def put(self, id):
        """Upload an image."""
        player = Player.query.get_or_404(id, "The player does not exist")

        if "photo" not in request.files:
            raise BadRequest("No photo was uploaded")

        photo = request.files["photo"]

        if photo and is_filename_allowed(photo.filename):
            photo_name = f"{uuid.uuid4()}.{get_extension(photo.filename)}"
            photo_path = os.path.join(os.getenv("UPLOAD_FOLDER"), photo_name)
            photo.save(photo_path)

            if os.path.exists(player.photo_path):
                os.remove(player.photo_path)

            player.photo_path = photo_path

            return jsonify(schema.dump(player)), HTTPStatus.OK

        raise BadRequest("File file type is invalid")


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "bmp", "webp"}


def is_filename_allowed(filename):
    # Confirm the filename has an extension and the extension is valid
    return "." in filename and get_extension(filename) in ALLOWED_EXTENSIONS


def get_extension(filename):
    return filename.rsplit(".", 1)[1].lower()


def register_resources(bp):
    """Add the resource routes to the application blueprint."""
    bp.add_url_rule("/players", view_func=PlayersResource.as_view("players_resource"))
    bp.add_url_rule("/players/<int:id>", view_func=PlayerResource.as_view("player_resource"))
    bp.add_url_rule("/players/<int:id>/photo", view_func=PlayerPhotoResource.as_view("player_photo_resource"))
