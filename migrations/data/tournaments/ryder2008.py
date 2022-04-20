"""
A script to create the matches for the 2008 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2008
>>> ryder2008.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2008, 6, 12)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2008, 6, 12), datetime(2008, 6, 12), "Morden, Manitoba, Canada"
        )
        tournament.save()

    minnewasta = Course.query.filter_by(name="Minnewasta Golf & Country Club").first()
    carmen = Course.query.filter_by(name="Carmen Golf & Curling Club").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(minnewasta.id, whites.id, fourball.id, datetime(2008, 6, 13, 8, 0), tournament.id).save()
    Match(minnewasta.id, whites.id, fourball.id, datetime(2008, 6, 13, 8, 7), tournament.id).save()
    Match(minnewasta.id, whites.id, fourball.id, datetime(2008, 6, 13, 8, 15), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(minnewasta.id, whites.id, alternate.id, datetime(2008, 6, 13, 14, 0), tournament.id).save()
    Match(minnewasta.id, whites.id, alternate.id, datetime(2008, 6, 13, 14, 7), tournament.id).save()
    Match(minnewasta.id, whites.id, alternate.id, datetime(2008, 6, 13, 14, 15), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 0), tournament.id).save()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 0), tournament.id).save()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 7), tournament.id).save()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 7), tournament.id).save()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 15), tournament.id).save()
    Match(carmen.id, whites.id, singles.id, datetime(2008, 6, 14, 14, 15), tournament.id).save()

    db.session.commit()
