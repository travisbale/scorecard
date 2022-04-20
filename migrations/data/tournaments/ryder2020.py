"""
A script to create the matches for the 2020 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import 2020ryder
>>> 2020ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2020, 6, 4)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2020, 6, 4), datetime(2020, 6, 6), "Killarney, Manitoba, Canada"
        )
        tournament.save()

    killarney = Course.query.filter_by(name="Killarney Lakeside Golf Club").first()
    pleasant_valley = Course.query.filter_by(name="Pleasant Valley Golf Club").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 0), tournament.id).save()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 7), tournament.id).save()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 15), tournament.id).save()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 23), tournament.id).save()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 30), tournament.id).save()
    Match(killarney.id, whites.id, fourball.id, datetime(2020, 6, 5, 8, 37), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 0), tournament.id).save()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 7), tournament.id).save()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 15), tournament.id).save()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 23), tournament.id).save()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 30), tournament.id).save()
    Match(killarney.id, whites.id, alternate.id, datetime(2020, 6, 5, 14, 37), tournament.id).save()

    scotch = MatchFormat.query.filter_by(name="Modified Scotch").first()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 0), tournament.id).save()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 7), tournament.id).save()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 15), tournament.id).save()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 23), tournament.id).save()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 30), tournament.id).save()
    Match(pleasant_valley.id, whites.id, scotch.id, datetime(2020, 6, 6, 8, 37), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 0), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 0), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 7), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 7), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 15), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 15), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 23), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 23), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 30), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 30), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 37), tournament.id).save()
    Match(pleasant_valley.id, whites.id, singles.id, datetime(2020, 6, 6, 14, 37), tournament.id).save()

    db.session.commit()
