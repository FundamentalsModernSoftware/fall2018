from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formShow():
    return render_template('form.html')

@app.route('/done')
def formSubmit():
    m = request.args['message']
    return render_template('result.html', msg = m)

app.run(host='0.0.0.0', port=3000)