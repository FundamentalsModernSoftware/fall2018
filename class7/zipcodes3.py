import csv

# Read CSV file into lines
f = open('zipcodes.csv')
reader = csv.reader(f)
zipcodes = list(reader)
f.close()

# Count zip codes in New York
ny_zipcodes = 0
for row in zipcodes:
    if row[3] == 'NY':
        ny_zipcodes = ny_zipcodes + 1

# Print number of zipcodes
print('There are ' + str(ny_zipcodes) + ' zip codes in New York.')

