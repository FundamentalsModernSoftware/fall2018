# Read input.txt into the list
fIn = open('input.txt')
lines = fIn.read().splitlines()
fIn.close()

# Write the list in reverse to output.txt
fOut = open('output.txt', 'w')
for line in reversed(lines):
	print(line, file=fOut)
fOut.close()
