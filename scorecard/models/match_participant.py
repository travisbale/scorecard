"""Match participation module."""

from marshmallow import fields

from scorecard import db

from .base import BaseModel, BaseSchema


class MatchParticipant(BaseModel):
    """Represents the link between matches and participants."""

    __tablename__ = "match_participants"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["tournament_id", "match_id"], ["matches.tournament_id", "matches.id"], ondelete="CASCADE"
        ),
        db.ForeignKeyConstraint(
            ["tournament_id", "player_id"], ["team_members.tournament_id", "team_members.player_id"]
        ),
    )

    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"))
    match_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), primary_key=True)

    match = db.relationship("Match", back_populates="participants")
    player = db.relationship("Player", back_populates="match_participations")

    def __init__(self, tournament_id, match_id, player_id):
        self.tournament_id = tournament_id
        self.match_id = match_id
        self.player_id = player_id


class MatchParticipantSchema(BaseSchema):
    """Serializes and deserializes match participants."""

    player_ids = fields.List(fields.Integer, required=True)
