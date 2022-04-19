"""
A script to create the Giants Ridge - Quarry.

To perform the migration run the following commands:

>>> from migrations.data.courses import giants_ridge_quarry
>>> giants_ridge_quarry.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Giants Ridge - Quarry"""
    quarry = Course.query.filter_by(name="Giants Ridge - Quarry").first()

    if quarry is not None:
        # What happens if there are matches on the course?
        quarry.delete()

    quarry = Course("Giants Ridge - Quarry").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 132, 72.9, quarry.id).save()
    Hole(1, 4, 7, 409, quarry.id, blues_id).save()
    Hole(2, 5, 3, 558, quarry.id, blues_id).save()
    Hole(3, 4, 5, 405, quarry.id, blues_id).save()
    Hole(4, 3, 13, 228, quarry.id, blues_id).save()
    Hole(5, 5, 9, 485, quarry.id, blues_id).save()
    Hole(6, 4, 11, 346, quarry.id, blues_id).save()
    Hole(7, 3, 15, 175, quarry.id, blues_id).save()
    Hole(8, 4, 1, 455, quarry.id, blues_id).save()
    Hole(9, 4, 17, 353, quarry.id, blues_id).save()
    Hole(10, 4, 18, 347, quarry.id, blues_id).save()
    Hole(11, 3, 16, 142, quarry.id, blues_id).save()
    Hole(12, 4, 2, 436, quarry.id, blues_id).save()
    Hole(13, 4, 14, 296, quarry.id, blues_id).save()
    Hole(14, 5, 8, 499, quarry.id, blues_id).save()
    Hole(15, 4, 4, 431, quarry.id, blues_id).save()
    Hole(16, 5, 10, 502, quarry.id, blues_id).save()
    Hole(17, 3, 12, 181, quarry.id, blues_id).save()
    Hole(18, 4, 6, 488, quarry.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 126, 70.2, quarry.id).save()
    Hole(1, 4, 7, 381, quarry.id, whites_id).save()
    Hole(2, 5, 3, 525, quarry.id, whites_id).save()
    Hole(3, 4, 5, 353, quarry.id, whites_id).save()
    Hole(4, 3, 13, 188, quarry.id, whites_id).save()
    Hole(5, 5, 9, 465, quarry.id, whites_id).save()
    Hole(6, 4, 11, 313, quarry.id, whites_id).save()
    Hole(7, 3, 15, 142, quarry.id, whites_id).save()
    Hole(8, 4, 1, 424, quarry.id, whites_id).save()
    Hole(9, 4, 17, 325, quarry.id, whites_id).save()
    Hole(10, 4, 18, 305, quarry.id, whites_id).save()
    Hole(11, 3, 16, 121, quarry.id, whites_id).save()
    Hole(12, 4, 2, 395, quarry.id, whites_id).save()
    Hole(13, 4, 14, 275, quarry.id, whites_id).save()
    Hole(14, 5, 8, 454, quarry.id, whites_id).save()
    Hole(15, 4, 4, 398, quarry.id, whites_id).save()
    Hole(16, 5, 10, 473, quarry.id, whites_id).save()
    Hole(17, 3, 12, 156, quarry.id, whites_id).save()
    Hole(18, 4, 6, 408, quarry.id, whites_id).save()

    db.session.commit()
