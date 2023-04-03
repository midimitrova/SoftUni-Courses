from project_test.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(10)

    def test_is_plantation_initialized_correct(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_when_is_raised_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -5
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_size_with_valid_data(self):
        self.assertEqual(10, self.plantation.size)

    def test_hire_worker_when_worker_already_hired(self):
        self.plantation.workers = ['Ivan']
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Ivan')
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_when_worker_added_for_first_time(self):
        result = self.plantation.hire_worker('Ivan')
        self.assertEqual("Ivan successfully hired.", result)
        self.assertEqual(1, len(self.plantation.workers))
        self.assertEqual(['Ivan'], self.plantation.workers)

    def test_len_method(self):
        self.plantation.hire_worker('Ivan')
        self.plantation.plants['Ivan'] = ['Tomatoes']
        result = len(self.plantation.plants)
        self.assertEqual(1, result)

    def test_len_not_addition(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Martin')
        self.plantation.hire_worker('Alexandra')
        self.plantation.plants['Martin'] = ['Tomatoes']
        self.plantation.plants['Alexandra'] = ['plant']
        self.assertEqual(2, self.plantation.__len__())

    def test_planting_when_worker_is_not_hired_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Ivan', 'Tomatoes')
        self.assertEqual("Worker with name Ivan is not hired!", str(ve.exception))

    def test_planting_when_plantation_is_full(self):
        self.plantation.size = 1
        self.plantation.hire_worker('Ivan')
        self.plantation.planting('Ivan', 'Tomatoes')

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Maria')
            self.plantation.planting('Maria', 'Bananas')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_when_worker_is_in_workers(self):
        self.plantation.hire_worker('Ivan')
        self.plantation.planting('Ivan', 'Tomatoes')

        result = self.plantation.planting('Ivan', 'Bananas')

        self.assertEqual("Ivan planted Bananas.", result)
        self.assertEqual(2, len(self.plantation))

    def test_plantation_when_worker_plant_for_first_time(self):
        self.plantation.hire_worker('Ivan')

        result = self.plantation.planting('Ivan', 'Tomatoes')

        self.assertEqual("Ivan planted it's first Tomatoes.", result)
        self.assertEqual(1, len(self.plantation))

    def test_str_method(self):
        self.assertEqual(Plantation(2).__str__().strip(), 'Plantation size: 2')
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Martin')
        self.plantation.planting('Martin', 'Radishes')
        self.assertEqual('Plantation size: 2\nMartin\nMartin planted: Radishes', self.plantation.__str__().strip())

    def test_repr_wrong_output(self):
        self.assertEqual(Plantation(2).__repr__().strip(), 'Size: 2\nWorkers:')
        self.plantation = Plantation(2)
        self.plantation.hire_worker('Martin')
        self.plantation.planting('Martin', 'Radishes')
        self.assertEqual('Size: 2\nWorkers: Martin', self.plantation.__repr__().strip())


if __name__ == '__main__':
    main()
