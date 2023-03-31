from project_test.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_is_initialized_correct(self):
        for key in range(ord('A'), ord('G') + 1):
            self.assertIsNone(self.toy_store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.toy_store.toy_shelf))

    def test_add_toy_when_shelf_do_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('Z', 'Barby')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_when_toy_is_already_on_shelf(self):
        self.toy_store.add_toy('A', 'Barby')

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Barby')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_when_shelf_is_already_taken(self):
        self.toy_store.add_toy('A', 'Barby')

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'Bear')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_when_there_are_no_errors(self):
        result = self.toy_store.add_toy('A', 'Barby')

        self.assertEqual("Toy:Barby placed successfully!", result)

    def test_remove_toy_when_shelf_do_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Z', 'Barby')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_when_toy_do_not_exists(self):
        self.toy_store.add_toy('A', 'Barby')

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'Bear')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_when_is_working_correct(self):
        self.toy_store.add_toy('A', 'Barby')
        result = self.toy_store.remove_toy('A', 'Barby')

        self.assertEqual("Remove toy:Barby successfully!", result)
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == '__main__':
    main()
