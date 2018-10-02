from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def link():
    return render_template('link2.html')

if __name__ == "__main__":
    app.run()
