import csv

# Read CSV file into lines
f = open('zipcodesheader.csv')
reader = csv.DictReader(f)
zipcodes = list(reader)
f.close()

# Make a list of states which have a locality named Springfield
states = []
for row in zipcodes:
    if row['Place Name'] == 'Springfield':
        state = row['State']
        if state not in states:
            states.append(state)
print(states)