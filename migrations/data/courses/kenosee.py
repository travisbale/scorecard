"""A script to create Golf Kenosee."""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create kenosee."""
    kenosee = Course.query.filter_by(name="Kenosee").first()

    if kenosee is not None:
        kenosee.delete()

    kenosee = Course("Kenosee")
    kenosee.save()

    blacks = [
        Hole(1, 4, 11, 360),
        Hole(2, 5, 15, 460),
        Hole(3, 4, 13, 367),
        Hole(4, 4, 17, 338),
        Hole(5, 3, 9, 178),
        Hole(6, 5, 3, 538),
        Hole(7, 4, 1, 433),
        Hole(8, 3, 7, 165),
        Hole(9, 4, 5, 361),
        Hole(10, 5, 16, 499),
        Hole(11, 4, 12, 335),
        Hole(12, 5, 8, 519),
        Hole(13, 4, 4, 322),
        Hole(14, 3, 6, 202),
        Hole(15, 4, 2, 402),
        Hole(16, 4, 10, 315),
        Hole(17, 4, 18, 360),
        Hole(18, 3, 14, 161),
    ]

    blues = [
        Hole(1, 4, 11, 346),
        Hole(2, 5, 15, 446),
        Hole(3, 4, 13, 349),
        Hole(4, 4, 17, 304),
        Hole(5, 3, 9, 147),
        Hole(6, 5, 3, 511),
        Hole(7, 4, 1, 422),
        Hole(8, 3, 7, 160),
        Hole(9, 4, 5, 351),
        Hole(10, 5, 16, 492),
        Hole(11, 4, 12, 330),
        Hole(12, 5, 8, 494),
        Hole(13, 4, 4, 302),
        Hole(14, 3, 6, 183),
        Hole(15, 4, 2, 384),
        Hole(16, 4, 10, 288),
        Hole(17, 4, 18, 348),
        Hole(18, 3, 14, 148),
    ]

    whites = [
        Hole(1, 4, 11, 307),
        Hole(2, 5, 15, 441),
        Hole(3, 4, 13, 324),
        Hole(4, 4, 17, 276),
        Hole(5, 3, 9, 125),
        Hole(6, 5, 3, 456),
        Hole(7, 4, 1, 356),
        Hole(8, 3, 7, 139),
        Hole(9, 4, 5, 325),
        Hole(10, 5, 16, 448),
        Hole(11, 4, 12, 268),
        Hole(12, 5, 8, 427),
        Hole(13, 4, 4, 290),
        Hole(14, 3, 6, 168),
        Hole(15, 4, 2, 321),
        Hole(16, 4, 10, 260),
        Hole(17, 4, 18, 317),
        Hole(18, 3, 14, 131),
    ]

    create_holes(kenosee.id, "Black", 130, 72.5, blacks)
    create_holes(kenosee.id, "Blue", 130, 72.5, blues)
    create_holes(kenosee.id, "White", 125, 70.7, whites)

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
