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

    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    match_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), primary_key=True)

    match = db.relationship("Match", back_populates="participants")
    player = db.relationship("Player", back_populates="match_participations")
    scores = db.relationship(
        "Score", back_populates="participant", cascade="all, delete-orphan", order_by="Score.hole_number"
    )

    def __init__(self, tournament_id, match_id, player_id):
        self.tournament_id = tournament_id
        self.match_id = match_id
        self.player_id = player_id

    @property
    def team(self):
        """Return the team the player played for during the match."""
        return self.player.get_team(self.tournament_id)


class MatchParticipantSchema(BaseSchema):
    """Serializes and deserializes match participants."""

    player_ids = fields.List(fields.Integer, required=True)
    team = fields.Pluck("TeamSchema", "name", dump_only=True)
    player_id = fields.Integer(attribute="player.id", dump_only=True)
    last_name = fields.String(attribute="player.last_name", dump_only=True)
    full_name = fields.String(attribute="player.full_name", dump_only=True)
