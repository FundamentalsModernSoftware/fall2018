colors = []
color = input('Pick a color or type \'quit\': ')
while color != 'quit':
    colors = colors + [color]
    color = input('Pick a color or type \'quit\': ')
for color in colors:
    print('You picked: ' + color)
