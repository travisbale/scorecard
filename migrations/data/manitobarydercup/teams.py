"""Create teams."""

from scorecard import db
from scorecard.models.team import Team


def create():
    """Create new teams."""
    Team("Red").save()
    Team("Blue").save()

    db.session.commit()
