"""Resources package."""

from flask import Blueprint

from . import players

# Create a blueprint for the application resources
bp = Blueprint("api", __name__)

# Register the resources for each module
players.register_resources(bp)
