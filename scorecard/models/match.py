"""Match module."""

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
    )

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), nullable=False)
    match_format_id = db.Column(db.Integer, db.ForeignKey("match_formats.id"), nullable=False)
    tee_time = db.Column(db.DateTime)

    tournament = db.relationship("Tournament", back_populates="matches")
    tee_set = db.relationship("TeeSet")
    participants = db.relationship("MatchParticipant", back_populates="match", cascade="all, delete-orphan")

    def __init__(self, course_id, tee_color_id, match_format_id, tee_time):
        self.course_id = course_id
        self.tee_color_id = tee_color_id
        self.match_format_id = match_format_id
        self.tee_time = tee_time

    @property
    def players(self):
        """Return the list of players currently participating in the match."""
        return [participant.player for participant in self.participants]


class MatchSchema(BaseSchema):
    """Serializes and deserializes matches of golf."""

    id = fields.Integer(dump_only=True)
    course_id = fields.Integer(required=True)
    tee_color_id = fields.Integer(required=True)
    match_format_id = fields.Integer(required=True)
    tee_time = fields.DateTime(required=True)

    @post_load
    def load_match(self, data, **kwargs):
        """Create a match using the serialized values."""
        return Match(**data)
