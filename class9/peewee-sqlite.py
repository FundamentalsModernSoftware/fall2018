from peewee import *

db = SqliteDatabase('menu.sqlite')

class items(Model):
    Name = CharField()
    Price = CharField()
    Type = CharField()
    class Meta:
        database = db

for i in items.select():
    print (i.Name + ': ' + i.Price)

mainsList = items.select().where(items.Type == 'Mains')
print ('There are ' + str(len(mainsList)) + ' main dishes.')
