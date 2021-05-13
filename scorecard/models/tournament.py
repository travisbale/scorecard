"""Tournament module."""

from marshmallow import fields
from marshmallow.decorators import post_load
from scorecard import db
from scorecard.models import Team

from .base import BaseModel, BaseSchema


class Tournament(BaseModel):
    """Represents a tournament."""

    __tablename__ = "tournaments"
    ___table_args___ = (db.UniqueConstraint("name", "start_date", "end_date", name="uix_name_start_date_end_date"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    participants = db.relationship("TeamMember", back_populates="tournament", cascade="all, delete-orphan")
    matches = db.relationship(
        "Match", back_populates="tournament", cascade="all, delete-orphan", order_by="Match.tee_time"
    )

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    @property
    def teams(self):
        teams = Team.query.all()
        result = []

        for team in teams:
            result.append(
                {
                    "name": team.name,
                    "captain": team.get_captain(self),
                    "points": team.get_points(self),
                }
            )

        return result

    def __repr__(self):
        return f"<Tournament {self.start_date.year} {self.name}>"


class TournamentSchema(BaseSchema):
    """Serializes and deserializes tournaments."""

    class TeamSchema(BaseSchema):
        name = fields.String(required=True)
        captain = fields.Nested("PlayerSchema", dump_only=True)
        points = fields.Float(dump_only=True)

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    teams = fields.Nested("TeamSchema", many=True, dump_only=True)

    @post_load
    def load_tournament(self, data, **kwargs):
        """Create a tournament object using the deserialized values."""
        return Tournament(**data)
