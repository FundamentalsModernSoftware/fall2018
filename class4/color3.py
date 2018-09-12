colors = []
while True:
    color = input('Pick a color or type \'quit\': ')
    if color == 'quit':
        break
    else:
        colors = colors + [color]
print(colors)
