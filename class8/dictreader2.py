import csv

# Read CSV file into lines
headers = ['Zip Code',' Place Name', 'State', 'State Abbreviation', 'State Subdivision', 'Latitude', 'Longitude']
f = open('zipcodes.csv')
reader = csv.DictReader(f, fieldnames=headers)
zipcodes = list(reader)
f.close()

# Sanity check
print(zipcodes[0])