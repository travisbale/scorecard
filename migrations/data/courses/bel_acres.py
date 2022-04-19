"""
A script to create the Bel Acres Golf & Country Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import bel_acres
>>> bel_acres.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Bel Acres Golf & Country Club"""
    bel_acres = Course.query.filter_by(name="Bel Acres Golf & Country Club").first()

    if bel_acres is not None:
        # What happens if there are matches on the course?
        bel_acres.delete()

    bel_acres = Course("Bel Acres Golf & Country Club").save()

    blacks_id = TeeColor.query.filter_by(color="Black").first().id
    TeeSet(blacks_id, 132, 72.9, bel_acres.id).save()
    Hole(1, 5, 11, 524, bel_acres.id, blacks_id).save()
    Hole(2, 4, 5, 415, bel_acres.id, blacks_id).save()
    Hole(3, 3, 17, 132, bel_acres.id, blacks_id).save()
    Hole(4, 5, 13, 497, bel_acres.id, blacks_id).save()
    Hole(5, 4, 9, 403, bel_acres.id, blacks_id).save()
    Hole(6, 3, 7, 209, bel_acres.id, blacks_id).save()
    Hole(7, 4, 1, 451, bel_acres.id, blacks_id).save()
    Hole(8, 4, 15, 380, bel_acres.id, blacks_id).save()
    Hole(9, 4, 3, 399, bel_acres.id, blacks_id).save()
    Hole(10, 4, 12, 411, bel_acres.id, blacks_id).save()
    Hole(11, 4, 4, 381, bel_acres.id, blacks_id).save()
    Hole(12, 5, 8, 554, bel_acres.id, blacks_id).save()
    Hole(13, 3, 10, 195, bel_acres.id, blacks_id).save()
    Hole(14, 4, 6, 424, bel_acres.id, blacks_id).save()
    Hole(15, 4, 2, 472, bel_acres.id, blacks_id).save()
    Hole(16, 3, 18, 188, bel_acres.id, blacks_id).save()
    Hole(17, 4, 16, 375, bel_acres.id, blacks_id).save()
    Hole(18, 5, 14, 565, bel_acres.id, blacks_id).save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 126, 70.2, bel_acres.id).save()
    Hole(1, 5, 11, 505, bel_acres.id, blues_id).save()
    Hole(2, 4, 5, 384, bel_acres.id, blues_id).save()
    Hole(3, 3, 17, 125, bel_acres.id, blues_id).save()
    Hole(4, 5, 13, 480, bel_acres.id, blues_id).save()
    Hole(5, 4, 9, 394, bel_acres.id, blues_id).save()
    Hole(6, 3, 7, 183, bel_acres.id, blues_id).save()
    Hole(7, 4, 1, 426, bel_acres.id, blues_id).save()
    Hole(8, 4, 15, 365, bel_acres.id, blues_id).save()
    Hole(9, 4, 3, 380, bel_acres.id, blues_id).save()
    Hole(10, 4, 12, 363, bel_acres.id, blues_id).save()
    Hole(11, 4, 4, 355, bel_acres.id, blues_id).save()
    Hole(12, 5, 8, 528, bel_acres.id, blues_id).save()
    Hole(13, 3, 10, 179, bel_acres.id, blues_id).save()
    Hole(14, 4, 6, 391, bel_acres.id, blues_id).save()
    Hole(15, 4, 2, 442, bel_acres.id, blues_id).save()
    Hole(16, 3, 18, 150, bel_acres.id, blues_id).save()
    Hole(17, 4, 16, 357, bel_acres.id, blues_id).save()
    Hole(18, 5, 14, 544, bel_acres.id, blues_id).save()

    db.session.commit()
