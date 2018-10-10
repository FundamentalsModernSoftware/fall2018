from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    words = ['swordfish', 'xyzzy', 'Tyler sent me']
    return render_template('hello.html', secretWords=words)

app.run(host='0.0.0.0', port=3000)