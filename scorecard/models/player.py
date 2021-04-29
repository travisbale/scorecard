"""Player module."""

from marshmallow import fields
from marshmallow.decorators import post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Player(BaseModel):
    """Represents a player object."""

    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    hdcp = db.Column(db.Integer, default=0, nullable=False)

    memberships = db.relationship("TeamMember", back_populates="player", cascade="all, delete-orphan")
    match_participations = db.relationship("MatchParticipant", back_populates="player")

    def __init__(self, email, first_name, last_name, hdcp=0):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.hdcp = hdcp

    @property
    def full_name(self):
        """Return the player's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def matches(self):
        """Return the matches the player has played in."""
        return [participation.match for participation in self.match_participations]

    @property
    def tournaments(self):
        """Return the tournaments the player has played in."""
        return [membership.tournament for membership in self.memberships]

    def get_team(self, tournament_id):
        """Return the team the player played on during the tournament."""
        for membership in self.memberships:
            if membership.tournament_id == tournament_id:
                return membership.team

        raise ValueError(f"Player did not play in tournament with ID {tournament_id}")

    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name}>"


class PlayerSchema(BaseSchema):
    """Serializes and deserializes player objects."""

    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    full_name = fields.String(dump_only=True)
    hdcp = fields.Integer()
    confidence = fields.Constant(0, dump_only=True)
    wins = fields.Constant(0, dump_only=True)
    losses = fields.Constant(0, dump_only=True)
    ties = fields.Constant(0, dump_only=True)
    cups = fields.Constant(0, dump_only=True)
    bio = fields.Constant("Player biography", dump_only=True)
    pictureUrl = fields.Constant("/img/fordyce.png", dump_only=True)
    level = fields.Constant("white", dump_only=True)

    @post_load
    def load_player(self, data, **kwargs):
        """Create a player using the deserialized values."""
        return Player(**data)
