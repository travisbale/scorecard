"""Course module."""

from marshmallow import fields, post_load

from scorecard import db

from .base import BaseModel, BaseSchema


class Course(BaseModel):
    """Represents a golf course."""

    __tablename__ = "courses"
    __table_args__ = (db.UniqueConstraint("name"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    tee_sets = db.relationship("TeeSet", back_populates="course", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Course {self.name}>"


class CourseSchema(BaseSchema):
    """Serializes and deserializes courses."""

    id = fields.Integer()
    name = fields.String(required=True)

    @post_load
    def load_course(self, data, **kwargs):
        """Create a course using the serialized values."""
        return Course(**data)
