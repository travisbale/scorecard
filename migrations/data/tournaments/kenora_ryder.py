"""
A script to create the matches for the 2022 Manitoba Ryder Cup

To perform the migration run the following commands:

>>> from migrations.data.tournaments import kenora_ryder
>>> kenora_ryder.create()
"""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.tee_color import TeeColor
from scorecard.models.tournament import Tournament


def create():
    tournament = Tournament("Manitoba Ryder Cup", datetime(2022, 6, 4), datetime(2022, 6, 5), "Kenora, Ontario, Canada")
    tournament.save()

    kenora = Course.query.filter_by(name="Kenora Golf & Country Club").first()
    beauty_bay = Course.query.filter_by(name="Beauty Bay Golf Course").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    Match(beauty_bay.id, whites.id, fourball.id, datetime(2022, 6, 4, 8, 0), tournament.id).save()
    Match(beauty_bay.id, whites.id, fourball.id, datetime(2022, 6, 4, 8, 7), tournament.id).save()
    Match(beauty_bay.id, whites.id, fourball.id, datetime(2022, 6, 4, 8, 15), tournament.id).save()
    Match(beauty_bay.id, whites.id, fourball.id, datetime(2022, 6, 4, 8, 23), tournament.id).save()

    scotch = MatchFormat.query.filter_by(name="Modified Scotch").first()
    Match(kenora.id, whites.id, scotch.id, datetime(2022, 6, 4, 14, 0), tournament.id).save()
    Match(kenora.id, whites.id, scotch.id, datetime(2022, 6, 4, 14, 7), tournament.id).save()
    Match(kenora.id, whites.id, scotch.id, datetime(2022, 6, 4, 14, 15), tournament.id).save()
    Match(kenora.id, whites.id, scotch.id, datetime(2022, 6, 4, 14, 23), tournament.id).save()

    alternate = MatchFormat.query.filter_by(name="Alternate Shot").first()
    Match(beauty_bay.id, whites.id, alternate.id, datetime(2022, 6, 5, 8, 0), tournament.id).save()
    Match(beauty_bay.id, whites.id, alternate.id, datetime(2022, 6, 5, 8, 7), tournament.id).save()
    Match(beauty_bay.id, whites.id, alternate.id, datetime(2022, 6, 5, 8, 15), tournament.id).save()
    Match(beauty_bay.id, whites.id, alternate.id, datetime(2022, 6, 5, 8, 23), tournament.id).save()

    singles = MatchFormat.query.filter_by(name="Singles").first()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 0), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 0), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 7), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 7), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 15), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 15), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 23), tournament.id).save()
    Match(beauty_bay.id, whites.id, singles.id, datetime(2022, 6, 5, 14, 23), tournament.id).save()

    db.session.commit()
