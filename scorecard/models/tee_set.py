"""Teeing area module."""

import simplejson
from marshmallow import fields, post_load, validate

from scorecard import db

from .base import BaseModel, BaseSchema

# Constants
MIN_SLOPE = 55
MAX_SLOPE = 155


class TeeSet(BaseModel):
    """Represents a set of teeing areas at a golf course."""

    __tablename__ = "tee_sets"
    __table_args__ = (db.CheckConstraint(f"slope >= {MIN_SLOPE} AND slope <= {MAX_SLOPE}"),)

    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True)
    tee_color_id = db.Column(db.Integer, db.ForeignKey("tee_colors.id"), primary_key=True)
    slope = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Numeric(4, 1), nullable=False)

    course = db.relationship("Course", back_populates="tee_sets")
    tee_color = db.relationship("TeeColor")
    holes = db.relationship("Hole", back_populates="tee_set", cascade="all, delete-orphan")

    def __init__(self, tee_color_id, slope, rating, course_id=None):
        self.tee_color_id = tee_color_id
        self.slope = slope
        self.rating = rating
        self.course_id = course_id

    @property
    def yards(self):
        """Return the total yards for the tee set."""
        return sum(map(lambda hole: hole.yards, self.holes))

    @property
    def par(self):
        """Return the par for the tee set."""
        return sum(map(lambda hole: hole.par, self.holes))

    def __repr__(self):
        return f"<Tees {self.id}>"


class TeeSetSchema(BaseSchema):
    """Serializes and deserializes a set of golf course tees."""

    tee_color_id = fields.Integer(required=True)
    slope = fields.Integer(required=True, validate=validate.Range(min=MIN_SLOPE, max=MAX_SLOPE))
    rating = fields.Decimal(required=True)
    course = fields.Pluck("CourseSchema", "name")
    yards = fields.Integer(dump_only=True)
    par = fields.Integer(dump_only=True)
    tee_color = fields.Pluck("TeeColorSchema", "color")
    holes = fields.Nested("HoleSchema", many=True)

    class Meta:
        """Override the json module so decimal.Decimal can be serialized."""

        render_module = simplejson

    @post_load
    def load_tees(self, data, **kwargs):
        """Create a set of tees using the deserialized values."""
        return TeeSet(**data)
