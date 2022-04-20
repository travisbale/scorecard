"""
A script to create players who have participated in the Manitoba Ryder Cup.

To perform the migration run the following commands:

>>> from migrations.data.players import players
>>> players.create()
"""

from scorecard import db
from scorecard.models.player import Player


def create():
    """Create the tournament participants."""
    Player("m.lepage@manitobarydercup.com", "M", "Lepage", "").save()
    Player("r.lall@manitobarydercup.com", "R", "Lall", "").save()
    Player("b.vanwalleghem@manitobarydercup.com", "B", "Van Walleghem", "").save()
    Player("c.kehler@manitobarydercup.com", "C", "Kehler", "").save()
    Player("a.sefton@manitobarydercup.com", "A", "Sefton", "").save()
    Player("t.antolovich@manitobarydercup.com", "T", "Antolovich", "", "").save()
    Player("m.hargreaves@manitobarydercup.com", "M", "Hargreaves", "").save()
    Player("r.decosse@manitobarydercup.com", "R", "Decosse", "").save()
    Player("d.newfield@manitobarydercup.com", "D", "Newfield", "").save()
    Player("g.cramer@manitobarydercup.com", "G", "Cramer", "").save()
    Player("m.rackham@manitobarydercup.com", "M", "Rackham", "").save()
    Player("a.loewen@manitobarydercup.com", "A", "Loewen", "").save()
    Player("d.redfern@manitobarydercup.com", "D", "Redfern", "").save()
    Player("s.mckee@manitobarydercup.com", "S", "McKee", "").save()
    Player("t.reidle@manitobarydercup.com", "T", "Reidle", "").save()
    Player("d.bohemier@manitobarydercup.com", "D", "Bohemier", "").save()
    Player("h.kaler@manitobarydercup.com", "H", "Kaler", "").save()
    Player("c.thomson@manitobarydercup.com", "C", "Thomson", "").save()
    Player("c.mccannel@manitobarydercup.com", "C", "McCannel", "").save()
    Player("a.challis@manitobarydercup.com", "A", "Challis", "").save()
    Player("m.hobday@manitobarydercup.com", "M", "Hobday", "").save()
    Player("b.zubrycki@manitobarydercup.com", "B", "Zubrycki", "").save()
    Player("d.magnus@manitobarydercup.com", "D", "Magnus", "").save()
    Player("e.sthilaire@manitobarydercup.com", "E", "St-Hilaire", "").save()
    Player("d.mcinnes@manitobarydercup.com", "D", "McInnes", "").save()
    Player("k.emond@manitobarydercup.com", "K", "Emond", "").save()
    Player("c.kellas@manitobarydercup.com", "C", "Kellas", "").save()
    Player("s.greenhalgh@manitobarydercup.com", "S", "Greenhalgh", "").save()
    Player("j.gunnlaugson@manitobarydercup.com", "Jason", "Gunnlaugson", "").save()
    Player("nmilnes002@gmail.com", "Nigel", "Milnes", "").save()
    Player("b.bayes@manitobarydercup.com", "B", "Bayes", "").save()
    Player("t.horn@manitobarydercup.com", "T", "Horn", "").save()

    db.session.commit()
