"""
A script to create the matches for the 2024 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import 2024ryder
>>> 2024ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament.query.filter_by(start_date=datetime(2024, 9, 13)).first()

    if tournament is None:
        tournament = Tournament(
            "Manitoba Ryder Cup", datetime(2024, 9, 13), datetime(2024, 9, 14), "Golf Kenosee, Saskatchewan, Canada"
        )
        tournament.save()

    kenosee = Course.query.filter_by(name="Kenosee").first()
    whitebear = Course.query.filter_by(name="White Bear Lake Golf Course").first()
    blues = TeeColor.query.filter_by(color="Blue").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 8, 0), tournament.id).save()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 8, 10), tournament.id).save()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 8, 20), tournament.id).save()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 9, 30), tournament.id).save()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 9, 40), tournament.id).save()
    Match(kenosee.id, blues.id, fourball.id, datetime(2024, 9, 13, 9, 50), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 0), tournament.id).save()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 10), tournament.id).save()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 20), tournament.id).save()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 30), tournament.id).save()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 40), tournament.id).save()
    Match(kenosee.id, blues.id, alternate.id, datetime(2024, 9, 13, 14, 50), tournament.id).save()

    scotch = MatchFormat.query.filter_by(name="Modified Scotch").first()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 0), tournament.id).save()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 10), tournament.id).save()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 20), tournament.id).save()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 30), tournament.id).save()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 40), tournament.id).save()
    Match(whitebear.id, whites.id, scotch.id, datetime(2024, 9, 14, 8, 50), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 0), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 0), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 10), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 10), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 20), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 20), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 30), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 30), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 40), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 40), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 50), tournament.id).save()
    Match(kenosee.id, blues.id, singles.id, datetime(2024, 9, 14, 14, 50), tournament.id).save()

    db.session.commit()
