from flask import *
app = Flask(__name__)

users = {'jtg243': 'James Grimmelmann',
         'cl2278': 'Clarence Lee',
         'gjv25':  'Garrett van Ryzin'}

@app.route('/users/<username>')
def user_homepage(username):
    if username in users:
        return 'This is the homepage for ' + users[username] + '.'
    else:
        return 'No such user.', 404


app.run(host='0.0.0.0')