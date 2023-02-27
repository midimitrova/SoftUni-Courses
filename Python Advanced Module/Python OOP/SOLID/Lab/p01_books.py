class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'Book title {self.title} from {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        pass

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return 'Not found book'


my_library = Library()
for num in range(1, 21):
    book = Book(f'Title {num}', f'Author {num}')
    my_library.add_book(book)

print(my_library.find_book('Title 1'))
