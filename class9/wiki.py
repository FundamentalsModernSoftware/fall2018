import requests
import sys

URL = "https://en.wikipedia.org/w/api.php"
query = sys.argv[1]
PARAMS = {
    'action': 'query',
    'list': 'search',
    'srsearch': query,
    'format': 'json'
}

r = requests.get(url=URL, params=PARAMS)
data = r.json()

if data['query']['search'][0]['title'] == query:
    print('There is an article titled ' + query + ' on Wikipedia')