"""
A script to create the Lake of the Sandhills golf course.

To perform the migration run the following commands:

>>> from migrations.data.courses import beauty_bay
>>> beauty_bay.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Beauty Bay Golf Course"""
    beauty_bay = Course.query.filter_by(name="Beauty Bay Golf Course").first()

    if beauty_bay is not None:
        # What happens if there are matches on the course?
        beauty_bay.delete()

    beauty_bay = Course("Beauty Bay Golf Course").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 127, 69.1, beauty_bay.id).save()
    Hole(1, 4, 15, 332, beauty_bay.id, blues_id).save()
    Hole(2, 3, 17, 142, beauty_bay.id, blues_id).save()
    Hole(3, 5, 1, 542, beauty_bay.id, blues_id).save()
    Hole(4, 4, 13, 376, beauty_bay.id, blues_id).save()
    Hole(5, 4, 11, 390, beauty_bay.id, blues_id).save()
    Hole(6, 4, 3, 400, beauty_bay.id, blues_id).save()
    Hole(7, 3, 9, 194, beauty_bay.id, blues_id).save()
    Hole(8, 5, 7, 604, beauty_bay.id, blues_id).save()
    Hole(9, 3, 5, 186, beauty_bay.id, blues_id).save()
    Hole(10, 4, 10, 268, beauty_bay.id, blues_id).save()
    Hole(11, 4, 14, 325, beauty_bay.id, blues_id).save()
    Hole(12, 4, 12, 314, beauty_bay.id, blues_id).save()
    Hole(13, 4, 16, 309, beauty_bay.id, blues_id).save()
    Hole(14, 3, 2, 124, beauty_bay.id, blues_id).save()
    Hole(15, 4, 8, 372, beauty_bay.id, blues_id).save()
    Hole(16, 4, 6, 324, beauty_bay.id, blues_id).save()
    Hole(17, 4, 4, 358, beauty_bay.id, blues_id).save()
    Hole(18, 4, 18, 454, beauty_bay.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 122, 67.6, beauty_bay.id).save()
    Hole(1, 4, 15, 324, beauty_bay.id, whites_id).save()
    Hole(2, 3, 17, 125, beauty_bay.id, whites_id).save()
    Hole(3, 5, 1, 489, beauty_bay.id, whites_id).save()
    Hole(4, 4, 13, 360, beauty_bay.id, whites_id).save()
    Hole(5, 4, 11, 376, beauty_bay.id, whites_id).save()
    Hole(6, 4, 3, 392, beauty_bay.id, whites_id).save()
    Hole(7, 3, 9, 180, beauty_bay.id, whites_id).save()
    Hole(8, 5, 7, 538, beauty_bay.id, whites_id).save()
    Hole(9, 3, 5, 163, beauty_bay.id, whites_id).save()
    Hole(10, 4, 10, 256, beauty_bay.id, whites_id).save()
    Hole(11, 4, 14, 316, beauty_bay.id, whites_id).save()
    Hole(12, 4, 12, 306, beauty_bay.id, whites_id).save()
    Hole(13, 4, 16, 289, beauty_bay.id, whites_id).save()
    Hole(14, 3, 2, 116, beauty_bay.id, whites_id).save()
    Hole(15, 4, 8, 356, beauty_bay.id, whites_id).save()
    Hole(16, 4, 6, 315, beauty_bay.id, whites_id).save()
    Hole(17, 4, 4, 340, beauty_bay.id, whites_id).save()
    Hole(18, 4, 18, 434, beauty_bay.id, whites_id).save()

    reds_id = TeeColor.query.filter_by(color="Red").first().id
    TeeSet(reds_id, 114, 64.6, beauty_bay.id).save()
    Hole(1, 4, 15, 318, beauty_bay.id, reds_id).save()
    Hole(2, 3, 17, 112, beauty_bay.id, reds_id).save()
    Hole(3, 5, 1, 447, beauty_bay.id, reds_id).save()
    Hole(4, 4, 13, 290, beauty_bay.id, reds_id).save()
    Hole(5, 4, 11, 345, beauty_bay.id, reds_id).save()
    Hole(6, 4, 3, 340, beauty_bay.id, reds_id).save()
    Hole(7, 3, 9, 140, beauty_bay.id, reds_id).save()
    Hole(8, 5, 7, 405, beauty_bay.id, reds_id).save()
    Hole(9, 3, 5, 144, beauty_bay.id, reds_id).save()
    Hole(10, 4, 10, 246, beauty_bay.id, reds_id).save()
    Hole(11, 4, 14, 306, beauty_bay.id, reds_id).save()
    Hole(12, 4, 12, 286, beauty_bay.id, reds_id).save()
    Hole(13, 4, 16, 267, beauty_bay.id, reds_id).save()
    Hole(14, 3, 2, 108, beauty_bay.id, reds_id).save()
    Hole(15, 4, 8, 321, beauty_bay.id, reds_id).save()
    Hole(16, 4, 6, 310, beauty_bay.id, reds_id).save()
    Hole(17, 4, 4, 330, beauty_bay.id, reds_id).save()
    Hole(18, 4, 18, 394, beauty_bay.id, reds_id).save()

    db.session.commit()
