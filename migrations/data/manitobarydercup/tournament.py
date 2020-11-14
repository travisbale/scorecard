"""Create a new tournament."""

from scorecard import db
from scorecard.models.tournament import Tournament


def create(name, start_date, end_date):
    """Create a tournament."""
    tournament = Tournament.query.filter_by(name=name, start_date=start_date, end_date=end_date).first()

    if tournament is None:
        tournament = Tournament(name, start_date, end_date)
        tournament.save()

        db.session.commit()

    return tournament
