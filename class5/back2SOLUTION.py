line = ['Anne', 'Betty', 'Clarissa', 'Doris', 'Eileen']
lostPlace = ['Doris', 'Betty']

for person in lostPlace:
    line.remove(person)
    line.append(person)

# line == ['Anne', 'Clarissa', 'Eileen', 'Doris', 'Betty']

# Print final state of line
print(line)