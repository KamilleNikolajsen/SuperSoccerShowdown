import requests


def fetch_pokemon(number):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching data from {url}, status code: {response.status_code}")
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
    url = f"https://swapi.py4e.com/api/people/{number}"
    response = requests.get(url)
    data = response.json()

    person = {
        'name': data['name'],
        'height': data['height'],
        'weight': data['mass'],
        'position': 'Not assigned'
    }

    return [person]
