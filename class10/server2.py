from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/again')
def hello_again():
    return 'Hello again!'

app.run(host='0.0.0.0')