import csv

# Read CSV file into lines
f_in = open('zipcodesheader.csv')
reader = csv.DictReader(f_in)
zipcodes = list(reader)
f_in.close()

headers = zipcodes[0].keys()
f_out = open('zipcodesheader_out.csv', 'w')
writer = csv.DictWriter(f_out, headers)
writer.writeheader()
writer.writerows(zipcodes)
f_out.close()