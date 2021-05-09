"""Resources package."""

from flask import Blueprint

from . import (
    courses,
    holes,
    match_formats,
    match_participants,
    matches,
    players,
    scores,
    team_members,
    tee_colors,
    tee_sets,
    tournaments,
)

# Create a blueprint for the application resources
bp = Blueprint("api", __name__)

# Register the resources for each module
players.register_resources(bp)
tournaments.register_resources(bp)
team_members.register_resources(bp)
courses.register_resources(bp)
tee_colors.register_resources(bp)
tee_sets.register_resources(bp)
holes.register_resources(bp)
match_formats.register_resources(bp)
match_participants.register_resources(bp)
matches.register_resources(bp)
scores.register_resources(bp)
