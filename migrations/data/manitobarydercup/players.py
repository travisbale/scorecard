"""A script to create some players."""

from scorecard import db
from scorecard.models.player import Player


def create():
    """Create some new players."""
    players = [
        _create_player("ian.fordyce@gmail.com", "Ian", "Fordyce", 14),
        _create_player("nigel.milnes@gmail.com", "Nigel", "Milnes", 21),
        _create_player("jon.ray@gmail.com", "Jon", "Ray", 11),
        _create_player("h.benning@gmail.com", "H", "Benning", 11),
        _create_player("i.mcdonald@gmail.com", "I", "McDonald", 11),
        _create_player("garry.hargreaves@gmail.com", "Garry", "Hargreaves", 11),
        _create_player("b.horn@gmail.com", "B", "Horn", 11),
        _create_player("b.zander@gmail.com", "B", "Zander", 11),
        _create_player("matt.pilloud@gmail.com", "Matt", "Pilloud", 11),
        _create_player("r.lall@gmail.com", "R", "Lall", 11),
        _create_player("keith.vanwalleghem@gmail.com", "Keith", "VanWalleghem", 11),
        _create_player("jason.gunnalugson@gmail.com", "Jason", "Gunnlaugson", 11),
        _create_player("c.kehler@gmail.com", "C", "Kehler", 11),
        _create_player("g.cramer@gmail.com", "G", "Cramer", 11),
        _create_player("matt.phin@gmail.com", "Matt", "Phin", 11),
        _create_player("e.sthilaire@gmail.com", "E", "St-Hilaire", 11),
        _create_player("j.rabe@gmail.com", "J", "Rabe", 11),
        _create_player("d.mcinnes@gmail.com", "Dan", "McInnes", 11),
        _create_player("connor.macaulay@gmail.com", "Connor", "MacAulay", 11),
        _create_player("a.sefton@gmail.com", "A", "Sefton", 11),
        _create_player("m.hargreaves@gmail.com", "M", "Hargreaves", 11),
        _create_player("travis.bale@gmail.com", "Travis", "Bale", 11),
    ]

    db.session.commit()

    return players


def _create_player(email, first_name, last_name, hdcp):
    player = Player.query.filter_by(email=email).first()

    if player is None:
        player = Player(email, first_name, last_name, hdcp)
        player.save()

    return player
