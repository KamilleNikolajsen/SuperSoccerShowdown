from infrastructure import fetchData
from Application import teamGenerator
from Application import displayTeam


def print_teams():
    pokemon_team = teamGenerator.generate_team_v2(fetchData.fetch_pokemon, 'Pokemon Team', 5,
                                                  'https://pokeapi.co/api/v2/pokemon/', 1, 100)
    displayTeam.display_team(pokemon_team)

    star_wars_team = teamGenerator.generate_team_v2(fetchData.fetch_person, 'Star Wars Team', 5,
                                                    'https://swapi.py4e.com/api/people/', 1, 100)
    displayTeam.display_team(star_wars_team)


if __name__ == '__main__':
    print_teams()
