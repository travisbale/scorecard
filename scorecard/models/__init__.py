"""Models package."""

from flask import Blueprint
from scorecard import db

from .course import Course
from .hole import Hole
from .match import Match
from .match_format import MatchFormat
from .match_participant import MatchParticipant
from .player import Player
from .score import Score
from .team import Team
from .team_member import TeamMember
from .tee_color import TeeColor
from .tee_set import TeeSet
from .tournament import Tournament

bp = Blueprint("database", __name__)

__all__ = [
    "Course",
    "Hole",
    "Match",
    "MatchFormat",
    "MatchParticipant",
    "Player",
    "Score",
    "Team",
    "TeamMember",
    "TeeColor",
    "TeeSet",
    "Tournament",
]


@bp.after_app_request
def commit_session(response):
    """After each successful request commit the current database session."""
    if response.status_code < 400:
        # TODO: Might have to catch exceptions here
        db.session.commit()

    return response
