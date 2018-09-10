my_list = ['dog', 'cat', 'giraffe']
if input('Do you like animals? ') == 'yes':
    print('So do I!')
    for animal in my_list:
        print('I like ' + animal + 's')
else:
    print('Oh, well.')
