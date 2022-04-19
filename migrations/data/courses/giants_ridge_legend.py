"""
A script to create the Giants Ridge - The Legend.

To perform the migration run the following commands:

>>> from migrations.data.courses import legend
>>> legend.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Giants Ridge - The Legend"""
    legend = Course.query.filter_by(name="Giants Ridge - The Legend").first()

    if legend is not None:
        # What happens if there are matches on the course?
        legend.delete()

    legend = Course("Giants Ridge - The Legend").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 132, 72.6, legend.id).save()
    Hole(1, 4, 13, 365, legend.id, blues_id).save()
    Hole(2, 3, 17, 146, legend.id, blues_id).save()
    Hole(3, 5, 9, 476, legend.id, blues_id).save()
    Hole(4, 4, 11, 381, legend.id, blues_id).save()
    Hole(5, 4, 5, 398, legend.id, blues_id).save()
    Hole(6, 3, 15, 180, legend.id, blues_id).save()
    Hole(7, 4, 7, 388, legend.id, blues_id).save()
    Hole(8, 4, 1, 445, legend.id, blues_id).save()
    Hole(9, 5, 3, 513, legend.id, blues_id).save()
    Hole(10, 4, 10, 378, legend.id, blues_id).save()
    Hole(11, 3, 18, 130, legend.id, blues_id).save()
    Hole(12, 4, 12, 383, legend.id, blues_id).save()
    Hole(13, 4, 14, 382, legend.id, blues_id).save()
    Hole(14, 5, 8, 480, legend.id, blues_id).save()
    Hole(15, 4, 2, 424, legend.id, blues_id).save()
    Hole(16, 5, 6, 493, legend.id, blues_id).save()
    Hole(17, 3, 4, 216, legend.id, blues_id).save()
    Hole(18, 4, 16, 337, legend.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 129, 70.6, legend.id).save()
    Hole(1, 4, 13, 362, legend.id, whites_id).save()
    Hole(2, 3, 17, 320, legend.id, whites_id).save()
    Hole(3, 5, 9, 290, legend.id, whites_id).save()
    Hole(4, 4, 11, 433, legend.id, whites_id).save()
    Hole(5, 4, 5, 117, legend.id, whites_id).save()
    Hole(6, 3, 15, 318, legend.id, whites_id).save()
    Hole(7, 4, 7, 301, legend.id, whites_id).save()
    Hole(8, 4, 1, 136, legend.id, whites_id).save()
    Hole(9, 5, 3, 471, legend.id, whites_id).save()
    Hole(10, 4, 10, 310, legend.id, whites_id).save()
    Hole(11, 3, 18, 319, legend.id, whites_id).save()
    Hole(12, 4, 12, 134, legend.id, whites_id).save()
    Hole(13, 4, 14, 446, legend.id, whites_id).save()
    Hole(14, 5, 8, 124, legend.id, whites_id).save()
    Hole(15, 4, 2, 483, legend.id, whites_id).save()
    Hole(16, 5, 6, 167, legend.id, whites_id).save()
    Hole(17, 3, 4, 347, legend.id, whites_id).save()
    Hole(18, 4, 16, 469, legend.id, whites_id).save()

    db.session.commit()
