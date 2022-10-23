books = input().split('&')

command = input()
while command != 'Done':
    command = command.split(' | ')
    current_command = command[0]

    if current_command == 'Add Book':
        book = command[1]
        if book not in books:
            books.insert(0, book)
    elif current_command == 'Take Book':
        book = command[1]
        if book in books:
            books.remove(book)
    elif current_command == 'Swap Books':
        book_one = command[1]
        book_two = command[2]
        if book_one in books and book_two in books:
            index_one = books.index(book_one)
            index_two = books.index(book_two)
            books[index_one], books[index_two] = books[index_two], books[index_one]
    elif current_command == 'Insert Book':
        book = command[1]
        if book not in books:
            books.append(book)
    elif current_command == 'Check Book':
        index = int(command[1])
        if 0 <= index < len(books):
            print(books[index])
    command = input()

print(', '.join(books))





