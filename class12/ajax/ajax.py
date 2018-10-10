from flask import Flask, render_template
import random

messages = ['If we hit that bullseye, the rest of the dominoes will fall like a house of cards. Checkmate.', 'Your face has been declared a weapon of mass disgusting!', 'In the game of chess, you can never let your adversary see your pieces.', 'I\'ve never heard of such a brutal and shocking injustice that I cared so little about!', 'Using the twin guns of grace and tact, I blasted our worthless enemies with a fair compromise.', 'Prepare to continue the epic struggle between good and neutral.', 'Fire all weapons and open a hailing frequency for my victory yodel.']

app = Flask(__name__)

@app.route('/')
def ajax_main():
    return render_template('ajax.html')

@app.route('/ajax.js')
def ajax_js():
    return render_template('ajax.js')

@app.route('/zapp')
def ajax_message():
    return random.choice(messages)

app.run('0.0.0.0', port=3000)