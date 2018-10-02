from flask import *
from fmsdb import *

app = Flask(__name__)
open_db('geo.json')

@app.route('/lookup/<zipcode>')
def lookup(zipcode):
    rows = where(sql_from('zipcodes'), 'Zip Code', zipcode)
    text = zipcode + ' is in ' + rows[0]['Place Name'] + ', ' + rows[0]['State']
    return text

app.run(host='0.0.0.0', port=3000)