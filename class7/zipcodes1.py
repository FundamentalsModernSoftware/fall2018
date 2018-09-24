# Read CSV file into lines
f = open('zipcodes.csv')
lines = f.read().splitlines()
f.close()

# Split each line on the commas
zipcodes = []
for line in lines:
    fields = line.split(',')
    zipcodes.append(fields)
