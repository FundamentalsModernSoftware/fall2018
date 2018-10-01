import requests
import sys

URL = 'https://pokeapi.co/api/v2/pokemon/'
id = sys.argv[1]
full_URL = URL + id + '/'
r = requests.get(full_URL)
j = r.json()

print('Pokemon ' + id + ' is ' + j['name'])