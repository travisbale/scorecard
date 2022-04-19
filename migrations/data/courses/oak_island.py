"""
A script to create the Oak Island Resort.

To perform the migration run the following commands:

>>> from migrations.data.courses import oak_island
>>> oak_island.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Oak Island Resort"""
    oak_island = Course.query.filter_by(name="Oak Island Resort").first()

    if oak_island is not None:
        # What happens if there are matches on the course?
        oak_island.delete()

    oak_island = Course("Oak Island Resort").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 130, 72.7, oak_island.id).save()
    Hole(1, 4, 3, 400, oak_island.id, blues_id).save()
    Hole(2, 4, 13, 348, oak_island.id, blues_id).save()
    Hole(3, 4, 17, 321, oak_island.id, blues_id).save()
    Hole(4, 5, 1, 459, oak_island.id, blues_id).save()
    Hole(5, 3, 15, 146, oak_island.id, blues_id).save()
    Hole(6, 4, 7, 347, oak_island.id, blues_id).save()
    Hole(7, 4, 11, 328, oak_island.id, blues_id).save()
    Hole(8, 3, 9, 178, oak_island.id, blues_id).save()
    Hole(9, 5, 5, 505, oak_island.id, blues_id).save()
    Hole(10, 4, 12, 342, oak_island.id, blues_id).save()
    Hole(11, 4, 8, 349, oak_island.id, blues_id).save()
    Hole(12, 3, 16, 165, oak_island.id, blues_id).save()
    Hole(13, 5, 2, 494, oak_island.id, blues_id).save()
    Hole(14, 3, 18, 153, oak_island.id, blues_id).save()
    Hole(15, 5, 4, 509, oak_island.id, blues_id).save()
    Hole(16, 3, 14, 189, oak_island.id, blues_id).save()
    Hole(17, 4, 6, 387, oak_island.id, blues_id).save()
    Hole(18, 5, 10, 482, oak_island.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 129, 71.1, oak_island.id).save()
    Hole(1, 4, 3, 362, oak_island.id, whites_id).save()
    Hole(2, 4, 13, 320, oak_island.id, whites_id).save()
    Hole(3, 4, 17, 290, oak_island.id, whites_id).save()
    Hole(4, 5, 1, 433, oak_island.id, whites_id).save()
    Hole(5, 3, 15, 117, oak_island.id, whites_id).save()
    Hole(6, 4, 7, 318, oak_island.id, whites_id).save()
    Hole(7, 4, 11, 301, oak_island.id, whites_id).save()
    Hole(8, 3, 9, 136, oak_island.id, whites_id).save()
    Hole(9, 5, 5, 471, oak_island.id, whites_id).save()
    Hole(10, 4, 12, 310, oak_island.id, whites_id).save()
    Hole(11, 4, 8, 319, oak_island.id, whites_id).save()
    Hole(12, 3, 16, 134, oak_island.id, whites_id).save()
    Hole(13, 5, 2, 446, oak_island.id, whites_id).save()
    Hole(14, 3, 18, 124, oak_island.id, whites_id).save()
    Hole(15, 5, 4, 483, oak_island.id, whites_id).save()
    Hole(16, 3, 14, 167, oak_island.id, whites_id).save()
    Hole(17, 4, 6, 347, oak_island.id, whites_id).save()
    Hole(18, 5, 10, 469, oak_island.id, whites_id).save()

    db.session.commit()
