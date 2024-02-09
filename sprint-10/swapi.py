from pprint import pprint

import requests


response = requests.get('https://swapi.dev/api/people/?search=luke').json()[
    'results'
][0]
diameter = requests.get(response['homeworld']).json()['diameter']

print(diameter)
