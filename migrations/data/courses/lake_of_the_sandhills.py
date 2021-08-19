"""
A script to create the Lake of the Sandhills golf course.

To perform the migration run the following commands:

>>> from migrations.data.courses import lake_of_the_sandhills
>>> lake_of_the_sandhills.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Lake of the Sandhills"""
    sandhills = Course.query.filter_by(name="Lake of the Sandhills").first()

    if sandhills is not None:
        # What happens if there are matches on the course?
        sandhills.delete()

    sandhills = Course("Lake of the Sandhills").save()

    blacks_id = TeeColor.query.filter_by(color="Black").first().id
    TeeSet(blacks_id, 123, 72.6, sandhills.id).save()
    Hole(1, 4, 18, 360, sandhills.id, blacks_id).save()
    Hole(2, 4, 4, 391, sandhills.id, blacks_id).save()
    Hole(3, 3, 8, 185, sandhills.id, blacks_id).save()
    Hole(4, 5, 12, 516, sandhills.id, blacks_id).save()
    Hole(5, 4, 14, 337, sandhills.id, blacks_id).save()
    Hole(6, 4, 6, 405, sandhills.id, blacks_id).save()
    Hole(7, 3, 16, 167, sandhills.id, blacks_id).save()
    Hole(8, 5, 2, 589, sandhills.id, blacks_id).save()
    Hole(9, 4, 10, 396, sandhills.id, blacks_id).save()
    Hole(10, 4, 1, 454, sandhills.id, blacks_id).save()
    Hole(11, 5, 13, 539, sandhills.id, blacks_id).save()
    Hole(12, 4, 15, 352, sandhills.id, blacks_id).save()
    Hole(13, 3, 3, 216, sandhills.id, blacks_id).save()
    Hole(14, 4, 5, 457, sandhills.id, blacks_id).save()
    Hole(15, 5, 7, 565, sandhills.id, blacks_id).save()
    Hole(16, 3, 17, 160, sandhills.id, blacks_id).save()
    Hole(17, 4, 9, 435, sandhills.id, blacks_id).save()
    Hole(18, 4, 11, 367, sandhills.id, blacks_id).save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 121, 70.8, sandhills.id).save()
    Hole(1, 4, 18, 338, sandhills.id, blues_id).save()
    Hole(2, 4, 4, 371, sandhills.id, blues_id).save()
    Hole(3, 3, 8, 168, sandhills.id, blues_id).save()
    Hole(4, 5, 12, 500, sandhills.id, blues_id).save()
    Hole(5, 4, 14, 324, sandhills.id, blues_id).save()
    Hole(6, 4, 6, 396, sandhills.id, blues_id).save()
    Hole(7, 3, 16, 153, sandhills.id, blues_id).save()
    Hole(8, 5, 2, 568, sandhills.id, blues_id).save()
    Hole(9, 4, 10, 370, sandhills.id, blues_id).save()
    Hole(10, 4, 1, 422, sandhills.id, blues_id).save()
    Hole(11, 5, 13, 514, sandhills.id, blues_id).save()
    Hole(12, 4, 15, 345, sandhills.id, blues_id).save()
    Hole(13, 3, 3, 200, sandhills.id, blues_id).save()
    Hole(14, 4, 5, 413, sandhills.id, blues_id).save()
    Hole(15, 5, 7, 554, sandhills.id, blues_id).save()
    Hole(16, 3, 17, 148, sandhills.id, blues_id).save()
    Hole(17, 4, 9, 418, sandhills.id, blues_id).save()
    Hole(18, 4, 11, 351, sandhills.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 107, 66.7, sandhills.id).save()
    Hole(1, 4, 18, 287, sandhills.id, whites_id).save()
    Hole(2, 4, 4, 343, sandhills.id, whites_id).save()
    Hole(3, 3, 8, 153, sandhills.id, whites_id).save()
    Hole(4, 5, 12, 466, sandhills.id, whites_id).save()
    Hole(5, 4, 14, 267, sandhills.id, whites_id).save()
    Hole(6, 4, 6, 338, sandhills.id, whites_id).save()
    Hole(7, 3, 16, 134, sandhills.id, whites_id).save()
    Hole(8, 5, 2, 479, sandhills.id, whites_id).save()
    Hole(9, 4, 10, 323, sandhills.id, whites_id).save()
    Hole(10, 4, 1, 370, sandhills.id, whites_id).save()
    Hole(11, 5, 13, 473, sandhills.id, whites_id).save()
    Hole(12, 4, 15, 280, sandhills.id, whites_id).save()
    Hole(13, 3, 3, 152, sandhills.id, whites_id).save()
    Hole(14, 4, 5, 368, sandhills.id, whites_id).save()
    Hole(15, 5, 7, 477, sandhills.id, whites_id).save()
    Hole(16, 3, 17, 121, sandhills.id, whites_id).save()
    Hole(17, 4, 9, 342, sandhills.id, whites_id).save()
    Hole(18, 4, 11, 303, sandhills.id, whites_id).save()

    reds_id = TeeColor.query.filter_by(color="Red").first().id
    TeeSet(reds_id, 101, 68.8, sandhills.id).save()
    Hole(1, 4, 18, 277, sandhills.id, reds_id).save()
    Hole(2, 4, 4, 314, sandhills.id, reds_id).save()
    Hole(3, 3, 8, 121, sandhills.id, reds_id).save()
    Hole(4, 5, 12, 406, sandhills.id, reds_id).save()
    Hole(5, 4, 14, 241, sandhills.id, reds_id).save()
    Hole(6, 4, 6, 303, sandhills.id, reds_id).save()
    Hole(7, 3, 16, 104, sandhills.id, reds_id).save()
    Hole(8, 5, 2, 426, sandhills.id, reds_id).save()
    Hole(9, 4, 10, 285, sandhills.id, reds_id).save()
    Hole(10, 4, 1, 325, sandhills.id, reds_id).save()
    Hole(11, 5, 13, 417, sandhills.id, reds_id).save()
    Hole(12, 4, 15, 253, sandhills.id, reds_id).save()
    Hole(13, 3, 3, 134, sandhills.id, reds_id).save()
    Hole(14, 4, 5, 306, sandhills.id, reds_id).save()
    Hole(15, 5, 7, 446, sandhills.id, reds_id).save()
    Hole(16, 3, 17, 98, sandhills.id, reds_id).save()
    Hole(17, 4, 9, 315, sandhills.id, reds_id).save()
    Hole(18, 4, 11, 285, sandhills.id, reds_id).save()

    db.session.commit()
