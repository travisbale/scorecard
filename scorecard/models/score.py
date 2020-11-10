"""Match score module."""

from marshmallow import fields
from marshmallow.decorators import post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Score(BaseModel):
    """Represents the score on a single hole in a match."""

    __tablename__ = "scores"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["match_id", "player_id"],
            ["match_participants.match_id", "match_participants.player_id"],
            ondelete="CASCADE",
        ),
        db.ForeignKeyConstraint(
            ["match_id", "course_id", "tee_color_id"],
            ["matches.id", "matches.course_id", "matches.tee_color_id"],
            ondelete="CASCADE",
        ),
        db.ForeignKeyConstraint(
            ["course_id", "tee_color_id", "hole_number"], ["holes.course_id", "holes.tee_color_id", "holes.number"]
        ),
        db.CheckConstraint("strokes > 0"),
    )

    match_id = db.Column(db.Integer, db.ForeignKey("matches.id", ondelete="CASCADE"), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), nullable=False)
    hole_number = db.Column(db.Integer, primary_key=True)
    strokes = db.Column(db.Integer, nullable=False)

    participant = db.relationship("MatchParticipant", back_populates="scores")
    hole = db.relationship("Hole")

    def __init__(self, player_id, strokes):
        self.player_id = player_id
        self.strokes = strokes


class ScoreSchema(BaseSchema):
    """Serializes and deserializes a player's scores in a match."""

    player_id = fields.Integer(required=True)
    strokes = fields.Integer(required=True)
    hole_number = fields.Integer(dump_only=True)
    playerName = fields.String(attribute="participant.player.full_name", dump_only=True)

    @post_load
    def load_match_score(self, data, **kwargs):
        """Create a player's score in a match from the deserialized values."""
        return Score(**data)
