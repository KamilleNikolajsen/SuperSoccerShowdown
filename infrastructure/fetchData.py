import requests


def fetch_pokemon(number):
    url_v2 = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url_v2)

    if response.status_code != 200:
        print(f"Error fetching data from {url_v2}, status code: {response.status_code}")
        return []

    data = response.json()
    pokemon = {
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'position': 'Not assigned'
    }

    return [pokemon]


def fetch_person(number):
    url_v2 = f"https://swapi.py4e.com/api/people/{number}"
    response = requests.get(url_v2)
    data = response.json()

    person = {
        'name': data['name'],
        'height': data['height'],
        'weight': data['mass'],
        'position': 'Not assigned'
    }

    return [person]
