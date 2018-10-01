import sqlite3

dbname = 'menu.sqlite'

connection = sqlite3.connect(dbname)
c = connection.cursor()

c.execute('SELECT * FROM items;')
rows = c.fetchall()
print(rows)

c.execute('SELECT * FROM items WHERE Type = \'Mains\';')
rows = c.fetchall()
print(rows)
