import pandas as pd
import random

from Domain.player import Player
from Domain.team import Team


class TeamGenerator:
    def __init__(self, team_size, team_name):
        self.team_name = team_name
        self.team_size = team_size
        self.players_dict = ()


def generate_team_v2(fetch, team_name, team_size, base_url, random_number_start, random_number_end):
    all_players = []
    random_player_number = generate_random_number(random_number_start, random_number_end, team_size)

    for number in random_player_number:
        all_players.extend(fetch(base_url, number))

    players = [Player(d['name'], d['height'], d['weight'], d['position']) for d in all_players]

    players.sort(key=lambda p: p.height, reverse=True)

    team_data = Team(team_name)
# bytter rundt på højde og vægt, fix!
    goalie = players.pop(0)
    add_player_to_team(team_data, goalie, 'Goalie')
   # goalie.position = 'Goalie'

  #  team_data.add_player(goalie)  # Goalie is the tallest player

    players.sort(key=lambda p: p.weight, reverse=True)

    defence1 = players.pop(0)
    add_player_to_team(team_data, defence1, 'Defence')
    #defence1.position = 'Defence'
    defence2 = players.pop(0)
    add_player_to_team(team_data, defence2, 'Defence')
    #defence2.position = 'Defence'

    #team_data.add_player(defence1)  # Defence is the heaviest player
    #team_data.add_player(defence2)  # Defence is the heaviest player

    players.sort(key=lambda p: p.height)

    offence1 = players.pop(0)
    #offence1.position = 'Offence'
    add_player_to_team(team_data, offence1, 'Offence')
    offence2 = players.pop(0)
    #offence2.position = 'Offence'
    add_player_to_team(team_data, offence2, 'Offence')

    #team_data.add_player(offence1)  # Offence is the shortest player
    #team_data.add_player(offence2)  # Offence is the shortest player

    return team_data


def generate_random_number(start, end, team_size):
    player_number = []
    for i in range(team_size):
        player_number.append(random.randint(start, end))
    return player_number

def add_player_to_team(team, player, position):
    player.position = position
    team.add_player(player)
    return team
