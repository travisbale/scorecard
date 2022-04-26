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
    photo_path = db.Column(db.String, default="", nullable=False)
    biography = db.Column(db.Text, default="", nullable=False)
    tier = db.Column(db.String(32), default="white", nullable=False)

    memberships = db.relationship("TeamMember", back_populates="player", cascade="all, delete-orphan")
    match_participations = db.relationship("MatchParticipant", back_populates="player")

    def __init__(self, email, first_name, last_name, biography, tier="white", hdcp=0):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography
        self.tier = tier
        self.hdcp = hdcp

    @property
    def full_name(self):
        """Return the player's full name."""
        return f"{self.first_name} {self.last_name}"

    def get_tournaments(self):
        """Return the tournaments the player has played in."""
        return [membership.tournament for membership in self.memberships]

    def get_matches(self):
        """Return the matches the player has played in."""
        return [participation.match for participation in self.match_participations]

    def get_team(self, tournament_id):
        """Return the team the player played on during the tournament."""
        for membership in self.memberships:
            if membership.tournament_id == tournament_id:
                return membership.team

        raise ValueError(f"Player did not play in tournament with ID {tournament_id}")

    def get_hdcp_strokes(self, hole_hdcp):
        return self.hdcp // 18 + (1 if self.hdcp % 18 >= hole_hdcp else 0)

    def get_wins(self):
        wins = 0
        for participation in self.match_participations:
            if participation.team.name == participation.match.winner:
                wins += 1
        return wins

    def get_losses(self):
        losses = 0
        for participation in self.match_participations:
            if participation.match.finished and participation.team.name != participation.match.winner:
                losses += 1
        return losses

    def get_ties(self):
        ties = 0
        for participation in self.match_participations:
            if participation.match.winner == "Tied":
                ties += 1
        return ties

    def get_cups(self):
        cups = 0

        for membership in self.memberships:
            winner = membership.tournament.get_winning_team()
            if winner is not None and winner.name == membership.team.name:
                cups += 1

        return cups

    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name}>"


class PlayerSchema(BaseSchema):
    """Serializes and deserializes player objects."""

    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    full_name = fields.String(dump_only=True)
    photo_path = fields.String(dump_only=True)
    hdcp = fields.Integer()
    biography = fields.String()
    tier = fields.String()

    wins = fields.Function(lambda player: player.get_wins(), dump_only=True)
    losses = fields.Function(lambda player: player.get_losses(), dump_only=True)
    ties = fields.Function(lambda player: player.get_ties(), dump_only=True)
    cups = fields.Function(lambda player: player.get_cups(), dump_only=True)

    @post_load
    def load_player(self, data, **kwargs):
        """Create a player using the deserialized values."""
        return Player(**data)
