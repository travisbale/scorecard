"""A script to create Rossmere Golf & Country Club."""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create rossmere."""
    rossmere = Course.query.filter_by(name="Rossmere Golf & Country Club").first()

    if rossmere is not None:
        rossmere.delete()

    rossmere = Course("Rossmere Golf & Country Club")
    rossmere.save()

    blues = [
        Hole(1, 5, 1, 529),
        Hole(2, 4, 11, 348),
        Hole(3, 3, 15, 187),
        Hole(4, 4, 9, 452),
        Hole(5, 3, 17, 170),
        Hole(6, 4, 13, 406),
        Hole(7, 4, 7, 436),
        Hole(8, 5, 5, 531),
        Hole(9, 4, 3, 418),
        Hole(10, 4, 14, 369),
        Hole(11, 4, 2, 470),
        Hole(12, 3, 18, 170),
        Hole(13, 4, 10, 356),
        Hole(14, 3, 6, 220),
        Hole(15, 4, 4, 335),
        Hole(16, 5, 12, 490),
        Hole(17, 3, 16, 172),
        Hole(18, 4, 8, 393),
    ]

    whites = [
        Hole(1, 5, 1, 513),
        Hole(2, 4, 11, 338),
        Hole(3, 3, 15, 172),
        Hole(4, 4, 9, 444),
        Hole(5, 3, 17, 156),
        Hole(6, 4, 13, 394),
        Hole(7, 4, 7, 424),
        Hole(8, 5, 5, 514),
        Hole(9, 4, 3, 396),
        Hole(10, 4, 14, 358),
        Hole(11, 4, 2, 460),
        Hole(12, 3, 18, 160),
        Hole(13, 4, 10, 347),
        Hole(14, 3, 6, 215),
        Hole(15, 4, 4, 325),
        Hole(16, 5, 12, 482),
        Hole(17, 3, 16, 154),
        Hole(18, 4, 8, 383),
    ]

    yellows = [
        Hole(1, 4, 1, 438),
        Hole(2, 4, 11, 315),
        Hole(3, 3, 15, 143),
        Hole(4, 4, 9, 436),
        Hole(5, 3, 17, 144),
        Hole(6, 4, 13, 342),
        Hole(7, 4, 7, 412),
        Hole(8, 5, 5, 497),
        Hole(9, 4, 3, 345),
        Hole(10, 4, 14, 348),
        Hole(11, 4, 2, 410),
        Hole(12, 3, 18, 145),
        Hole(13, 4, 10, 388),
        Hole(14, 3, 6, 196),
        Hole(15, 4, 4, 315),
        Hole(16, 5, 12, 477),
        Hole(17, 3, 16, 141),
        Hole(18, 4, 8, 373),
    ]

    create_holes(rossmere.id, "Blue", 128, 71.1, blues)
    create_holes(rossmere.id, "White", 127, 70.1, whites)
    create_holes(rossmere.id, "Yellow", 122, 68.4, yellows)

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
