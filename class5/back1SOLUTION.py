# Sample data
line = ['Anne', 'Betty', 'Clarissa', 'Doris', 'Eileen']
lostPlace = ['Doris', 'Betty']

# Go to the back of the line!
for person in lostPlace:
    line.remove(person)
    line.append(person)

# Print final state of line
print(line)
