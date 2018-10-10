from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formShow():
    return render_template('form.html')

@app.route('/done')
def formSubmit():
    m = request.args['message']
    return render_template('result.html', msg = m)

if __name__ == "__main__":
    app.run()