"""Match module."""

import numpy as np
from marshmallow import fields, post_load
from scorecard import db

from .base import BaseModel, BaseSchema


class Match(BaseModel):
    """Represents a match in a tournament."""

    __tablename__ = "matches"
    __table_args__ = (
        db.ForeignKeyConstraint(["course_id", "tee_color_id"], ["tee_sets.course_id", "tee_sets.tee_color_id"]),
        # These columns must be declared unique because they are used as foreign keys
        db.UniqueConstraint("id", "tournament_id"),
        db.UniqueConstraint("id", "course_id", "tee_color_id", name="uix_id_course_id_tee_color_id"),
    )

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), nullable=False)
    match_format_id = db.Column(db.Integer, db.ForeignKey("match_formats.id"), nullable=False)
    tee_time = db.Column(db.DateTime)
    handicapped = db.Column(db.Boolean, default=False, nullable=False)

    tournament = db.relationship("Tournament", back_populates="matches")
    tee_set = db.relationship("TeeSet")
    match_format = db.relationship("MatchFormat")
    participants = db.relationship("MatchParticipant", back_populates="match", cascade="all, delete-orphan")

    def __init__(self, course_id, tee_color_id, match_format_id, tee_time, tournament_id=None):
        self.course_id = course_id
        self.tee_color_id = tee_color_id
        self.match_format_id = match_format_id
        self.tee_time = tee_time
        self.tournament_id = tournament_id

    def get_team_members(self, team_name):
        return list(filter(lambda participant: participant.team.name == team_name, self.participants))

    @property
    def scores(self):
        """Return the current score in the match."""
        scores = [{"matchStatus": 0, "statusText": ""}]

        if self.started():
            red_team_strokes = []
            blue_team_strokes = []

            for member in self.get_team_members("Red"):
                if self.handicapped:
                    red_team_strokes.append(list(map(lambda s: s.net_strokes, member.scores)))
                else:
                    red_team_strokes.append(list(map(lambda s: s.strokes, member.scores)))

            for member in self.get_team_members("Blue"):
                if self.handicapped:
                    blue_team_strokes.append(list(map(lambda s: s.net_strokes, member.scores)))
                else:
                    blue_team_strokes.append(list(map(lambda s: s.strokes, member.scores)))

            red_team_strokes = (
                np.minimum(red_team_strokes[0], red_team_strokes[1])
                if len(red_team_strokes) == 2
                else red_team_strokes[0]
            )
            blue_team_strokes = (
                np.minimum(blue_team_strokes[0], blue_team_strokes[1])
                if len(blue_team_strokes) == 2
                else blue_team_strokes[0]
            )

            for blue_score, red_score in zip(blue_team_strokes, red_team_strokes):
                status_change = 1 if blue_score > red_score else -1 if red_score > blue_score else 0
                matchStatus = scores[-1]["matchStatus"] + status_change

                if scores[-1]["statusText"].find("&") != -1:
                    status_text = scores[-1]["statusText"]
                elif matchStatus == 0:
                    status_text = "AS"
                else:
                    if abs(matchStatus) > 18 - len(scores) and len(scores) != 18:
                        status_text = f"{abs(matchStatus)} & {18 - len(scores)}"
                    else:
                        status_text = f"{abs(matchStatus)} UP"

                scores.append(
                    {
                        "redTeamScore": red_score,
                        "blueTeamScore": blue_score,
                        "matchStatus": matchStatus,
                        "statusText": status_text,
                    }
                )

        return scores[1:]

    @property
    def winner(self):
        if self.finished:
            if self.scores[-1]["matchStatus"] > 0:
                return "Red"
            elif self.scores[-1]["matchStatus"] < 0:
                return "Blue"
            else:
                return "Tied"
        else:
            return ""

    @property
    def players(self):
        """Return the list of players currently participating in the match."""
        return [participant.player for participant in self.participants]

    def started(self):
        for participant in self.participants:
            if len(participant.scores) == 0:
                return False

        # Match hasn't started if there are no participants
        return len(self.participants) > 0

    @property
    def finished(self):
        if len(self.participants) == 0:
            return False
        if len(self.scores) > 0 and self.scores[-1]["statusText"].find("&") > 0:
            return True

        for participant in self.participants:
            if len(participant.scores) < 18:
                return False

        return True


class MatchSchema(BaseSchema):
    """Serializes and deserializes matches of golf."""

    class HoleStatusSchema(BaseSchema):
        redTeamScore = fields.Integer()
        blueTeamScore = fields.Integer()
        matchStatus = fields.Integer()
        statusText = fields.String()

    id = fields.Integer(dump_only=True)
    course_id = fields.Integer(required=True)
    tee_color_id = fields.Integer(required=True)
    match_format_id = fields.Integer(required=True, load_only=True)
    match_format = fields.Pluck("MatchFormatSchema", "name", data_key="format", dump_only=True)
    tee_time = fields.DateTime(required=True)
    participants = fields.Nested("MatchParticipantSchema", many=True)
    scores = fields.Nested("HoleStatusSchema", many=True, dump_only=True)
    finished = fields.Boolean(dump_only=True)
    tournament_id = fields.Integer(dump_only=True)

    @post_load
    def load_match(self, data, **kwargs):
        """Create a match using the serialized values."""
        return Match(**data)
