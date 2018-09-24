import csv

# Read CSV file into lines
f_in = open('zipcodes.csv')
reader = csv.reader(f_in)
zipcodes = list(reader)
f_in.close()

f_out = open('zipcodes_out.csv', 'w')
writer = csv.writer(f_out)
writer.writerows(zipcodes)
f_out.close()