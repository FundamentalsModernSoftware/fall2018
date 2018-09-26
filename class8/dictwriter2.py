import csv

# Read CSV file
headers = ['Zip Code',' Place Name', 'State', 'State Abbreviation', 'State Subdivision', 'Latitude', 'Longitude']
f = open('zipcodes.csv')
reader = csv.DictReader(f, fieldnames=headers)
zipcodes = list(reader)
f.close()

# Write CSV file
f_out = open('zipcodes_out.csv', 'w')
writer = csv.DictWriter(f_out, headers)
writer.writerows(zipcodes)
f_out.close()