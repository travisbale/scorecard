"""A script to create the available match formats."""

from scorecard import db
from scorecard.models.match_format import MatchFormat


def create():
    """Create the default match formats."""
    formats = [
        MatchFormat("Stroke play", "Hit the ball less than everyone else."),
        MatchFormat(
            "Match play",
            (
                "In match play, each match features one player from each team."
                " The player with the lower score on each hole wins that hole."
                " If their scores are tied, the hole is halved."
            ),
        ),
        MatchFormat(
            "Fourball",
            (
                "In fourball, each member of a two-man team plays his own ball,"
                " so four balls are in play on every hole. Each team counts the"
                " lowest of its two scores on each hole, and the team whose"
                " player has the lowest score wins the hole. If the low scores"
                " are tied, the hole is halved."
            ),
        ),
        MatchFormat(
            "Foursomes",
            (
                "In foursomes, each two-man team plays one ball per hole with"
                " the players taking turns until each hole is complete. Players"
                " alternate hitting tee shots, with one leading off on"
                " odd-numbered holes, and the other hitting first on"
                " even-numbered holes. The team with the low score on each hole"
                " wins that hole. If their scores are tied, the hole is halved."
            ),
        ),
    ]

    for match_format in formats:
        match_format.save()

    db.session.commit()
