"""Tee color module."""

from marshmallow import fields, post_load

from scorecard import db
from scorecard.models.base import BaseModel, BaseSchema


class TeeColor(BaseModel):
    """Represents a tee color."""

    __tablename__ = "tee_colors"
    __table_args__ = (db.UniqueConstraint("color"),)

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(16), nullable=False)

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"<TeeColor {self.color}>"


class TeeColorSchema(BaseSchema):
    """Serializes and deserializes tee colors."""

    id = fields.Integer(dump_only=True)
    color = fields.String(required=True)

    @post_load
    def load_tee_color(self, data, **kwargs):
        """Create a tee color using the serialized values."""
        return TeeColor(**data)
