"""Create the manitoba ryder cup."""

from datetime import datetime

from scorecard import db
from scorecard.models.course import Course
from scorecard.models.match import Match
from scorecard.models.match_format import MatchFormat
from scorecard.models.match_participant import MatchParticipant
from scorecard.models.player import Player
from scorecard.models.team import Team
from scorecard.models.team_member import TeamMember
from scorecard.models.tee_color import TeeColor

from .tournament import create as create_tournament


def create():
    """Create the Manitoba Ryder Cup."""
    tournament = create_tournament("Manitoba Ryder Cup", datetime(2021, 6, 17), datetime(2021, 6, 20))
    red_team = Team.query.filter_by(name="Red").first()
    blue_team = Team.query.filter_by(name="Blue").first()

    players = [
        _create_player("travis.bale@gmail.com", "Travis", "Bale", 11),
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
    ]

    team_members = [
        # Red team members
        TeamMember(tournament.id, red_team.id, players[0].id, True),
        TeamMember(tournament.id, red_team.id, players[1].id, False),
        TeamMember(tournament.id, red_team.id, players[2].id, False),
        TeamMember(tournament.id, red_team.id, players[3].id, False),
        TeamMember(tournament.id, red_team.id, players[4].id, False),
        TeamMember(tournament.id, red_team.id, players[5].id, False),
        TeamMember(tournament.id, red_team.id, players[6].id, False),
        TeamMember(tournament.id, red_team.id, players[7].id, False),
        TeamMember(tournament.id, red_team.id, players[8].id, False),
        TeamMember(tournament.id, red_team.id, players[9].id, False),
        # Blue Team members
        TeamMember(tournament.id, blue_team.id, players[10].id, False),
        TeamMember(tournament.id, blue_team.id, players[11].id, True),
        TeamMember(tournament.id, blue_team.id, players[12].id, False),
        TeamMember(tournament.id, blue_team.id, players[13].id, False),
        TeamMember(tournament.id, blue_team.id, players[14].id, False),
        TeamMember(tournament.id, blue_team.id, players[15].id, False),
        TeamMember(tournament.id, blue_team.id, players[16].id, False),
        TeamMember(tournament.id, blue_team.id, players[17].id, False),
        TeamMember(tournament.id, blue_team.id, players[18].id, False),
        TeamMember(tournament.id, blue_team.id, players[19].id, False),
    ]

    for team_member in team_members:
        team_member.merge()

    # Create matches
    rossmere = Course.query.filter_by(name="Rossmere Golf & Country Club").first()
    whites = TeeColor.query.filter_by(color="White").first()

    fourball = MatchFormat.query.filter_by(name="Fourball").first()
    alt_shot = MatchFormat.query.filter_by(name="Alternate Shot").first()
    scramble = MatchFormat.query.filter_by(name="Scramble").first()
    singles = MatchFormat.query.filter_by(name="Singles").first()

    matches = [
        # Fourball
        Match(rossmere.id, whites.id, fourball.id, datetime(2021, 6, 17, 8, 30)),
        Match(rossmere.id, whites.id, fourball.id, datetime(2021, 6, 17, 8, 37)),
        Match(rossmere.id, whites.id, fourball.id, datetime(2021, 6, 17, 8, 45)),
        Match(rossmere.id, whites.id, fourball.id, datetime(2021, 6, 17, 8, 53)),
        Match(rossmere.id, whites.id, fourball.id, datetime(2021, 6, 17, 9)),
        # Alternate Shot
        Match(rossmere.id, whites.id, alt_shot.id, datetime(2021, 6, 17, 14, 30)),
        Match(rossmere.id, whites.id, alt_shot.id, datetime(2021, 6, 17, 14, 37)),
        Match(rossmere.id, whites.id, alt_shot.id, datetime(2021, 6, 17, 14, 45)),
        Match(rossmere.id, whites.id, alt_shot.id, datetime(2021, 6, 17, 14, 53)),
        Match(rossmere.id, whites.id, alt_shot.id, datetime(2021, 6, 17, 15)),
        # Scramble
        Match(rossmere.id, whites.id, scramble.id, datetime(2021, 6, 18, 8, 30)),
        Match(rossmere.id, whites.id, scramble.id, datetime(2021, 6, 18, 8, 37)),
        Match(rossmere.id, whites.id, scramble.id, datetime(2021, 6, 18, 8, 45)),
        Match(rossmere.id, whites.id, scramble.id, datetime(2021, 6, 18, 8, 53)),
        Match(rossmere.id, whites.id, scramble.id, datetime(2021, 6, 18, 9)),
        # Singles
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 30)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 30)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 37)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 37)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 45)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 45)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 53)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 14, 53)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 15)),
        Match(rossmere.id, whites.id, singles.id, datetime(2021, 6, 18, 15)),
    ]

    for match in matches:
        match.tournament_id = tournament.id
        match.save()

    match_participants = [
        # Fourball - Match 1
        MatchParticipant(tournament.id, matches[0].id, players[0].id),
        MatchParticipant(tournament.id, matches[0].id, players[1].id),
        MatchParticipant(tournament.id, matches[0].id, players[10].id),
        MatchParticipant(tournament.id, matches[0].id, players[11].id),
        # Fourball - Match 2
        MatchParticipant(tournament.id, matches[1].id, players[2].id),
        MatchParticipant(tournament.id, matches[1].id, players[3].id),
        MatchParticipant(tournament.id, matches[1].id, players[12].id),
        MatchParticipant(tournament.id, matches[1].id, players[13].id),
        # Fourball - Match 3
        MatchParticipant(tournament.id, matches[2].id, players[4].id),
        MatchParticipant(tournament.id, matches[2].id, players[5].id),
        MatchParticipant(tournament.id, matches[2].id, players[14].id),
        MatchParticipant(tournament.id, matches[2].id, players[15].id),
        # Fourball - Match 4
        MatchParticipant(tournament.id, matches[3].id, players[6].id),
        MatchParticipant(tournament.id, matches[3].id, players[7].id),
        MatchParticipant(tournament.id, matches[3].id, players[16].id),
        MatchParticipant(tournament.id, matches[3].id, players[17].id),
        # Fourball - Match 5
        MatchParticipant(tournament.id, matches[4].id, players[8].id),
        MatchParticipant(tournament.id, matches[4].id, players[9].id),
        MatchParticipant(tournament.id, matches[4].id, players[18].id),
        MatchParticipant(tournament.id, matches[4].id, players[19].id),
        # Alternate Shot - Match 1
        MatchParticipant(tournament.id, matches[5].id, players[0].id),
        MatchParticipant(tournament.id, matches[5].id, players[1].id),
        MatchParticipant(tournament.id, matches[5].id, players[10].id),
        MatchParticipant(tournament.id, matches[5].id, players[11].id),
        # Alternate Shot - Match 2
        MatchParticipant(tournament.id, matches[6].id, players[2].id),
        MatchParticipant(tournament.id, matches[6].id, players[3].id),
        MatchParticipant(tournament.id, matches[6].id, players[12].id),
        MatchParticipant(tournament.id, matches[6].id, players[13].id),
        # Alternate Shot - Match 3
        MatchParticipant(tournament.id, matches[7].id, players[4].id),
        MatchParticipant(tournament.id, matches[7].id, players[5].id),
        MatchParticipant(tournament.id, matches[7].id, players[14].id),
        MatchParticipant(tournament.id, matches[7].id, players[15].id),
        # Alternate Shot - Match 4
        MatchParticipant(tournament.id, matches[8].id, players[6].id),
        MatchParticipant(tournament.id, matches[8].id, players[7].id),
        MatchParticipant(tournament.id, matches[8].id, players[16].id),
        MatchParticipant(tournament.id, matches[8].id, players[17].id),
        # Alternate Shot - Match 5
        MatchParticipant(tournament.id, matches[9].id, players[8].id),
        MatchParticipant(tournament.id, matches[9].id, players[9].id),
        MatchParticipant(tournament.id, matches[9].id, players[18].id),
        MatchParticipant(tournament.id, matches[9].id, players[19].id),
        # Scramble - Match 1
        MatchParticipant(tournament.id, matches[10].id, players[0].id),
        MatchParticipant(tournament.id, matches[10].id, players[1].id),
        MatchParticipant(tournament.id, matches[10].id, players[10].id),
        MatchParticipant(tournament.id, matches[10].id, players[11].id),
        # Scramble - Match 2
        MatchParticipant(tournament.id, matches[11].id, players[2].id),
        MatchParticipant(tournament.id, matches[11].id, players[3].id),
        MatchParticipant(tournament.id, matches[11].id, players[12].id),
        MatchParticipant(tournament.id, matches[11].id, players[13].id),
        # Scramble - Match 3
        MatchParticipant(tournament.id, matches[12].id, players[4].id),
        MatchParticipant(tournament.id, matches[12].id, players[5].id),
        MatchParticipant(tournament.id, matches[12].id, players[14].id),
        MatchParticipant(tournament.id, matches[12].id, players[15].id),
        # Scramble - Match 4
        MatchParticipant(tournament.id, matches[13].id, players[6].id),
        MatchParticipant(tournament.id, matches[13].id, players[7].id),
        MatchParticipant(tournament.id, matches[13].id, players[16].id),
        MatchParticipant(tournament.id, matches[13].id, players[17].id),
        # Scramble - Match 5
        MatchParticipant(tournament.id, matches[14].id, players[8].id),
        MatchParticipant(tournament.id, matches[14].id, players[9].id),
        MatchParticipant(tournament.id, matches[14].id, players[18].id),
        MatchParticipant(tournament.id, matches[14].id, players[19].id),
        # Singles - Match 1
        MatchParticipant(tournament.id, matches[15].id, players[0].id),
        MatchParticipant(tournament.id, matches[15].id, players[10].id),
        # Singles - Match 2
        MatchParticipant(tournament.id, matches[16].id, players[1].id),
        MatchParticipant(tournament.id, matches[16].id, players[11].id),
        # Singles - Match 3
        MatchParticipant(tournament.id, matches[17].id, players[2].id),
        MatchParticipant(tournament.id, matches[17].id, players[12].id),
        # Singles - Match 4
        MatchParticipant(tournament.id, matches[18].id, players[3].id),
        MatchParticipant(tournament.id, matches[18].id, players[13].id),
        # Singles - Match 5
        MatchParticipant(tournament.id, matches[19].id, players[4].id),
        MatchParticipant(tournament.id, matches[19].id, players[14].id),
        # Singles - Match 6
        MatchParticipant(tournament.id, matches[20].id, players[5].id),
        MatchParticipant(tournament.id, matches[20].id, players[15].id),
        # Singles - Match 7
        MatchParticipant(tournament.id, matches[21].id, players[6].id),
        MatchParticipant(tournament.id, matches[21].id, players[16].id),
        # Singles - Match 8
        MatchParticipant(tournament.id, matches[22].id, players[7].id),
        MatchParticipant(tournament.id, matches[22].id, players[17].id),
        # Singles - Match 9
        MatchParticipant(tournament.id, matches[23].id, players[8].id),
        MatchParticipant(tournament.id, matches[23].id, players[18].id),
        # Singles - Match 10
        MatchParticipant(tournament.id, matches[24].id, players[9].id),
        MatchParticipant(tournament.id, matches[24].id, players[19].id),
    ]

    for participant in match_participants:
        participant.save()

    db.session.commit()


def _create_player(email, first_name, last_name, hdcp):
    player = Player.query.filter_by(email=email).first()

    if player is None:
        player = Player(email, first_name, last_name, hdcp)
        player.save()

    return player
