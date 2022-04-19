"""
A script to create the Minnewasta Golf & Country Club.

To perform the migration run the following commands:

>>> from migrations.data.courses import minnewasta
>>> minnewasta.create()
"""

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.hole import Hole
from scorecard.models.tee_color import TeeColor
from scorecard.models.tee_set import TeeSet


def create():
    """Create Minnewasta Golf Course"""
    minnewasta = Course.query.filter_by(name="Minnewasta Golf & Country Club").first()

    if minnewasta is not None:
        # What happens if there are matches on the course?
        minnewasta.delete()

    minnewasta = Course("Minnewasta Golf & Country Club").save()

    blues_id = TeeColor.query.filter_by(color="Blue").first().id
    TeeSet(blues_id, 130, 72.3, minnewasta.id).save()
    Hole(1, 4, 14, 297, minnewasta.id, blues_id).save()
    Hole(2, 5, 4, 587, minnewasta.id, blues_id).save()
    Hole(3, 4, 2, 466, minnewasta.id, blues_id).save()
    Hole(4, 3, 18, 170, minnewasta.id, blues_id).save()
    Hole(5, 4, 12, 319, minnewasta.id, blues_id).save()
    Hole(6, 4, 8, 303, minnewasta.id, blues_id).save()
    Hole(7, 5, 6, 525, minnewasta.id, blues_id).save()
    Hole(8, 3, 16, 212, minnewasta.id, blues_id).save()
    Hole(9, 4, 10, 341, minnewasta.id, blues_id).save()
    Hole(10, 5, 13, 505, minnewasta.id, blues_id).save()
    Hole(11, 3, 11, 236, minnewasta.id, blues_id).save()
    Hole(12, 4, 1, 450, minnewasta.id, blues_id).save()
    Hole(13, 3, 17, 180, minnewasta.id, blues_id).save()
    Hole(14, 5, 3, 416, minnewasta.id, blues_id).save()
    Hole(15, 5, 5, 499, minnewasta.id, blues_id).save()
    Hole(16, 4, 7, 379, minnewasta.id, blues_id).save()
    Hole(17, 4, 15, 346, minnewasta.id, blues_id).save()
    Hole(18, 4, 9, 415, minnewasta.id, blues_id).save()

    whites_id = TeeColor.query.filter_by(color="White").first().id
    TeeSet(whites_id, 128, 70.2, minnewasta.id).save()
    Hole(1, 4, 14, 278, minnewasta.id, whites_id).save()
    Hole(2, 5, 4, 559, minnewasta.id, whites_id).save()
    Hole(3, 4, 2, 445, minnewasta.id, whites_id).save()
    Hole(4, 3, 18, 152, minnewasta.id, whites_id).save()
    Hole(5, 4, 12, 302, minnewasta.id, whites_id).save()
    Hole(6, 4, 8, 281, minnewasta.id, whites_id).save()
    Hole(7, 5, 6, 506, minnewasta.id, whites_id).save()
    Hole(8, 3, 16, 200, minnewasta.id, whites_id).save()
    Hole(9, 4, 10, 313, minnewasta.id, whites_id).save()
    Hole(10, 5, 13, 483, minnewasta.id, whites_id).save()
    Hole(11, 3, 11, 216, minnewasta.id, whites_id).save()
    Hole(12, 4, 1, 430, minnewasta.id, whites_id).save()
    Hole(13, 3, 17, 148, minnewasta.id, whites_id).save()
    Hole(14, 5, 3, 392, minnewasta.id, whites_id).save()
    Hole(15, 5, 5, 479, minnewasta.id, whites_id).save()
    Hole(16, 4, 7, 352, minnewasta.id, whites_id).save()
    Hole(17, 4, 15, 306, minnewasta.id, whites_id).save()
    Hole(18, 4, 9, 358, minnewasta.id, whites_id).save()

    golds_id = TeeColor.query.filter_by(color="Gold").first().id
    TeeSet(golds_id, 119, 68.2, minnewasta.id).save()
    Hole(1, 4, 14, 262, minnewasta.id, golds_id).save()
    Hole(2, 5, 4, 429, minnewasta.id, golds_id).save()
    Hole(3, 4, 2, 319, minnewasta.id, golds_id).save()
    Hole(4, 3, 18, 128, minnewasta.id, golds_id).save()
    Hole(5, 4, 12, 252, minnewasta.id, golds_id).save()
    Hole(6, 4, 8, 238, minnewasta.id, golds_id).save()
    Hole(7, 5, 6, 487, minnewasta.id, golds_id).save()
    Hole(8, 3, 16, 178, minnewasta.id, golds_id).save()
    Hole(9, 4, 10, 264, minnewasta.id, golds_id).save()
    Hole(10, 5, 13, 448, minnewasta.id, golds_id).save()
    Hole(11, 3, 11, 192, minnewasta.id, golds_id).save()
    Hole(12, 4, 1, 405, minnewasta.id, golds_id).save()
    Hole(13, 3, 17, 137, minnewasta.id, golds_id).save()
    Hole(14, 5, 3, 368, minnewasta.id, golds_id).save()
    Hole(15, 5, 5, 412, minnewasta.id, golds_id).save()
    Hole(16, 4, 7, 319, minnewasta.id, golds_id).save()
    Hole(17, 4, 15, 268, minnewasta.id, golds_id).save()
    Hole(18, 4, 9, 336, minnewasta.id, golds_id).save()

    greens_id = TeeColor.query.filter_by(color="Green").first().id
    TeeSet(greens_id, 110, 65.3, minnewasta.id).save()
    Hole(1, 4, 14, 242, minnewasta.id, greens_id).save()
    Hole(2, 5, 4, 425, minnewasta.id, greens_id).save()
    Hole(3, 4, 2, 315, minnewasta.id, greens_id).save()
    Hole(4, 3, 18, 104, minnewasta.id, greens_id).save()
    Hole(5, 4, 12, 221, minnewasta.id, greens_id).save()
    Hole(6, 4, 8, 219, minnewasta.id, greens_id).save()
    Hole(7, 5, 6, 449, minnewasta.id, greens_id).save()
    Hole(8, 3, 16, 166, minnewasta.id, greens_id).save()
    Hole(9, 4, 10, 196, minnewasta.id, greens_id).save()
    Hole(10, 5, 13, 407, minnewasta.id, greens_id).save()
    Hole(11, 3, 11, 175, minnewasta.id, greens_id).save()
    Hole(12, 4, 1, 387, minnewasta.id, greens_id).save()
    Hole(13, 3, 17, 120, minnewasta.id, greens_id).save()
    Hole(14, 5, 3, 349, minnewasta.id, greens_id).save()
    Hole(15, 5, 5, 398, minnewasta.id, greens_id).save()
    Hole(16, 4, 7, 301, minnewasta.id, greens_id).save()
    Hole(17, 4, 15, 246, minnewasta.id, greens_id).save()
    Hole(18, 4, 9, 313, minnewasta.id, greens_id).save()

    db.session.commit()
