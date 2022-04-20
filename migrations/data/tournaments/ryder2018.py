"""
A script to create the matches for the 2018 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import 2018ryder
>>> 2018ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2018, 6, 7)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2018, 6, 7), datetime(2018, 6, 9), "Buffalo Point, Manitoba, Canada"
        )
        tournament.save()

    dutch_legacy = Course.query.filter_by(name="Dutch Legacy").first()
    lehman_legacy = Course.query.filter_by(name="Lehman Legacy").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(dutch_legacy.id, whites.id, fourball.id, datetime(2018, 6, 8, 8, 0), tournament.id).save()
    Match(dutch_legacy.id, whites.id, fourball.id, datetime(2018, 6, 8, 8, 7), tournament.id).save()
    Match(dutch_legacy.id, whites.id, fourball.id, datetime(2018, 6, 8, 8, 15), tournament.id).save()
    Match(dutch_legacy.id, whites.id, fourball.id, datetime(2018, 6, 8, 8, 23), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(dutch_legacy.id, whites.id, alternate.id, datetime(2018, 6, 8, 14, 0), tournament.id).save()
    Match(dutch_legacy.id, whites.id, alternate.id, datetime(2018, 6, 8, 14, 7), tournament.id).save()
    Match(dutch_legacy.id, whites.id, alternate.id, datetime(2018, 6, 8, 14, 15), tournament.id).save()
    Match(dutch_legacy.id, whites.id, alternate.id, datetime(2018, 6, 8, 14, 23), tournament.id).save()

    scramble = MatchFormat.query.filter_by(name="Scramble").first()
    Match(lehman_legacy.id, whites.id, scramble.id, datetime(2018, 6, 9, 8, 0), tournament.id).save()
    Match(lehman_legacy.id, whites.id, scramble.id, datetime(2018, 6, 9, 8, 7), tournament.id).save()
    Match(lehman_legacy.id, whites.id, scramble.id, datetime(2018, 6, 9, 8, 15), tournament.id).save()
    Match(lehman_legacy.id, whites.id, scramble.id, datetime(2018, 6, 9, 8, 23), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 0), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 0), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 7), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 7), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 15), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 15), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 23), tournament.id).save()
    Match(lehman_legacy.id, whites.id, singles.id, datetime(2018, 6, 9, 14, 23), tournament.id).save()

    db.session.commit()
