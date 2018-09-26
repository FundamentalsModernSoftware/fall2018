import csv

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