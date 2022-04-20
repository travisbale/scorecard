"""
A script to create the matches for the 2013 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2013
>>> ryder2013.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2013, 6, 6)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2013, 6, 6), datetime(2013, 6, 8), "Giants Ridge, Minnesota, USA"
        )
        tournament.save()

    quarry = Course.query.filter_by(name="Giants Ridge - Quarry").first()
    legend = Course.query.filter_by(name="Giants Ridge - The Legend").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(quarry.id, whites.id, fourball.id, datetime(2013, 6, 7, 8, 0), tournament.id).save()
    Match(quarry.id, whites.id, fourball.id, datetime(2013, 6, 7, 8, 7), tournament.id).save()
    Match(quarry.id, whites.id, fourball.id, datetime(2013, 6, 7, 8, 15), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(quarry.id, whites.id, alternate.id, datetime(2013, 6, 7, 14, 0), tournament.id).save()
    Match(quarry.id, whites.id, alternate.id, datetime(2013, 6, 7, 14, 7), tournament.id).save()
    Match(quarry.id, whites.id, alternate.id, datetime(2013, 6, 7, 14, 15), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 0), tournament.id).save()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 0), tournament.id).save()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 7), tournament.id).save()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 7), tournament.id).save()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 15), tournament.id).save()
    Match(legend.id, whites.id, singles.id, datetime(2013, 6, 8, 13, 15), tournament.id).save()

    db.session.commit()
