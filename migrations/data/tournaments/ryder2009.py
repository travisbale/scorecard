"""
A script to create the matches for the 2009 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2009
>>> ryder2009.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2009, 6, 11)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2009, 6, 11), datetime(2009, 6, 13), "Neepawa, Manitoba, Canada"
        )
        tournament.save()

    neepawa = Course.query.filter_by(name="Neepawa Golf & Country Club").first()
    clear_lake = Course.query.filter_by(name="Clear Lake Golf Course").first()
    blues = TeeColor.query.filter_by(color="Blue").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(neepawa.id, blues.id, fourball.id, datetime(2009, 6, 12, 8, 0), tournament.id).save()
    Match(neepawa.id, blues.id, fourball.id, datetime(2009, 6, 12, 8, 7), tournament.id).save()
    Match(neepawa.id, blues.id, fourball.id, datetime(2009, 6, 12, 8, 15), tournament.id).save()
    Match(neepawa.id, blues.id, fourball.id, datetime(2009, 6, 12, 8, 22), tournament.id).save()
    Match(neepawa.id, blues.id, fourball.id, datetime(2009, 6, 12, 8, 30), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(neepawa.id, blues.id, alternate.id, datetime(2009, 6, 12, 14, 0), tournament.id).save()
    Match(neepawa.id, blues.id, alternate.id, datetime(2009, 6, 12, 14, 7), tournament.id).save()
    Match(neepawa.id, blues.id, alternate.id, datetime(2009, 6, 12, 14, 15), tournament.id).save()
    Match(neepawa.id, blues.id, alternate.id, datetime(2009, 6, 12, 14, 22), tournament.id).save()
    Match(neepawa.id, blues.id, alternate.id, datetime(2009, 6, 12, 14, 30), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 0), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 7), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 7), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 15), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 15), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 22), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 22), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 30), tournament.id).save()
    Match(clear_lake.id, blues.id, singles.id, datetime(2009, 6, 13, 14, 30), tournament.id).save()

    db.session.commit()
