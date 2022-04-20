"""
A script to create the matches for the 2019 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import 2019ryder
>>> 2019ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2019, 6, 6)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2019, 6, 6), datetime(2019, 6, 8), "Buffalo Point, Manitoba, Canada"
        )
        tournament.save()

    lots = Course.query.filter_by(name="Lake of the Sandhills").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(lots.id, whites.id, fourball.id, datetime(2019, 6, 7, 8, 0), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2019, 6, 7, 8, 7), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2019, 6, 7, 8, 15), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2019, 6, 7, 8, 23), tournament.id).save()
    Match(lots.id, whites.id, fourball.id, datetime(2019, 6, 7, 8, 30), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(lots.id, whites.id, alternate.id, datetime(2019, 6, 7, 14, 0), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2019, 6, 7, 14, 7), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2019, 6, 7, 14, 15), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2019, 6, 7, 14, 23), tournament.id).save()
    Match(lots.id, whites.id, alternate.id, datetime(2019, 6, 7, 14, 30), tournament.id).save()

    scramble = MatchFormat.query.filter_by(name="Scramble").first()
    Match(lots.id, whites.id, scramble.id, datetime(2019, 6, 9, 8, 0), tournament.id).save()
    Match(lots.id, whites.id, scramble.id, datetime(2019, 6, 8, 8, 7), tournament.id).save()
    Match(lots.id, whites.id, scramble.id, datetime(2019, 6, 8, 8, 15), tournament.id).save()
    Match(lots.id, whites.id, scramble.id, datetime(2019, 6, 8, 8, 23), tournament.id).save()
    Match(lots.id, whites.id, scramble.id, datetime(2019, 6, 8, 8, 30), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 9, 14, 0), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 0), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 7), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 7), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 15), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 15), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 23), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 23), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 30), tournament.id).save()
    Match(lots.id, whites.id, singles.id, datetime(2019, 6, 8, 14, 30), tournament.id).save()

    db.session.commit()
