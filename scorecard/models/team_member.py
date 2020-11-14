"""Team member module."""

from marshmallow import fields

from scorecard import db

from .base import BaseModel, BaseSchema


class TeamMember(BaseModel):
    """Represents the association between tournaments, players, and teams."""

    __tablename__ = "team_members"

    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id", ondelete="CASCADE"), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    is_captain = db.Column(db.Boolean, default=False, nullable=False)

    tournament = db.relationship("Tournament", back_populates="participants")
    player = db.relationship("Player", back_populates="memberships")
    team = db.relationship("Team", back_populates="members")
    matches = db.relationship("MatchParticipant")

    def __init__(self, tournament_id, team_id, player_id, is_captain):
        self.tournament_id = tournament_id
        self.team_id = team_id
        self.player_id = player_id
        self.is_captain = is_captain

    def __repr__(self):
        return f"<TeamMember team: {self.team.name} player: {self.player.full_name}>"


class TeamMemberSchema(BaseSchema):
    """
    Schema used to viewing and modifying team members.

    The player IDs are then combined with a team ID and are used to create or
    delete TeamMember objects. The team ID is retrieved from the route and does
    not require deserialization.
    """

    player_ids = fields.List(fields.Integer, required=True, load_only=True)
    player = fields.Pluck("PlayerSchema", "full_name", dump_only=True)
    is_captain = fields.Boolean(dump_only=True)
