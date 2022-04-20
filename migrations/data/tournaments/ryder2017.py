"""
A script to create the matches for the 2017 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2017
>>> ryder2017.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2017, 6, 8)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2017, 6, 8), datetime(2017, 6, 10), "Buffalo Point, Manitoba, Canada"
        )
        tournament.save()

    lots = Course.query.filter_by(name="Lake of the Sandhills").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(lots.id, whites.id, fourball.id, datetime(2017, 6, 9, 8, 0), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2017, 6, 9, 8, 7), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2017, 6, 9, 8, 15), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2017, 6, 9, 8, 22), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(lots.id, whites.id, alternate.id, datetime(2017, 6, 9, 14, 0), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2017, 6, 9, 14, 7), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2017, 6, 9, 14, 15), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2017, 6, 9, 14, 22), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 0), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 0), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 7), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 7), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 15), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 15), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 22), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2017, 6, 10, 13, 22), tournament.id).save()

    db.session.commit()
