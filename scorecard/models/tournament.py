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
    location = db.Column(db.String(255), nullable=False)

    participants = db.relationship("TeamMember", back_populates="tournament", cascade="all, delete-orphan")
    matches = db.relationship(
        "Match", back_populates="tournament", cascade="all, delete-orphan", order_by="Match.tee_time"
    )

    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

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

    def is_finished(self):
        return len(self.matches) > 0 and len(list(filter(lambda m: not m.finished, self.matches))) == 0

    def get_winning_team(self):
        if not self.is_finished():
            return None

        blueTeam = Team.query.filter_by(name="Blue").first()
        redTeam = Team.query.filter_by(name="Red").first()

        return redTeam if redTeam.get_points(self) > blueTeam.get_points(self) else blueTeam

    def __repr__(self):
        return f"<Tournament {self.start_date.year} {self.name}>"


class TournamentSchema(BaseSchema):
    """Serializes and deserializes tournaments."""

    class TournamentTeamSchema(BaseSchema):
        name = fields.String(required=True)
        captain = fields.Nested("PlayerSchema", dump_only=True)
        points = fields.Float(dump_only=True)

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    location = fields.String(required=True)
    teams = fields.Nested("TournamentTeamSchema", many=True, dump_only=True)
    is_finished = fields.Function(lambda tournament: tournament.is_finished(), dump_only=True)

    @post_load
    def load_tournament(self, data, **kwargs):
        """Create a tournament object using the deserialized values."""
        return Tournament(**data)
