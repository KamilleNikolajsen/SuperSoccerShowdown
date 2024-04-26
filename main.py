from infrastructure import fetch_data
from application import generator
from presentation import display


def print_teams():
    pokemon_team = generator.generate_team(fetch_data.fetch_pokemon, 'Pokemon Team', 5,
                                                    1, 100)
    display.display_team(pokemon_team)

    star_wars_team = generator.generate_team(fetch_data.fetch_person, 'Star Wars Team', 5,
                                                     1, 87)
    display.display_team(star_wars_team)


if __name__ == '__main__':
    print_teams()
