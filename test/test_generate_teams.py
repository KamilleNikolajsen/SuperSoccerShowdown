import unittest
from application import team_generator
from infrastructure import fetch_data


class TestGenerateTeams(unittest.TestCase):
    def test_generate_pokemon_team(self):
        team = team_generator.generate_team_v2(fetch_data.fetch_pokemon, 'The Pokemon Team', 5,
                                              1, 100)

        self.assertEqual(len(team.players), 5)
        self.assertEqual(team.players[0].position, 'Goalie')
        self.assertEqual(team.players[1].position, 'Defence')
        self.assertEqual(team.players[2].position, 'Defence')
        self.assertEqual(team.players[3].position, 'Offence')
        self.assertEqual(team.players[4].position, 'Offence')

    def test_generate_star_wars_team(self):
        team = team_generator.generate_team_v2(fetch_data.fetch_person, 'The Star Wars Team', 5,
                                              1, 82)

        self.assertEqual(len(team.players), 5)
        self.assertEqual(team.players[0].position, 'Goalie')
        self.assertEqual(team.players[1].position, 'Defence')
        self.assertEqual(team.players[2].position, 'Defence')
        self.assertEqual(team.players[3].position, 'Offence')
        self.assertEqual(team.players[4].position, 'Offence')

    def test_fetch_pokemon(self):
        pokemon = fetch_data.fetch_pokemon(1)

        self.assertEqual(len(pokemon), 1)
        self.assertEqual(pokemon[0]['name'], 'bulbasaur')
        self.assertEqual(pokemon[0]['height'], 7)
        self.assertEqual(pokemon[0]['weight'], 69)

    def test_fetch_person(self):
        person = fetch_data.fetch_person(1)

        self.assertEqual(len(person), 1)
        self.assertEqual(person[0]['name'], 'Luke Skywalker')
        self.assertEqual(person[0]['height'], '172')
        self.assertEqual(person[0]['weight'], '77')

    def test_add_player_to_team(self):
        team = team_generator.TeamGenerator(5, 'test_team')
        player = team_generator.Player('player_name', 1, 1, 'test_position')
        team_generator.add_player_to_team(team, player, 'Defence')

        self.assertEqual(len(team.players), 1)
        self.assertEqual(team.players[0].name, 'player_name')
        self.assertEqual(team.players[0].height, 1)
        self.assertEqual(team.players[0].weight, 1)
        self.assertEqual(team.players[0].position, 'Defence')


if __name__ == '__main__':
    unittest.main()
