"""
A script to create the Neepawa Golf & Country Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import neepawa
>>> neepawa.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Neepawa Golf & Country Club"""
    neepawa = Course.query.filter_by(name="Neepawa Golf & Country Club").first()

    if neepawa is not None:
        # What happens if there are matches on the course?
        neepawa.delete()

    neepawa = Course("Neepawa Golf & Country Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 130, 72.3, neepawa.id).save()
    Hole(1, 4, 14, 369, neepawa.id, blues_id).save()
    Hole(2, 4, 4, 382, neepawa.id, blues_id).save()
    Hole(3, 4, 2, 406, neepawa.id, blues_id).save()
    Hole(4, 3, 18, 148, neepawa.id, blues_id).save()
    Hole(5, 4, 12, 324, neepawa.id, blues_id).save()
    Hole(6, 4, 8, 350, neepawa.id, blues_id).save()
    Hole(7, 5, 6, 494, neepawa.id, blues_id).save()
    Hole(8, 3, 16, 168, neepawa.id, blues_id).save()
    Hole(9, 5, 10, 520, neepawa.id, blues_id).save()
    Hole(10, 5, 13, 520, neepawa.id, blues_id).save()
    Hole(11, 4, 11, 432, neepawa.id, blues_id).save()
    Hole(12, 3, 1, 152, neepawa.id, blues_id).save()
    Hole(13, 4, 17, 394, neepawa.id, blues_id).save()
    Hole(14, 4, 3, 378, neepawa.id, blues_id).save()
    Hole(15, 4, 5, 462, neepawa.id, blues_id).save()
    Hole(16, 5, 7, 530, neepawa.id, blues_id).save()
    Hole(17, 4, 15, 367, neepawa.id, blues_id).save()
    Hole(18, 3, 9, 177, neepawa.id, blues_id).save()

    db.session.commit()
