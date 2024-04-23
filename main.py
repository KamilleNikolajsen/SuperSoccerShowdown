# This is a sample Python script.
from infrastructure import fetchData
from Application import teamGenerator
from Application import displayTeam


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_teams(name):

    pokemon_team = teamGenerator.generate_team_v2(fetchData.fetch_pokemon, 'Pokemon Team', 5, 'https://pokeapi.co/api/v2/pokemon/', 1, 100)
    displayTeam.display_team(pokemon_team)

    # star_wars_team = teamGenerator.generate_team_v2(fetchData.fetch_person, 'Star Wars Team', 5, 'https://swapi.dev/api/people/', 1, 100)
    # displayTeam.display_team(star_wars_team)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_teams('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
