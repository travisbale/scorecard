"""Match format module."""

from marshmallow import fields, post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class MatchFormat(BaseModel):
    """Represents the format of a match."""

    __tablename__ = "match_formats"
    __table_args__ = (db.UniqueConstraint("name", name="uix_name"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<MatchFormat {self.name}>"


class MatchFormatSchema(BaseSchema):
    """Serializes and deserializes match formats."""

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)

    @post_load
    def load_match_format(self, data, **kwargs):
        """Create a match format object from the deserialized data."""
        return MatchFormat(**data)
