from flask import *
import requests

app = Flask(__name__)

@app.route('/space')
def space():
    return open('space.json').read()

@app.route('/iss')
def iss():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    return r.text

app.run(host='0.0.0.0')