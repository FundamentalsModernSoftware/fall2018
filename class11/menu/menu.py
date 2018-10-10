from flask import Flask, request, render_template
from fmsdb import *

app = Flask(__name__)s
open_db('menu.json')

def get_sections():
    return orderby(distinct(select(sql_from('items'), ['Section'])), 'Section')


@app.route('/')
def main():
    return render_template('main.html', sections=get_sections())

@app.route('/menu')
def menu():
    items_list = sql_from('items')
    return render_template('menu.html', 
                           items = items_list, 
                           sections = get_sections())

@app.route('/submenu')
def submenu():
    section = request.args['section']
    items_list = where(sql_from('items'), 'Section', section)
    return render_template('submenu.html',
                           section = section,
                           sections = get_sections(),
                           items = items_list)

@app.route('/add', methods=['POST'])
def add():
    new_item = {'Name': request.form['name'],
               'Price': request.form['price'],
               'Section': request.form['section']}
    insert('items', new_item)
    return render_template('add.html',
                           added_item = new_item,
                           sections = get_sections())


app.run(host='0.0.0.0', port=3000)