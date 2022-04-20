"""
A script to create the matches for the 2011 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import ryder2011
>>> ryder2011.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2011, 6, 9)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2011, 6, 9), datetime(2011, 6, 11), "Lac Du Bonnet, Manitoba, Canada"
        )
        tournament.save()

    granite_hills = Course.query.filter_by(name="Granite Hills Golf Club").first()
    pinawa = Course.query.filter_by(name="Pinawa Golf & Country Club").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(granite_hills.id, whites.id, fourball.id, datetime(2011, 6, 10, 8, 0), tournament.id).save()
    Match(granite_hills.id, whites.id, fourball.id, datetime(2011, 6, 10, 8, 7), tournament.id).save()
    Match(granite_hills.id, whites.id, fourball.id, datetime(2011, 6, 10, 8, 15), tournament.id).save()
    Match(granite_hills.id, whites.id, fourball.id, datetime(2011, 6, 10, 8, 22), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(granite_hills.id, whites.id, alternate.id, datetime(2011, 6, 10, 14, 0), tournament.id).save()
    Match(granite_hills.id, whites.id, alternate.id, datetime(2011, 6, 10, 14, 7), tournament.id).save()
    Match(granite_hills.id, whites.id, alternate.id, datetime(2011, 6, 10, 14, 15), tournament.id).save()
    Match(granite_hills.id, whites.id, alternate.id, datetime(2011, 6, 10, 14, 22), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 0), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 0), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 7), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 7), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 15), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 15), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 22), tournament.id).save()
    Match(pinawa.id, whites.id, singles.id, datetime(2011, 6, 11, 13, 22), tournament.id).save()

    db.session.commit()
