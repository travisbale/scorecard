"""A script to create White Bear Lake Golf Course."""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create white bear."""
    whitebear = Course.query.filter_by(name="White Bear Lake Golf Course").first()

    if whitebear is not None:
        whitebear.delete()

    whitebear = Course("White Bear Lake Golf Course")
    whitebear.save()

    whites = [
        Hole(1, 5, 18, 444),
        Hole(2, 3, 8, 143),
        Hole(3, 4, 10, 347),
        Hole(4, 4, 16, 347),
        Hole(5, 4, 12, 319),
        Hole(6, 4, 4, 375),
        Hole(7, 4, 2, 398),
        Hole(8, 3, 6, 169),
        Hole(9, 5, 14, 489),
        Hole(10, 4, 7, 390),
        Hole(11, 3, 17, 154),
        Hole(12, 5, 3, 558),
        Hole(13, 4, 13, 340),
        Hole(14, 4, 11, 346),
        Hole(15, 4, 1, 390),
        Hole(16, 3, 5, 191),
        Hole(17, 5, 9, 511),
        Hole(18, 4, 15, 350),
    ]

    create_holes(whitebear.id, "White", 125, 70.7, whites)

    db.session.commit()


def create_holes(course_id, tee_color, slope, rating, holes):
    """Create the tees on the golf course."""
    tee_color_id = TeeColor.query.filter_by(color=tee_color).first().id

    tee_set = TeeSet(tee_color_id, slope, rating)
    tee_set.course_id = course_id
    tee_set.save()

    for hole in holes:
        hole.course_id = course_id
        hole.tee_color_id = tee_color_id
        hole.save()
