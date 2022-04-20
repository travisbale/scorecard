"""
A script to create the matches for the 2015 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2015
>>> ryder2015.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2015, 6, 4)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2015, 6, 4), datetime(2015, 6, 6), "Steinbach, Manitoba, Canada"
        )
        tournament.save()

    quarry_oaks = Course.query.filter_by(name="Quarry Oaks").first()
    bel_acres = Course.query.filter_by(name="Bel Acres Golf & Country Club").first()
    blues = TeeColor.query.filter_by(color="Blue").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(quarry_oaks.id, blues.id, fourball.id, datetime(2015, 6, 5, 8, 0), tournament.id).save()
    Match(quarry_oaks.id, blues.id, fourball.id, datetime(2015, 6, 5, 8, 7), tournament.id).save()
    Match(quarry_oaks.id, blues.id, fourball.id, datetime(2015, 6, 5, 8, 15), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(quarry_oaks.id, blues.id, alternate.id, datetime(2015, 6, 5, 14, 0), tournament.id).save()
    Match(quarry_oaks.id, blues.id, alternate.id, datetime(2015, 6, 5, 14, 7), tournament.id).save()
    Match(quarry_oaks.id, blues.id, alternate.id, datetime(2015, 6, 5, 14, 15), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 0), tournament.id).save()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 0), tournament.id).save()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 7), tournament.id).save()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 7), tournament.id).save()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 15), tournament.id).save()
    Match(bel_acres.id, blues.id, singles.id, datetime(2015, 6, 6, 13, 15), tournament.id).save()

    db.session.commit()
