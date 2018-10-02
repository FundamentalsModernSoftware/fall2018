import sys
import requests
from requests_toolbelt.utils import dump

def view(url):
    resp = requests.get(url)
    data = dump.dump_all(resp, request_prefix = '', response_prefix='')
    print(data.decode('utf-8'))

# If this script is run directly, it loads and dumps its command-line argument.
if __name__ == '__main__':
    # Ensure there are enough command-line arguments.
    if len(sys.argv) < 2:
        print('Provide a URL to request.')
    else:
        view(sys.argv[1])
