import csv

# Read CSV file into lines
f = open('zipcodesheader.csv')
reader = csv.DictReader(f)
zipcodes = list(reader)
f.close()

# Sanity check
print(zipcodes[0])