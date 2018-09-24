import csv

# Read CSV file into lines
f = open('zipcodes.csv')
reader = csv.reader(f)
zipcodes = list(reader)
f.close()

# Make a list of states which have a locality named Springfield
states = []
for row in zipcodes:
    if row[1] == 'Springfield':
        state = row[2]
        if state not in states:
            states.append(state)
print(states)