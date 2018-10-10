from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formShow():
    return render_template('form.html')

@app.route('/done', methods=['POST'])
def formSubmit():
    return render_template('result.html', fields = request.form)

if __name__ == "__main__":
    app.run()
