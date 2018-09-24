import json
f = open('pokedex.json')
o = json.load(f)
f.close()

names = []
for pokemon in o['pokemon']:
    names.append(pokemon['name'])
names.sort()

print(names)
