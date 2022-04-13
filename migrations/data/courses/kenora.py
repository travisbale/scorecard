"""
A script to create the Lake of the Sandhills golf course.

To perform the migration run the following commands:

>>> from migrations.data.courses import kenora
>>> kenora.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Kenora Golf & Country Club"""
    kenora = Course.query.filter_by(name="Kenora Golf & Country Club").first()

    if kenora is not None:
        # What happens if there are matches on the course?
        kenora.delete()

    kenora = Course("Kenora Golf & Country Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 138, 71.1, kenora.id).save()
    Hole(1, 4, 7, 412, kenora.id, blues_id).save()
    Hole(2, 4, 11, 392, kenora.id, blues_id).save()
    Hole(3, 4, 15, 335, kenora.id, blues_id).save()
    Hole(4, 4, 5, 414, kenora.id, blues_id).save()
    Hole(5, 3, 9, 177, kenora.id, blues_id).save()
    Hole(6, 4, 3, 366, kenora.id, blues_id).save()
    Hole(7, 3, 13, 192, kenora.id, blues_id).save()
    Hole(8, 4, 17, 513, kenora.id, blues_id).save()
    Hole(9, 4, 1, 378, kenora.id, blues_id).save()
    Hole(10, 4, 6, 393, kenora.id, blues_id).save()
    Hole(11, 4, 10, 368, kenora.id, blues_id).save()
    Hole(12, 3, 16, 140, kenora.id, blues_id).save()
    Hole(13, 5, 2, 495, kenora.id, blues_id).save()
    Hole(14, 4, 8, 380, kenora.id, blues_id).save()
    Hole(15, 3, 14, 135, kenora.id, blues_id).save()
    Hole(16, 5, 12, 440, kenora.id, blues_id).save()
    Hole(17, 4, 18, 337, kenora.id, blues_id).save()
    Hole(18, 5, 4, 476, kenora.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 131, 70.1, kenora.id).save()
    Hole(1, 4, 7, 412, kenora.id, whites_id).save()
    Hole(2, 4, 11, 335, kenora.id, whites_id).save()
    Hole(3, 4, 15, 319, kenora.id, whites_id).save()
    Hole(4, 4, 5, 392, kenora.id, whites_id).save()
    Hole(5, 3, 9, 163, kenora.id, whites_id).save()
    Hole(6, 4, 3, 360, kenora.id, whites_id).save()
    Hole(7, 3, 13, 174, kenora.id, whites_id).save()
    Hole(8, 4, 17, 472, kenora.id, whites_id).save()
    Hole(9, 4, 1, 341, kenora.id, whites_id).save()
    Hole(10, 4, 6, 369, kenora.id, whites_id).save()
    Hole(11, 4, 10, 350, kenora.id, whites_id).save()
    Hole(12, 3, 16, 130, kenora.id, whites_id).save()
    Hole(13, 5, 2, 470, kenora.id, whites_id).save()
    Hole(14, 4, 8, 361, kenora.id, whites_id).save()
    Hole(15, 3, 14, 125, kenora.id, whites_id).save()
    Hole(16, 5, 12, 420, kenora.id, whites_id).save()
    Hole(17, 4, 18, 314, kenora.id, whites_id).save()
    Hole(18, 5, 4, 471, kenora.id, whites_id).save()

    greens_id = TeeColor.query.filter_by(color="Green").first().id
    TeeSet(greens_id, 124, 68, kenora.id).save()
    Hole(1, 4, 7, 330, kenora.id, greens_id).save()
    Hole(2, 4, 11, 335, kenora.id, greens_id).save()
    Hole(3, 4, 15, 319, kenora.id, greens_id).save()
    Hole(4, 4, 5, 310, kenora.id, greens_id).save()
    Hole(5, 3, 9, 125, kenora.id, greens_id).save()
    Hole(6, 4, 3, 360, kenora.id, greens_id).save()
    Hole(7, 3, 13, 155, kenora.id, greens_id).save()
    Hole(8, 4, 17, 472, kenora.id, greens_id).save()
    Hole(9, 4, 1, 311, kenora.id, greens_id).save()
    Hole(10, 4, 6, 369, kenora.id, greens_id).save()
    Hole(11, 4, 10, 340, kenora.id, greens_id).save()
    Hole(12, 3, 16, 125, kenora.id, greens_id).save()
    Hole(13, 5, 2, 450, kenora.id, greens_id).save()
    Hole(14, 4, 8, 303, kenora.id, greens_id).save()
    Hole(15, 3, 14, 125, kenora.id, greens_id).save()
    Hole(16, 5, 12, 420, kenora.id, greens_id).save()
    Hole(17, 4, 18, 314, kenora.id, greens_id).save()
    Hole(18, 5, 4, 411, kenora.id, greens_id).save()

    reds_id = TeeColor.query.filter_by(color="Red").first().id
    TeeSet(reds_id, 123, 70.9, kenora.id).save()
    Hole(1, 4, 7, 330, kenora.id, reds_id).save()
    Hole(2, 4, 5, 322, kenora.id, reds_id).save()
    Hole(3, 4, 9, 297, kenora.id, reds_id).save()
    Hole(4, 4, 1, 300, kenora.id, reds_id).save()
    Hole(5, 3, 17, 125, kenora.id, reds_id).save()
    Hole(6, 4, 11, 301, kenora.id, reds_id).save()
    Hole(7, 3, 15, 155, kenora.id, reds_id).save()
    Hole(8, 4, 13, 410, kenora.id, reds_id).save()
    Hole(9, 4, 3, 311, kenora.id, reds_id).save()
    Hole(10, 4, 10, 344, kenora.id, reds_id).save()
    Hole(11, 4, 8, 290, kenora.id, reds_id).save()
    Hole(12, 3, 18, 115, kenora.id, reds_id).save()
    Hole(13, 5, 2, 420, kenora.id, reds_id).save()
    Hole(14, 4, 12, 303, kenora.id, reds_id).save()
    Hole(15, 3, 14, 92, kenora.id, reds_id).save()
    Hole(16, 5, 6, 370, kenora.id, reds_id).save()
    Hole(17, 4, 16, 310, kenora.id, reds_id).save()
    Hole(18, 5, 4, 411, kenora.id, reds_id).save()

    db.session.commit()
