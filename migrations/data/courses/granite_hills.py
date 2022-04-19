"""
A script to create the Granite Hills Golf Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import granite_hills
>>> granite_hills.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Granite Hills Golf Club"""
    granite_hills = Course.query.filter_by(name="Granite Hills Golf Club").first()

    if granite_hills is not None:
        # What happens if there are matches on the course?
        granite_hills.delete()

    granite_hills = Course("Granite Hills Golf Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 121, 69.9, granite_hills.id).save()
    Hole(1, 4, 7, 404, granite_hills.id, blues_id).save()
    Hole(2, 4, 15, 402, granite_hills.id, blues_id).save()
    Hole(3, 5, 1, 496, granite_hills.id, blues_id).save()
    Hole(4, 3, 11, 199, granite_hills.id, blues_id).save()
    Hole(5, 4, 13, 401, granite_hills.id, blues_id).save()
    Hole(6, 3, 3, 207, granite_hills.id, blues_id).save()
    Hole(7, 4, 9, 408, granite_hills.id, blues_id).save()
    Hole(8, 4, 17, 323, granite_hills.id, blues_id).save()
    Hole(9, 5, 5, 519, granite_hills.id, blues_id).save()
    Hole(10, 5, 4, 560, granite_hills.id, blues_id).save()
    Hole(11, 4, 2, 408, granite_hills.id, blues_id).save()
    Hole(12, 3, 14, 176, granite_hills.id, blues_id).save()
    Hole(13, 4, 6, 406, granite_hills.id, blues_id).save()
    Hole(14, 4, 12, 338, granite_hills.id, blues_id).save()
    Hole(15, 5, 10, 500, granite_hills.id, blues_id).save()
    Hole(16, 4, 8, 351, granite_hills.id, blues_id).save()
    Hole(17, 3, 18, 159, granite_hills.id, blues_id).save()
    Hole(18, 4, 16, 385, granite_hills.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 116, 69.0, granite_hills.id).save()
    Hole(1, 4, 7, 390, granite_hills.id, whites_id).save()
    Hole(2, 4, 15, 390, granite_hills.id, whites_id).save()
    Hole(3, 5, 1, 449, granite_hills.id, whites_id).save()
    Hole(4, 3, 11, 171, granite_hills.id, whites_id).save()
    Hole(5, 4, 13, 363, granite_hills.id, whites_id).save()
    Hole(6, 3, 3, 177, granite_hills.id, whites_id).save()
    Hole(7, 4, 9, 393, granite_hills.id, whites_id).save()
    Hole(8, 4, 17, 297, granite_hills.id, whites_id).save()
    Hole(9, 5, 5, 475, granite_hills.id, whites_id).save()
    Hole(10, 5, 4, 513, granite_hills.id, whites_id).save()
    Hole(11, 4, 2, 396, granite_hills.id, whites_id).save()
    Hole(12, 3, 14, 154, granite_hills.id, whites_id).save()
    Hole(13, 4, 6, 383, granite_hills.id, whites_id).save()
    Hole(14, 4, 12, 282, granite_hills.id, whites_id).save()
    Hole(15, 5, 10, 482, granite_hills.id, whites_id).save()
    Hole(16, 4, 8, 351, granite_hills.id, whites_id).save()
    Hole(17, 3, 18, 132, granite_hills.id, whites_id).save()
    Hole(18, 4, 16, 336, granite_hills.id, whites_id).save()

    db.session.commit()
