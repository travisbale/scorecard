"""
A script to create the Quarry Oaks.

To perform the migration run the following commands:

>>> from migrations.data.courses import quarry_oaks
>>> quarry_oaks.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Quarry Oaks"""
    quarry = Course.query.filter_by(name="Quarry Oaks").first()

    if quarry is not None:
        # What happens if there are matches on the course?
        quarry.delete()

    quarry = Course("Quarry Oaks").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 126, 71.6, quarry.id).save()
    Hole(1, 4, 11, 361, quarry.id, blues_id).save()
    Hole(2, 5, 1, 583, quarry.id, blues_id).save()
    Hole(3, 3, 7, 162, quarry.id, blues_id).save()
    Hole(4, 4, 13, 350, quarry.id, blues_id).save()
    Hole(5, 3, 15, 164, quarry.id, blues_id).save()
    Hole(6, 4, 5, 356, quarry.id, blues_id).save()
    Hole(7, 5, 9, 486, quarry.id, blues_id).save()
    Hole(8, 3, 17, 122, quarry.id, blues_id).save()
    Hole(9, 5, 3, 513, quarry.id, blues_id).save()
    Hole(10, 4, 6, 408, quarry.id, blues_id).save()
    Hole(11, 3, 12, 203, quarry.id, blues_id).save()
    Hole(12, 4, 14, 415, quarry.id, blues_id).save()
    Hole(13, 5, 8, 548, quarry.id, blues_id).save()
    Hole(14, 4, 10, 382, quarry.id, blues_id).save()
    Hole(15, 3, 4, 167, quarry.id, blues_id).save()
    Hole(16, 4, 16, 419, quarry.id, blues_id).save()
    Hole(17, 4, 2, 365, quarry.id, blues_id).save()
    Hole(18, 5, 18, 492, quarry.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 122, 69.2, quarry.id).save()
    Hole(1, 4, 11, 334, quarry.id, whites_id).save()
    Hole(2, 5, 1, 553, quarry.id, whites_id).save()
    Hole(3, 3, 7, 148, quarry.id, whites_id).save()
    Hole(4, 4, 13, 316, quarry.id, whites_id).save()
    Hole(5, 3, 15, 143, quarry.id, whites_id).save()
    Hole(6, 4, 5, 316, quarry.id, whites_id).save()
    Hole(7, 5, 9, 446, quarry.id, whites_id).save()
    Hole(8, 3, 17, 103, quarry.id, whites_id).save()
    Hole(9, 5, 3, 447, quarry.id, whites_id).save()
    Hole(10, 4, 6, 379, quarry.id, whites_id).save()
    Hole(11, 3, 12, 137, quarry.id, whites_id).save()
    Hole(12, 4, 14, 385, quarry.id, whites_id).save()
    Hole(13, 5, 8, 487, quarry.id, whites_id).save()
    Hole(14, 4, 10, 360, quarry.id, whites_id).save()
    Hole(15, 3, 4, 176, quarry.id, whites_id).save()
    Hole(16, 4, 16, 395, quarry.id, whites_id).save()
    Hole(17, 4, 2, 339, quarry.id, whites_id).save()
    Hole(18, 5, 18, 459, quarry.id, whites_id).save()

    db.session.commit()
