"""Hole module."""

from marshmallow import fields, post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Hole(BaseModel):
    """Represents a hole on a golf course."""

    __tablename__ = "holes"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["course_id", "tee_color_id"], ["tee_sets.course_id", "tee_sets.tee_color_id"], ondelete="CASCADE"
        ),
        db.CheckConstraint("number >= 1 AND number <= 18", name="number"),
        db.CheckConstraint("hdcp >= 1 AND hdcp <= 18", name="hdcp"),
        db.CheckConstraint("par >= 3 AND par <= 6", name="par"),
        db.UniqueConstraint("course_id", "tee_color_id", "hdcp"),
    )

    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), primary_key=True)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), primary_key=True)
    number = db.Column(db.Integer, primary_key=True)
    par = db.Column(db.Integer, nullable=False)
    hdcp = db.Column(db.Integer, nullable=False)
    yards = db.Column(db.Integer, nullable=False)

    tee_set = db.relationship("TeeSet", back_populates="holes")

    def __init__(self, number, par, hdcp, yards, course_id=None, tee_color_id=None):
        self.number = number
        self.par = par
        self.hdcp = hdcp
        self.yards = yards
        self.course_id = course_id
        self.tee_color_id = tee_color_id


class HoleSchema(BaseSchema):
    """Serializes and deserializes golf course holes."""

    number = fields.Integer(required=True)
    par = fields.Integer(required=True)
    hdcp = fields.Integer(required=True)
    yards = fields.Integer(required=True)

    @post_load
    def load_hole(self, data, **kwargs):
        """Create a tee useing the deserialized values."""
        return Hole(**data)
