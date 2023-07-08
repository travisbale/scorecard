"""
A script to create the matches for the 2023 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import 2023ryder
>>> 2023ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2023, 7, 21)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2023, 7, 21), datetime(2023, 5, 22), "Cragun's Resort, Minnesota, USA"
        )
        tournament.save()

    lehman = Course.query.filter_by(name="Lehman Legacy").first()
    dutch = Course.query.filter_by(name="Dutch Legacy").first()
    whites = TeeColor.query.filter_by(color="White").first()

    scotch = MatchFormat.query.filter_by(name="Modified Scotch").first()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 8, 30), tournament.id).save()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 8, 40), tournament.id).save()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 8, 50), tournament.id).save()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 9, 0), tournament.id).save()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 9, 10), tournament.id).save()
    Match(dutch.id, whites.id, scotch.id, datetime(2023, 7, 21, 9, 20), tournament.id).save()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 15, 35), tournament.id).save()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 15, 45), tournament.id).save()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 15, 55), tournament.id).save()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 16, 5), tournament.id).save()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 16, 15), tournament.id).save()
    Match(lehman.id, whites.id, fourball.id, datetime(2023, 7, 21, 16, 25), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 25), tournament.id).save()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 35), tournament.id).save()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 45), tournament.id).save()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 55), tournament.id).save()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 5), tournament.id).save()
    Match(lehman.id, whites.id, alternate.id, datetime(2023, 7, 22, 8, 15), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 30), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 30), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 40), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 40), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 50), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 15, 50), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 0), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 0), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 10), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 10), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 20), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 20), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 30), tournament.id).save()
    Match(dutch.id, whites.id, singles.id, datetime(2023, 7, 22, 16, 30), tournament.id).save()

    db.session.commit()
