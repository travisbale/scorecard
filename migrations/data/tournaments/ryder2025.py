"""
A script to create the matches for the 2025 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2025
>>> ryder2025.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2025, 9, 12)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2025, 9, 12), datetime(2025, 9, 13), "Clear Lake, Manitoba, Canada"
        )
        tournament.save()

    clear_lake = Course.query.filter_by(name="Clear Lake Golf Course").first()
    blues = TeeColor.query.filter_by(color="Blue").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 8, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 8, 10), tournament.id).save()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 8, 20), tournament.id).save()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 9, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 9, 40), tournament.id).save()
    Match(clear_lake.id, blues.id, fourball.id, datetime(2025, 9, 12, 9, 50), tournament.id).save()

    scotch = MatchFormat.query.filter_by(name="Modified Scotch").first()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 10), tournament.id).save()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 20), tournament.id).save()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 40), tournament.id).save()
    Match(clear_lake.id, blues.id, scotch.id, datetime(2025, 9, 12, 14, 50), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 10), tournament.id).save()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 20), tournament.id).save()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 40), tournament.id).save()
    Match(clear_lake.id, blues.id, alternate.id, datetime(2025, 9, 13, 8, 50), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 10), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 10), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 20), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 20), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 40), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 40), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 50), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2025, 9, 13, 14, 50), tournament.id).save()

    db.session.commit()
