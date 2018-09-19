allBooks = [{ 'isbn':  '978-0312429096', 'author': 'Richard Powers',
              'title': 'Gain'},
            { 'isbn': '978-0061624261', 'author': 'Douglas Coupland',
              'title': 'Microserfs'},
            { 'isbn': '978-0312429980', 'author': 'Hilary Mantel',
              'title': 'Wolf Hall'}]

for book in allBooks:
    print('A BOOK:')
    for key in book:
        print ('  '  + key + ': ' + book[key])
