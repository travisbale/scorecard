"""Create the list of available tee colors."""

from scorecard import db
from scorecard.models.tee_color import TeeColor


def create():
    """Create the list of available tee colors."""
    tee_colors = [
        TeeColor("Green"),
        TeeColor("Yellow"),
        TeeColor("Red"),
        TeeColor("White"),
        TeeColor("Blue"),
        TeeColor("Gold"),
        TeeColor("Black"),
    ]

    for tee_color in tee_colors:
        tee_color.save()

    db.session.commit()
