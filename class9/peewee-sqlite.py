from peewee import *

db = SqliteDatabase('menu.sqlite')

class Items(Model):
    Name = CharField()
    Price = CharField()
    Type = CharField()
    class Meta:
        database = db

for i in Items.select():
    print (i.Name + ': ' + i.Price)

mainsList = Items.select().where(Items.Type == 'Mains')
print ('There are ' + str(len(mainsList)) + ' main dishes.')
