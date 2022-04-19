"""
A script to create the Killarney Lakeside Golf Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import killarney
>>> killarney.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Killarney Lakeside Golf Club"""
    killarney = Course.query.filter_by(name="Killarney Lakeside Golf Club").first()

    if killarney is not None:
        # What happens if there are matches on the course?
        killarney.delete()

    killarney = Course("Killarney Lakeside Golf Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 119, 70.8, killarney.id).save()
    Hole(1, 5, 11, 482, killarney.id, blues_id).save()
    Hole(2, 4, 5, 364, killarney.id, blues_id).save()
    Hole(3, 4, 17, 419, killarney.id, blues_id).save()
    Hole(4, 3, 13, 174, killarney.id, blues_id).save()
    Hole(5, 4, 9, 370, killarney.id, blues_id).save()
    Hole(6, 4, 7, 370, killarney.id, blues_id).save()
    Hole(7, 3, 1, 202, killarney.id, blues_id).save()
    Hole(8, 5, 15, 541, killarney.id, blues_id).save()
    Hole(9, 4, 3, 295, killarney.id, blues_id).save()
    Hole(10, 3, 12, 227, killarney.id, blues_id).save()
    Hole(11, 4, 4, 342, killarney.id, blues_id).save()
    Hole(12, 4, 8, 330, killarney.id, blues_id).save()
    Hole(13, 3, 10, 218, killarney.id, blues_id).save()
    Hole(14, 5, 6, 483, killarney.id, blues_id).save()
    Hole(15, 4, 2, 337, killarney.id, blues_id).save()
    Hole(16, 4, 18, 382, killarney.id, blues_id).save()
    Hole(17, 4, 16, 323, killarney.id, blues_id).save()
    Hole(18, 4, 14, 321, killarney.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 132, 72.9, killarney.id).save()
    Hole(1, 5, 11, 462, killarney.id, whites_id).save()
    Hole(2, 4, 5, 350, killarney.id, whites_id).save()
    Hole(3, 4, 17, 395, killarney.id, whites_id).save()
    Hole(4, 3, 13, 150, killarney.id, whites_id).save()
    Hole(5, 4, 9, 346, killarney.id, whites_id).save()
    Hole(6, 4, 7, 360, killarney.id, whites_id).save()
    Hole(7, 3, 1, 185, killarney.id, whites_id).save()
    Hole(8, 5, 15, 513, killarney.id, whites_id).save()
    Hole(9, 4, 3, 276, killarney.id, whites_id).save()
    Hole(10, 3, 12, 212, killarney.id, whites_id).save()
    Hole(11, 4, 4, 335, killarney.id, whites_id).save()
    Hole(12, 4, 8, 321, killarney.id, whites_id).save()
    Hole(13, 3, 10, 206, killarney.id, whites_id).save()
    Hole(14, 5, 6, 466, killarney.id, whites_id).save()
    Hole(15, 4, 2, 327, killarney.id, whites_id).save()
    Hole(16, 4, 18, 315, killarney.id, whites_id).save()
    Hole(17, 4, 16, 304, killarney.id, whites_id).save()
    Hole(18, 4, 14, 273, killarney.id, whites_id).save()

    db.session.commit()
