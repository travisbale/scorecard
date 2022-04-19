"""
A script to create the Carmen Golf & Curling Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import carmen
>>> carmen.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Carmen Golf & Curling Club"""
    carmen = Course.query.filter_by(name="Carmen Golf & Curling Club").first()

    if carmen is not None:
        # What happens if there are matches on the course?
        carmen.delete()

    carmen = Course("Carmen Golf & Curling Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 111, 68.6, carmen.id).save()
    Hole(1, 4, 3, 390, carmen.id, blues_id).save()
    Hole(2, 4, 1, 417, carmen.id, blues_id).save()
    Hole(3, 4, 11, 341, carmen.id, blues_id).save()
    Hole(4, 5, 5, 487, carmen.id, blues_id).save()
    Hole(5, 4, 7, 339, carmen.id, blues_id).save()
    Hole(6, 3, 13, 171, carmen.id, blues_id).save()
    Hole(7, 4, 17, 293, carmen.id, blues_id).save()
    Hole(8, 3, 15, 189, carmen.id, blues_id).save()
    Hole(9, 4, 9, 320, carmen.id, blues_id).save()
    Hole(10, 4, 10, 298, carmen.id, blues_id).save()
    Hole(11, 4, 14, 334, carmen.id, blues_id).save()
    Hole(12, 4, 6, 352, carmen.id, blues_id).save()
    Hole(13, 4, 16, 280, carmen.id, blues_id).save()
    Hole(14, 5, 2, 517, carmen.id, blues_id).save()
    Hole(15, 4, 8, 367, carmen.id, blues_id).save()
    Hole(16, 3, 12, 212, carmen.id, blues_id).save()
    Hole(17, 4, 4, 384, carmen.id, blues_id).save()
    Hole(18, 4, 18, 278, carmen.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 109, 67.8, carmen.id).save()
    Hole(1, 4, 3, 374, carmen.id, whites_id).save()
    Hole(2, 4, 1, 404, carmen.id, whites_id).save()
    Hole(3, 4, 11, 334, carmen.id, whites_id).save()
    Hole(4, 5, 5, 480, carmen.id, whites_id).save()
    Hole(5, 4, 7, 331, carmen.id, whites_id).save()
    Hole(6, 3, 13, 162, carmen.id, whites_id).save()
    Hole(7, 4, 17, 281, carmen.id, whites_id).save()
    Hole(8, 3, 15, 169, carmen.id, whites_id).save()
    Hole(9, 4, 9, 300, carmen.id, whites_id).save()
    Hole(10, 4, 10, 291, carmen.id, whites_id).save()
    Hole(11, 4, 14, 327, carmen.id, whites_id).save()
    Hole(12, 4, 6, 335, carmen.id, whites_id).save()
    Hole(13, 4, 16, 270, carmen.id, whites_id).save()
    Hole(14, 5, 2, 502, carmen.id, whites_id).save()
    Hole(15, 4, 8, 367, carmen.id, whites_id).save()
    Hole(16, 3, 12, 202, carmen.id, whites_id).save()
    Hole(17, 4, 4, 373, carmen.id, whites_id).save()
    Hole(18, 4, 18, 271, carmen.id, whites_id).save()

    db.session.commit()
