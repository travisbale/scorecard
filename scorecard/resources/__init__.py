"""Resources package."""

from flask import Blueprint

from . import players, team_members, teams, tournaments

# Create a blueprint for the application resources
bp = Blueprint("api", __name__)

# Register the resources for each module
players.register_resources(bp)
teams.register_resources(bp)
tournaments.register_resources(bp)
team_members.register_resources(bp)
