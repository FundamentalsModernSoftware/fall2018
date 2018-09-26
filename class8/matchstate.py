import csv

# Read CSV file into lines
f = open('zipcodesheader.csv')
reader = csv.DictReader(f)
zipcodes = list(reader)
f.close()

def match_state(rows, state):
    matches = []
    for row in rows:
        if row['State'] == state:
            matches.append(row['Zip Code'])
    return matches

print('New York: ')
print(match_state(zipcodes, 'New York'))
print('New Jersey: ' )
print(match_state(zipcodes, 'New Jersey'))