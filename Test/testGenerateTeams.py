import unittest

from Application import teamGenerator
from infrastructure import fetchData


class TestGenerateTeams(unittest.TestCase):
    def test_generate_pokemon_team(self):
        team = teamGenerator.generate_team_v2(fetchData.fetch_pokemon, 'The Pokemon Team', 5, 'https://pokeapi.co/api/v2/pokemon/', 1, 100)

        self.assertEqual(len(team.players), 5)
        self.assertEqual(team.players[0].position, 'Goalie')
        self.assertEqual(team.players[1].position, 'Defence')
        self.assertEqual(team.players[2].position, 'Defence')
        self.assertEqual(team.players[3].position, 'Offence')
        self.assertEqual(team.players[4].position, 'Offence')

    def test_generate_star_wars_team(self):
        team = teamGenerator.generate_team_v2(fetchData.fetch_person, 'The Star Wars Team', 5, 'https://swapi.dev/api/people/', 1, 82)

        self.assertEqual(len(team.players), 5)

    def test_fetch_pokemon(self):
        pokemon = fetchData.fetch_pokemon('https://pokeapi.co/api/v2/pokemon/', 1)

        self.assertEqual(len(pokemon), 1)
        self.assertEqual(pokemon[0]['name'], 'bulbasaur')
        self.assertEqual(pokemon[0]['height'], 7)
        self.assertEqual(pokemon[0]['weight'], 69)

    def test_fetch_person(self):
        person = fetchData.fetch_person('https://swapi.dev/api/people/', 1)

        self.assertEqual(len(person), 1)
        self.assertEqual(person[0]['name'], 'Luke Skywalker')
        self.assertEqual(person[0]['height'], '172')
        self.assertEqual(person[0]['weight'], '77')

if __name__ == '__main__':
    unittest.main()
