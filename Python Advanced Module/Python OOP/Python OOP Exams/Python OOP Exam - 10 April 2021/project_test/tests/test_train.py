from unittest import TestCase, main

from project_test.project.train.train import Train


class Tests(TestCase):
    def setUp(self):
        self.train = Train("Express", 100)

    def test_is_train_initialized_correct(self):
        self.assertEqual("Express", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_passenger_if_train_full_raises(self):
        self.train.capacity = 1
        self.train.passengers.append("Boris")

        with self.assertRaises(ValueError) as ex:
            self.train.add("Ivan")

        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(["Boris"], self.train.passengers)

    def test_add_invalid_passenger(self):
        self.train.passengers.append("Boris")

        with self.assertRaises(ValueError) as ex:
            self.train.add("Boris")

        self.assertEqual("Passenger Boris Exists", str(ex.exception))
        self.assertEqual(["Boris"], self.train.passengers)

    def test_add_success(self):
        train = Train("Express", 100)

        result = train.add("Boris")
        self.assertEqual("Added passenger Boris", result)
        self.assertEqual(["Boris"], train.passengers)

        result = train.add("Ivan")
        self.assertEqual("Added passenger Ivan", result)
        self.assertEqual(["Boris", "Ivan"], train.passengers)

    def test_remove_invalid_passenger_raises(self):
        train = Train("Express", 100)
        result = train.add("Boris")

        with self.assertRaises(ValueError) as ex:
            train.remove("Ivan")

        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["Boris"], train.passengers)

    def test_remove_passenger_success(self):
        result = self.train.add("Boris")
        result = self.train.add("Ivan")

        result = self.train.remove("Boris")

        self.assertEqual("Removed Boris", result)
        self.assertEqual(["Ivan"], self.train.passengers)

        result = self.train.remove("Ivan")

        self.assertEqual("Removed Ivan", result)
        self.assertEqual([], self.train.passengers)


if __name__ == "__main__":
    main()