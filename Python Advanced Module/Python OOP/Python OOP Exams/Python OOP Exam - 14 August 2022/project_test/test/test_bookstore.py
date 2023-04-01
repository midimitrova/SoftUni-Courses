from project_test.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(5)

    def test_is_initialized_correct(self):
        self.assertEqual(5, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_books_limit_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -5
        self.assertEqual("Books limit of -5 is not valid", str(ve.exception))

    def test_books_limit_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_books_limit_with_valid_value(self):
        self.assertEqual(5, self.store.books_limit)

    def test_count_books(self):
        self.store.availability_in_store_by_book_titles = {'Maugli': 3}
        self.assertEqual(3, len(self.store))

    def test_receive_book_with_not_enough_space(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Maugli', 6)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_with_enough_space(self):
        self.store.availability_in_store_by_book_titles = {'Maugli': 3}

        self.store.receive_book('Barbi', 2)

        self.assertEqual(5, len(self.store))
        self.assertEqual({'Maugli': 3, 'Barbi': 2}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_new_availability(self):
        result = self.store.receive_book('Maugli', 3)
        self.assertEqual("3 copies of Maugli are available in the bookstore.", result)

        result = self.store.receive_book('Maugli', 2)
        self.assertEqual("5 copies of Maugli are available in the bookstore.", result)
        self.assertEqual(5, len(self.store))

    def test_sell_book_when_book_not_available_in_store(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Barbi', 2)
        self.assertEqual("Book Barbi doesn't exist!", str(ex.exception))

    def test_sell_book_with_not_enough_copies(self):
        self.store.receive_book('Maugli', 3)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Maugli', 5)
        self.assertEqual("Maugli has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_correct(self):
        self.store.receive_book('Maugli', 3)

        result = self.store.sell_book('Maugli', 2)
        self.assertEqual("Sold 2 copies of Maugli", result)
        self.assertEqual(1, len(self.store.availability_in_store_by_book_titles))
        self.assertEqual(2, self.store.total_sold_books)

    def test_str_method(self):
        self.store.receive_book('Maugli', 3)
        self.store.sell_book('Maugli', 2)

        result = str(self.store)
        expected_result = "Total sold books: 2\nCurrent availability: 1\n - Maugli: 1 copies"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
