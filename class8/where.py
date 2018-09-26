import csv

headers = ['Zip Code', 'Place Name', 'State', 'State Abbreviation', 'State Subdivision', 'Latitude', 'Longitude']
f = open('zipcodes.csv')
reader = csv.DictReader(f, fieldnames=headers)
zipcodes = list(reader)
f.close()

# Return only the rows where field == value
def where(rows, field, value):
    matches = []
    for row in rows:
        if row[field] == value:
            matches.append(row)
    return matches

# Return list of the values in field
def select(rows, field):
    values = []
    for row in rows:
        values.append(row[field])
    return values

print('Zip codes in New York: ')
print(select(where(zipcodes, 'State', 'New York'), 'Zip Code'))

print('Place names in New Jersey: ' )
print(select(where(zipcodes, 'State', 'New Jersey'), 'Place Name'))

print('Place names in Bergen County: ')
print(select(where(zipcodes, 'State Subdivision', 'Bergen'), 'Place Name'))