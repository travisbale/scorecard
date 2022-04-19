"""
A script to create the Pinawa Golf & Country Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import pinawa
>>> pinawa.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Pinawa Golf & Country Club"""
    pinawa = Course.query.filter_by(name="Pinawa Golf & Country Club").first()

    if pinawa is not None:
        # What happens if there are matches on the course?
        pinawa.delete()

    pinawa = Course("Pinawa Golf & Country Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 130, 72.7, pinawa.id).save()
    Hole(1, 4, 3, 432, pinawa.id, blues_id).save()
    Hole(2, 4, 11, 384, pinawa.id, blues_id).save()
    Hole(3, 4, 13, 363, pinawa.id, blues_id).save()
    Hole(4, 3, 17, 200, pinawa.id, blues_id).save()
    Hole(5, 5, 1, 472, pinawa.id, blues_id).save()
    Hole(6, 3, 15, 215, pinawa.id, blues_id).save()
    Hole(7, 5, 5, 474, pinawa.id, blues_id).save()
    Hole(8, 4, 7, 343, pinawa.id, blues_id).save()
    Hole(9, 4, 9, 332, pinawa.id, blues_id).save()
    Hole(10, 3, 18, 168, pinawa.id, blues_id).save()
    Hole(11, 4, 4, 415, pinawa.id, blues_id).save()
    Hole(12, 4, 2, 411, pinawa.id, blues_id).save()
    Hole(13, 3, 16, 225, pinawa.id, blues_id).save()
    Hole(14, 4, 10, 403, pinawa.id, blues_id).save()
    Hole(15, 5, 8, 535, pinawa.id, blues_id).save()
    Hole(16, 4, 14, 338, pinawa.id, blues_id).save()
    Hole(17, 5, 6, 525, pinawa.id, blues_id).save()
    Hole(18, 4, 12, 354, pinawa.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 129, 71.1, pinawa.id).save()
    Hole(1, 4, 3, 426, pinawa.id, whites_id).save()
    Hole(2, 4, 11, 379, pinawa.id, whites_id).save()
    Hole(3, 4, 13, 358, pinawa.id, whites_id).save()
    Hole(4, 3, 17, 165, pinawa.id, whites_id).save()
    Hole(5, 5, 1, 462, pinawa.id, whites_id).save()
    Hole(6, 3, 15, 210, pinawa.id, whites_id).save()
    Hole(7, 5, 5, 470, pinawa.id, whites_id).save()
    Hole(8, 4, 7, 338, pinawa.id, whites_id).save()
    Hole(9, 4, 9, 327, pinawa.id, whites_id).save()
    Hole(10, 3, 18, 162, pinawa.id, whites_id).save()
    Hole(11, 4, 4, 375, pinawa.id, whites_id).save()
    Hole(12, 4, 2, 377, pinawa.id, whites_id).save()
    Hole(13, 3, 16, 182, pinawa.id, whites_id).save()
    Hole(14, 4, 10, 371, pinawa.id, whites_id).save()
    Hole(15, 5, 8, 509, pinawa.id, whites_id).save()
    Hole(16, 4, 14, 309, pinawa.id, whites_id).save()
    Hole(17, 5, 6, 510, pinawa.id, whites_id).save()
    Hole(18, 4, 12, 340, pinawa.id, whites_id).save()

    db.session.commit()
