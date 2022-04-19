"""
A script to create the Lehman Legacy.

To perform the migration run the following commands:

>>> from migrations.data.courses import lehman_legacy
>>> lehman_legacy.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Lehman Legacy"""
    lehman_legacy = Course.query.filter_by(name="Lehman Legacy").first()

    if lehman_legacy is not None:
        # What happens if there are matches on the course?
        lehman_legacy.delete()

    lehman_legacy = Course("Lehman Legacy").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 126, 70.2, lehman_legacy.id).save()
    Hole(1, 4, 11, 360, lehman_legacy.id, blues_id).save()
    Hole(2, 5, 5, 543, lehman_legacy.id, blues_id).save()
    Hole(3, 3, 17, 203, lehman_legacy.id, blues_id).save()
    Hole(4, 5, 13, 539, lehman_legacy.id, blues_id).save()
    Hole(5, 4, 9, 327, lehman_legacy.id, blues_id).save()
    Hole(6, 3, 7, 147, lehman_legacy.id, blues_id).save()
    Hole(7, 4, 1, 420, lehman_legacy.id, blues_id).save()
    Hole(8, 5, 15, 478, lehman_legacy.id, blues_id).save()
    Hole(9, 4, 3, 402, lehman_legacy.id, blues_id).save()
    Hole(10, 4, 12, 407, lehman_legacy.id, blues_id).save()
    Hole(11, 4, 4, 373, lehman_legacy.id, blues_id).save()
    Hole(12, 3, 8, 150, lehman_legacy.id, blues_id).save()
    Hole(13, 5, 10, 540, lehman_legacy.id, blues_id).save()
    Hole(14, 3, 6, 193, lehman_legacy.id, blues_id).save()
    Hole(15, 4, 2, 210, lehman_legacy.id, blues_id).save()
    Hole(16, 4, 18, 353, lehman_legacy.id, blues_id).save()
    Hole(17, 5, 16, 474, lehman_legacy.id, blues_id).save()
    Hole(18, 4, 14, 383, lehman_legacy.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 132, 72.9, lehman_legacy.id).save()
    Hole(1, 4, 11, 337, lehman_legacy.id, whites_id).save()
    Hole(2, 5, 5, 505, lehman_legacy.id, whites_id).save()
    Hole(3, 3, 17, 185, lehman_legacy.id, whites_id).save()
    Hole(4, 5, 13, 522, lehman_legacy.id, whites_id).save()
    Hole(5, 4, 9, 306, lehman_legacy.id, whites_id).save()
    Hole(6, 3, 7, 130, lehman_legacy.id, whites_id).save()
    Hole(7, 4, 1, 361, lehman_legacy.id, whites_id).save()
    Hole(8, 5, 15, 473, lehman_legacy.id, whites_id).save()
    Hole(9, 4, 3, 393, lehman_legacy.id, whites_id).save()
    Hole(10, 4, 12, 367, lehman_legacy.id, whites_id).save()
    Hole(11, 4, 4, 330, lehman_legacy.id, whites_id).save()
    Hole(12, 3, 8, 132, lehman_legacy.id, whites_id).save()
    Hole(13, 5, 10, 513, lehman_legacy.id, whites_id).save()
    Hole(14, 3, 6, 178, lehman_legacy.id, whites_id).save()
    Hole(15, 4, 2, 301, lehman_legacy.id, whites_id).save()
    Hole(16, 4, 18, 333, lehman_legacy.id, whites_id).save()
    Hole(17, 5, 16, 463, lehman_legacy.id, whites_id).save()
    Hole(18, 4, 14, 360, lehman_legacy.id, whites_id).save()

    db.session.commit()
