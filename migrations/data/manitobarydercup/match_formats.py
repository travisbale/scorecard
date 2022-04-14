"""
A script to create the available match formats.

To perform the migration run the following commands:

>>> from migrations.data.manitobarydercup import match_formats
>>> match_formats.create()
"""

from scorecard import db
from scorecard.models.match_format import MatchFormat


def create():
    """Create the default match formats."""
    _create_match_format("Stroke play", "Hit the ball less than everyone else.")
    _create_match_format(
        "Singles",
        "In singles, each match features one player from each team. The"
        " player with the lower score on each hole wins that hole. If their"
        " scores are tied, the hole is halved.",
    )
    _create_match_format(
        "Scramble",
        "In a scramble, each member of a two-man team hits a tee shot on"
        " each hole. Following following the tee shot, both players decide"
        " which shot they prefer and continue to play the hole from that"
        " location. The player whose shot was not selected picks up their"
        " ball and moves it to within one club length of the selected spot"
        " before continuing. The team with the low score on each hole wins"
        " that hole. If their scores are tied, the hole is halved.",
    )
    _create_match_format(
        "Fourball",
        "In fourball, each member of a two-man team plays his own ball,"
        " so four balls are in play on every hole. Each team counts the"
        " lowest of its two scores on each hole, and the team whose"
        " player has the lowest score wins the hole. If the low scores"
        " are tied, the hole is halved.",
    )
    _create_match_format(
        "Alternate Shot",
        "In foursomes, each two-man team plays one ball per hole with"
        " the players taking turns until each hole is complete. Players"
        " alternate hitting tee shots, with one leading off on"
        " odd-numbered holes, and the other hitting first on"
        " even-numbered holes. The team with the low score on each hole"
        " wins that hole. If their scores are tied, the hole is halved.",
    )
    _create_match_format(
        "Modified Scotch",
        "In modified scotch, each two man team hits a tee shot. The team then"
        " selects which ball they would like to hit for their second shot."
        " the player who did not hit the selected ball must take the second"
        " shot. After that the hole is played as a scramble where both players"
        " hit a shot and the ball is played from the better position.",
    )

    db.session.commit()


def _create_match_format(name, description):
    match_format = MatchFormat.query.filter_by(name=name).first()

    if match_format is None:
        match_format = MatchFormat(name, description)
        match_format.save()

    return match_format
