"""Team module."""

from marshmallow import fields, post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Team(BaseModel):
    """
    Represents a team.

    Teams belong to a tournament and are used to group players together so they
    can play against one another.
    """

    __tablename__ = "teams"
    __table_args__ = (db.UniqueConstraint("name"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    members = db.relationship("TeamMember", back_populates="team", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    @property
    def captain(self):
        """Return the captain of the team."""
        captains = list(filter(lambda member: member.is_captain, self.members))
        return captains[0].player if len(captains) > 0 else None

    @property
    def points(self):
        """Return the teams total points."""
        points = 0

        if len(self.members) > 0:
            for match in self.members[0].tournament.matches:
                winner = match.winner

                if winner == self.name:
                    points += 1
                elif winner == "Tied":
                    points += points + 0.5

        return points

    def __repr__(self):
        return f"<Team {self.name}>"


class TeamSchema(BaseSchema):
    """Serializes and deserializes team objects."""

    id = fields.Integer()
    name = fields.String(required=True)
    captain = fields.Nested("PlayerSchema", dump_only=True)
    points = fields.Float(dump_only=True)

    @post_load
    def load_team(self, data, **kwargs):
        """Create a team object using the deserialized values."""
        return Team(**data)
