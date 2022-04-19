"""
A script to create the Clear Lake Golf Course.

To perform the migration run the following commands:

>>> from migrations.data.courses import clear_lake
>>> clear_lake.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Clear Lake Golf Course"""
    clear_lake = Course.query.filter_by(name="Clear Lake Golf Course").first()

    if clear_lake is not None:
        # What happens if there are matches on the course?
        clear_lake.delete()

    clear_lake = Course("Clear Lake Golf Course").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 121, 69.9, clear_lake.id).save()
    Hole(1, 4, 11, 289, clear_lake.id, blues_id).save()
    Hole(2, 4, 7, 447, clear_lake.id, blues_id).save()
    Hole(3, 3, 17, 127, clear_lake.id, blues_id).save()
    Hole(4, 5, 3, 520, clear_lake.id, blues_id).save()
    Hole(5, 5, 9, 485, clear_lake.id, blues_id).save()
    Hole(6, 3, 15, 180, clear_lake.id, blues_id).save()
    Hole(7, 4, 1, 445, clear_lake.id, blues_id).save()
    Hole(8, 4, 13, 288, clear_lake.id, blues_id).save()
    Hole(9, 4, 5, 334, clear_lake.id, blues_id).save()
    Hole(10, 4, 4, 362, clear_lake.id, blues_id).save()
    Hole(11, 4, 12, 369, clear_lake.id, blues_id).save()
    Hole(12, 3, 14, 160, clear_lake.id, blues_id).save()
    Hole(13, 5, 2, 545, clear_lake.id, blues_id).save()
    Hole(14, 5, 6, 560, clear_lake.id, blues_id).save()
    Hole(15, 4, 8, 448, clear_lake.id, blues_id).save()
    Hole(16, 4, 18, 268, clear_lake.id, blues_id).save()
    Hole(17, 3, 16, 115, clear_lake.id, blues_id).save()
    Hole(18, 4, 10, 367, clear_lake.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 116, 69.0, clear_lake.id).save()
    Hole(1, 4, 11, 227, clear_lake.id, whites_id).save()
    Hole(2, 4, 7, 431, clear_lake.id, whites_id).save()
    Hole(3, 3, 17, 119, clear_lake.id, whites_id).save()
    Hole(4, 5, 3, 485, clear_lake.id, whites_id).save()
    Hole(5, 5, 9, 465, clear_lake.id, whites_id).save()
    Hole(6, 3, 15, 165, clear_lake.id, whites_id).save()
    Hole(7, 4, 1, 430, clear_lake.id, whites_id).save()
    Hole(8, 4, 13, 280, clear_lake.id, whites_id).save()
    Hole(9, 4, 5, 324, clear_lake.id, whites_id).save()
    Hole(10, 4, 4, 350, clear_lake.id, whites_id).save()
    Hole(11, 4, 12, 346, clear_lake.id, whites_id).save()
    Hole(12, 3, 14, 138, clear_lake.id, whites_id).save()
    Hole(13, 5, 2, 530, clear_lake.id, whites_id).save()
    Hole(14, 5, 6, 550, clear_lake.id, whites_id).save()
    Hole(15, 4, 8, 433, clear_lake.id, whites_id).save()
    Hole(16, 4, 18, 258, clear_lake.id, whites_id).save()
    Hole(17, 3, 16, 102, clear_lake.id, whites_id).save()
    Hole(18, 4, 10, 330, clear_lake.id, whites_id).save()

    db.session.commit()
