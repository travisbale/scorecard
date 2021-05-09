"""A script to create Southwood Golf & Country Club."""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create southwood."""
    southwood = Course.query.filter_by(name="Southwood Golf & Country Club").first()

    if southwood is not None:
        southwood.delete()

    southwood = Course("Southwood Golf & Country Club")
    southwood.save()

    blacks = [
        Hole(1, 4, 3, 475),
        Hole(2, 3, 11, 215),
        Hole(3, 4, 5, 416),
        Hole(4, 5, 7, 531),
        Hole(5, 4, 15, 354),
        Hole(6, 4, 1, 481),
        Hole(7, 5, 13, 576),
        Hole(8, 3, 17, 180),
        Hole(9, 4, 9, 438),
        Hole(10, 4, 2, 484),
        Hole(11, 3, 10, 228),
        Hole(12, 4, 16, 370),
        Hole(13, 4, 4, 398),
        Hole(14, 5, 14, 540),
        Hole(15, 4, 8, 446),
        Hole(16, 4, 6, 454),
        Hole(17, 3, 18, 166),
        Hole(18, 5, 12, 559),
    ]

    golds = [
        Hole(1, 4, 3, 431),
        Hole(2, 3, 11, 194),
        Hole(3, 4, 5, 390),
        Hole(4, 5, 7, 505),
        Hole(5, 4, 15, 327),
        Hole(6, 4, 1, 431),
        Hole(7, 5, 13, 542),
        Hole(8, 3, 17, 153),
        Hole(9, 4, 9, 411),
        Hole(10, 4, 2, 451),
        Hole(11, 3, 10, 201),
        Hole(12, 4, 16, 346),
        Hole(13, 4, 4, 367),
        Hole(14, 5, 14, 513),
        Hole(15, 4, 8, 419),
        Hole(16, 4, 6, 427),
        Hole(17, 3, 18, 155),
        Hole(18, 5, 12, 515),
    ]

    blues = [
        Hole(1, 4, 3, 421),
        Hole(2, 3, 11, 158),
        Hole(3, 4, 5, 366),
        Hole(4, 5, 7, 497),
        Hole(5, 4, 15, 316),
        Hole(6, 4, 1, 418),
        Hole(7, 5, 13, 531),
        Hole(8, 3, 17, 146),
        Hole(9, 4, 9, 391),
        Hole(10, 4, 2, 423),
        Hole(11, 3, 10, 176),
        Hole(12, 4, 16, 320),
        Hole(13, 4, 4, 340),
        Hole(14, 5, 14, 490),
        Hole(15, 4, 8, 396),
        Hole(16, 4, 6, 417),
        Hole(17, 3, 18, 130),
        Hole(18, 5, 12, 475),
    ]

    whites = [
        Hole(1, 4, 3, 379),
        Hole(2, 3, 11, 150),
        Hole(3, 4, 5, 343),
        Hole(4, 5, 7, 285),
        Hole(5, 4, 15, 367),
        Hole(6, 4, 1, 489),
        Hole(7, 5, 13, 126),
        Hole(8, 3, 17, 364),
        Hole(9, 4, 9, 297),
        Hole(10, 4, 2, 392),
        Hole(11, 3, 10, 152),
        Hole(12, 4, 16, 295),
        Hole(13, 4, 4, 307),
        Hole(14, 5, 14, 464),
        Hole(15, 4, 8, 390),
        Hole(16, 4, 6, 385),
        Hole(17, 3, 18, 130),
        Hole(18, 5, 12, 468),
    ]

    greens = [
        Hole(1, 4, 3, 351),
        Hole(2, 3, 11, 130),
        Hole(3, 4, 5, 267),
        Hole(4, 5, 7, 404),
        Hole(5, 4, 15, 249),
        Hole(6, 4, 1, 341),
        Hole(7, 5, 13, 446),
        Hole(8, 3, 17, 103),
        Hole(9, 4, 9, 337),
        Hole(10, 4, 2, 363),
        Hole(11, 3, 10, 138),
        Hole(12, 4, 16, 226),
        Hole(13, 4, 4, 262),
        Hole(14, 5, 14, 418),
        Hole(15, 4, 8, 326),
        Hole(16, 4, 6, 358),
        Hole(17, 3, 18, 112),
        Hole(18, 5, 12, 443),
    ]

    create_holes(southwood.id, "Black", 136, 75.4, blacks)
    create_holes(southwood.id, "Gold", 130, 72.5, golds)
    create_holes(southwood.id, "Blue", 130, 72.5, blues)
    create_holes(southwood.id, "White", 125, 70.7, whites)
    create_holes(southwood.id, "Green", 118, 68.8, greens)

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
