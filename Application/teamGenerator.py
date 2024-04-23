import random
from Domain.player import Player
from Domain.team import Team


class TeamGenerator:
    def __init__(self, team_size, team_name):
        self.team_name = team_name
        self.team_size = team_size
        self.players = []


def generate_team_v2(fetch, team_name, team_size, random_number_start, random_number_end):
    all_players = []
    random_player_number = generate_random_number(random_number_start, random_number_end, team_size)

    for number in random_player_number:
        all_players.extend(fetch(number))

    players = [Player(d['name'], d['height'], d['weight'], d['position']) for d in all_players]
    team_data = Team(team_name)

    players.sort(key=lambda p: p.height, reverse=True)

    # Pop the first player from the list and assign them as the goalie
    goalie = players.pop(0)
    add_player_to_team(team_data, goalie, 'Goalie')

    players.sort(key=lambda p: p.weight, reverse=True)

    # Pop the first two players from the list and assign them as the defence
    defence1 = players.pop(0)
    add_player_to_team(team_data, defence1, 'Defence')
    defence2 = players.pop(0)
    add_player_to_team(team_data, defence2, 'Defence')

    players.sort(key=lambda p: p.height)

    # Pop the first two players from the list and assign them as the offence
    offence1 = players.pop(0)
    add_player_to_team(team_data, offence1, 'Offence')
    offence2 = players.pop(0)
    add_player_to_team(team_data, offence2, 'Offence')

    return team_data


def generate_random_number(start, end, team_size):
    player_number = []
    for i in range(team_size):
        player_number.append(random.randint(start, end))
    return player_number


def add_player_to_team(team, player, position):
    player.position = position
    team.players.append(player)
    return team
