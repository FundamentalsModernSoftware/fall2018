import csv

# Read CSV file into lines
f = open('zipcodes.csv')
reader = csv.reader(f)
zipcodes = list(reader)
f.close()

# Make a list of states which have a locality named Springfield
# Put the list in a variable named states
# <Your code goes here>

print(states)