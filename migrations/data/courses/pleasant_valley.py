"""
A script to create the Pleasant Valley Golf Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import pleasant_valley
>>> pleasant_valley.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Pleasant Valley Golf Club"""
    pv = Course.query.filter_by(name="Pleasant Valley Golf Club").first()

    if pv is not None:
        # What happens if there are matches on the course?
        pv.delete()

    pv = Course("Pleasant Valley Golf Club").save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 114, 70.3, pv.id).save()
    Hole(1, 5, 9, 430, pv.id, whites_id).save()
    Hole(2, 3, 1, 245, pv.id, whites_id).save()
    Hole(3, 3, 5, 210, pv.id, whites_id).save()
    Hole(4, 4, 7, 385, pv.id, whites_id).save()
    Hole(5, 4, 15, 310, pv.id, whites_id).save()
    Hole(6, 4, 13, 290, pv.id, whites_id).save()
    Hole(7, 4, 11, 365, pv.id, whites_id).save()
    Hole(8, 5, 3, 530, pv.id, whites_id).save()
    Hole(9, 4, 17, 280, pv.id, whites_id).save()
    Hole(10, 4, 12, 375, pv.id, whites_id).save()
    Hole(11, 3, 18, 160, pv.id, whites_id).save()
    Hole(12, 4, 6, 365, pv.id, whites_id).save()
    Hole(13, 4, 2, 385, pv.id, whites_id).save()
    Hole(14, 4, 14, 255, pv.id, whites_id).save()
    Hole(15, 3, 16, 135, pv.id, whites_id).save()
    Hole(16, 4, 4, 355, pv.id, whites_id).save()
    Hole(17, 5, 8, 465, pv.id, whites_id).save()
    Hole(18, 4, 10, 385, pv.id, whites_id).save()

    db.session.commit()
