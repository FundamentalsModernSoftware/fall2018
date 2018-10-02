from flask import *
app = Flask(__name__)

users = {'jtg243': 'James Grimmelmann',
         'cl2278': 'Clarence Lee',
         'gjv25':  'Garrett van Ryzin'}

@app.route('/user')
def user_page():
    if 'username' in request.args:
        username = request.args['username']
    else:
        return 'No user specified!'

    if username in users:
        s = 'This is the homepage for ' + users[username] + '.'
        if 'message' in request.args:
            s += '  BONUS MESSAGE: ' + request.args['message']
        return s
    else:
        return 'No such user.'

app.run(host='0.0.0.0', port=3000)