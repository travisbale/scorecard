"""Match module."""

import numpy as np
from marshmallow import fields, post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Match(BaseModel):
    """Represents a match in a tournament."""

    __tablename__ = "matches"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["course_id", "tee_color_id"], ["tee_sets.course_id", "tee_sets.tee_color_id"], ondelete="CASCADE"
        ),
        db.UniqueConstraint("id", "tournament_id"),
        db.UniqueConstraint("id", "course_id", "tee_color_id", name="uix_id_course_id_tee_color_id"),
    )

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), nullable=False)
    match_format_id = db.Column(db.Integer, db.ForeignKey("match_formats.id"), nullable=False)
    tee_time = db.Column(db.DateTime)

    tournament = db.relationship("Tournament", back_populates="matches")
    tee_set = db.relationship("TeeSet")
    match_format = db.relationship("MatchFormat")
    participants = db.relationship("MatchParticipant", back_populates="match", cascade="all, delete-orphan")

    def __init__(self, course_id, tee_color_id, match_format_id, tee_time):
        self.course_id = course_id
        self.tee_color_id = tee_color_id
        self.match_format_id = match_format_id
        self.tee_time = tee_time

    def get_team_members(self, team_name):
        return list(filter(lambda participant: participant.team.name == team_name, self.participants))

    @property
    def score(self):
        """Return the current score in the match."""
        score = 0

        if self.started():
            red_team_members = self.get_team_members("Red")
            blue_team_members = self.get_team_members("Blue")

            red_team_strokes = []
            blue_team_strokes = []

            for member in red_team_members:
                red_team_strokes.append(list(map(lambda s: s.strokes, member.scores)))

            for member in blue_team_members:
                blue_team_strokes.append(list(map(lambda s: s.strokes, member.scores)))

            red_team_strokes = (
                np.minimum(red_team_strokes[0], red_team_strokes[1])
                if len(red_team_strokes) == 2
                else red_team_strokes[0]
            )
            blue_team_strokes = (
                np.minimum(blue_team_strokes[0], blue_team_strokes[1])
                if len(blue_team_strokes) == 2
                else blue_team_strokes[0]
            )

            for blue_score, red_score in zip(blue_team_strokes, red_team_strokes):
                if blue_score > red_score:
                    score += 1
                elif red_score > blue_score:
                    score -= 1

        return {
            "leader": "Red" if score > 0 else "Blue" if score < 0 else "Tied",
            "status": "AS" if score == 0 else f"{abs(score)} UP",
        }

    @property
    def winner(self):
        return self.score["leader"] if self.finished else ""

    @property
    def players(self):
        """Return the list of players currently participating in the match."""
        return [participant.player for participant in self.participants]

    def started(self):
        for participant in self.participants:
            if len(participant.scores) == 0:
                return False

        return True

    @property
    def finished(self):
        for participant in self.participants:
            if len(participant.scores) < 18:
                return False

        return True


class MatchSchema(BaseSchema):
    """Serializes and deserializes matches of golf."""

    id = fields.Integer(dump_only=True)
    course_id = fields.Integer(required=True)
    tee_color_id = fields.Integer(required=True)
    match_format_id = fields.Integer(required=True, load_only=True)
    match_format = fields.Pluck("MatchFormatSchema", "name", data_key="format", dump_only=True)
    tee_time = fields.DateTime(required=True)
    participants = fields.Nested("MatchParticipantSchema", many=True)
    score = fields.Dict(dump_only=True)
    finished = fields.Boolean(dump_only=True)

    @post_load
    def load_match(self, data, **kwargs):
        """Create a match using the serialized values."""
        return Match(**data)
