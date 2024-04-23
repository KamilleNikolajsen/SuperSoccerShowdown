from infrastructure import fetch_data
from application import team_generator
from presentation import display_team


def print_teams():
    pokemon_team = team_generator.generate_team_v2(fetch_data.fetch_pokemon, 'Pokemon Team', 5,
                                                    1, 100)
    display_team.display_team(pokemon_team)

    star_wars_team = team_generator.generate_team_v2(fetch_data.fetch_person, 'Star Wars Team', 5,
                                                     1, 87)
    display_team.display_team(star_wars_team)


if __name__ == '__main__':
    print_teams()
