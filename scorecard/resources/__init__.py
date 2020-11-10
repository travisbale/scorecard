"""Resources package."""

from flask import Blueprint

from . import courses, players, team_members, teams, tee_colors, tournaments

# Create a blueprint for the application resources
bp = Blueprint("api", __name__)

# Register the resources for each module
players.register_resources(bp)
teams.register_resources(bp)
tournaments.register_resources(bp)
team_members.register_resources(bp)
courses.register_resources(bp)
tee_colors.register_resources(bp)
