from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    words = ['swordfish', 'xyzzy', 'Tyler sent me']
    return render_template('hello.html', secretWords=words)

if __name__ == "__main__":
    app.run()
