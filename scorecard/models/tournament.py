"""Tournament module."""

from marshmallow import fields
from marshmallow.decorators import post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Tournament(BaseModel):
    """Represents a tournament."""

    __tablename__ = "tournaments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Tournament {self.start_date.year} {self.name}>"


class TournamentSchema(BaseSchema):
    """Serializes and deserializes tournaments."""

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    @post_load
    def load_tournament(self, data, **kwargs):
        """Create a tournament object using the deserialized values."""
        return Tournament(**data)
