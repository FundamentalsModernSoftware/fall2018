from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'name' in request.args:
        n = request.args['name']	
    else:
        n = 'nobody'
    return render_template('hello.html', friend=n)

app.run(host='0.0.0.0', port=3000)