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

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Team {self.name}>"


class TeamSchema(BaseSchema):
    """Serializes and deserializes team objects."""

    id = fields.Integer()
    name = fields.String(required=True)

    @post_load
    def load_team(self, data, **kwargs):
        """Create a team object using the deserialized values."""
        return Team(**data)
