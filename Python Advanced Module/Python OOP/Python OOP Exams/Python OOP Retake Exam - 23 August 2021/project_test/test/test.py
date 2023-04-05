from project_test.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library('Harmony')

    def test_is_library_initialized_correct(self):
        self.assertEqual('Harmony', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_when_error_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_name_when_is_written_correct(self):
        self.assertEqual('Harmony', self.library.name)

    def test_add_book_when_author_and_title_not_in_books(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.assertEqual({'James Clear': ['Atomic Habits']}, self.library.books_by_authors)

    def test_add_book_author_in_books(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.assertEqual({'James Clear': ['Atomic Habits']}, self.library.books_by_authors)

        self.library.add_book('James Clear', '30 Days to Better Habits')
        self.assertEqual({'James Clear': ['Atomic Habits', '30 Days to Better Habits']}, self.library.books_by_authors)

    def test_add_book_title_in_books(self):
        self.library.add_book('James Clear', 'Atomic Habits')

        self.library.add_book('James Clear', 'Atomic Habits')
        self.assertEqual({'James Clear': ['Atomic Habits']}, self.library.books_by_authors)

    def test_add_reader_when_name_not_in_readers(self):
        self.library.add_reader('Maria')
        self.assertEqual({'Maria': []}, self.library.readers)

    def test_add_reader_when_name_is_already_in_readers(self):
        self.library.add_reader('Maria')
        self.assertEqual({'Maria': []}, self.library.readers)

        result = self.library.add_reader('Maria')
        self.assertEqual("Maria is already registered in the Harmony library.", result)

    def test_rent_book_when_reader_not_in_readers(self):
        self.library.add_book('James Clear', 'Atomic Habits')

        result = self.library.rent_book('Maria', 'James Clear', 'Atomic Habits')
        self.assertEqual("Maria is not registered in the Harmony Library.", result)

    def test_rent_book_when_author_not_in_readers(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.library.add_reader('Maria')

        result = self.library.rent_book('Maria', 'Nikola Clear', 'Atomic Habits')
        self.assertEqual("Harmony Library does not have any Nikola Clear's books.", result)

    def test_rent_book_when_title_not_in_readers(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.library.add_reader('Maria')

        result = self.library.rent_book('Maria', 'James Clear', 'Habits')
        self.assertEqual("""Harmony Library does not have James Clear's "Habits".""", result)

    def test_rent_book_when_reader_author_title_not_exist(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.library.add_reader('Maria')

        result = self.library.rent_book('Natalia', 'Nikola Clear', 'Habits')
        self.assertEqual("Natalia is not registered in the Harmony Library.", result)
        # self.assertEqual("Harmony Library does not have any Nikola Clear's books.", result)
        # self.assertEqual("""Harmony Library does not have Nikola Clear's "Habits".""", result)

    def test_rent_book_when_reader_author_title_exist(self):
        self.library.add_book('James Clear', 'Atomic Habits')
        self.library.add_reader('Maria')

        self.library.rent_book('Maria', 'James Clear', 'Atomic Habits')

        self.assertEqual({'Maria': [{'James Clear': 'Atomic Habits'}]}, self.library.readers)
        self.assertEqual({'James Clear': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
