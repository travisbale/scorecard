"""
A script to create the Dutch Legacy.

To perform the migration run the following commands:

>>> from migrations.data.courses import dutch_legacy
>>> dutch_legacy.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Dutch Legacy"""
    dutch_legacy = Course.query.filter_by(name="Dutch Legacy").first()

    if dutch_legacy is not None:
        # What happens if there are matches on the course?
        dutch_legacy.delete()

    dutch_legacy = Course("Dutch Legacy").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 126, 70.2, dutch_legacy.id).save()
    Hole(1, 4, 11, 387, dutch_legacy.id, blues_id).save()
    Hole(2, 4, 5, 418, dutch_legacy.id, blues_id).save()
    Hole(3, 4, 17, 373, dutch_legacy.id, blues_id).save()
    Hole(4, 4, 13, 340, dutch_legacy.id, blues_id).save()
    Hole(5, 4, 9, 357, dutch_legacy.id, blues_id).save()
    Hole(6, 3, 7, 183, dutch_legacy.id, blues_id).save()
    Hole(7, 4, 1, 338, dutch_legacy.id, blues_id).save()
    Hole(8, 5, 15, 602, dutch_legacy.id, blues_id).save()
    Hole(9, 3, 3, 110, dutch_legacy.id, blues_id).save()
    Hole(10, 4, 12, 402, dutch_legacy.id, blues_id).save()
    Hole(11, 3, 4, 160, dutch_legacy.id, blues_id).save()
    Hole(12, 4, 8, 417, dutch_legacy.id, blues_id).save()
    Hole(13, 4, 10, 411, dutch_legacy.id, blues_id).save()
    Hole(14, 4, 6, 445, dutch_legacy.id, blues_id).save()
    Hole(15, 3, 2, 220, dutch_legacy.id, blues_id).save()
    Hole(16, 5, 18, 491, dutch_legacy.id, blues_id).save()
    Hole(17, 3, 16, 132, dutch_legacy.id, blues_id).save()
    Hole(18, 5, 14, 515, dutch_legacy.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 132, 72.9, dutch_legacy.id).save()
    Hole(1, 4, 11, 363, dutch_legacy.id, whites_id).save()
    Hole(2, 4, 5, 348, dutch_legacy.id, whites_id).save()
    Hole(3, 4, 17, 356, dutch_legacy.id, whites_id).save()
    Hole(4, 4, 13, 299, dutch_legacy.id, whites_id).save()
    Hole(5, 4, 9, 308, dutch_legacy.id, whites_id).save()
    Hole(6, 3, 7, 173, dutch_legacy.id, whites_id).save()
    Hole(7, 4, 1, 323, dutch_legacy.id, whites_id).save()
    Hole(8, 5, 15, 550, dutch_legacy.id, whites_id).save()
    Hole(9, 3, 3, 93, dutch_legacy.id, whites_id).save()
    Hole(10, 4, 12, 382, dutch_legacy.id, whites_id).save()
    Hole(11, 3, 4, 140, dutch_legacy.id, whites_id).save()
    Hole(12, 4, 8, 332, dutch_legacy.id, whites_id).save()
    Hole(13, 4, 10, 355, dutch_legacy.id, whites_id).save()
    Hole(14, 4, 6, 427, dutch_legacy.id, whites_id).save()
    Hole(15, 3, 2, 157, dutch_legacy.id, whites_id).save()
    Hole(16, 5, 18, 473, dutch_legacy.id, whites_id).save()
    Hole(17, 3, 16, 115, dutch_legacy.id, whites_id).save()
    Hole(18, 5, 14, 479, dutch_legacy.id, whites_id).save()

    db.session.commit()
