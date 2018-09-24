# Read CSV file into lines
f = open('zipcodes.csv')
lines = f.read().splitlines()
f.close()

# Split each line on the commas
zipcodes = []
for line in lines:
    fields = line.split(',')
    zipcodes.append(fields)

# Count zip codes in New York
ny_zipcodes = 0
for row in zipcodes:
    if row[3] == 'NY':
        ny_zipcodes = ny_zipcodes + 1

# Print number of zipcodes
print('There are ' + str(ny_zipcodes) + ' zip codes in New York.')

