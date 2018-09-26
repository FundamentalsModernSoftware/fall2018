import csv

# Read CSV file
f_in = open('zipcodesheader.csv')
reader = csv.DictReader(f_in)
zipcodes = list(reader)
f_in.close()

# Write CSV file
f_out = open('zipcodesheader_out.csv', 'w')
writer = csv.DictWriter(f_out, reader.fieldnames)
writer.writeheader()
writer.writerows(zipcodes)
f_out.close()