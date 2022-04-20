"""Team module."""

from marshmallow import fields
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

    def get_team_members(self, tournament):
        return list(filter(lambda member: member.tournament_id == tournament.id, self.members))

    def get_captain(self, tournament_id):
        """Return the captain of the team."""
        captains = list(filter(lambda member: member.is_captain, self.get_team_members(tournament_id)))
        return captains[0].player if len(captains) > 0 else None

    def get_points(self, tournament):
        """Return the teams total points."""
        points = 0

        for match in tournament.matches:
            winner = match.winner

            if winner == self.name:
                points += 1
            elif winner == "Tied":
                points += 0.5

        return points

    def __repr__(self):
        return f"<Team {self.name}>"


class TeamSchema(BaseSchema):
    """Schema used to view teams."""

    id = fields.Integer(dump_only=True)
    name = fields.String(dump_only=True)
