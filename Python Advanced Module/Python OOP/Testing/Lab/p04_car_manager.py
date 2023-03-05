class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTests(TestCase):
    def test_is_initialized_car_correct(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        self.assertEqual('Nissan', car.make)
        self.assertEqual('GT-R', car.model)
        self.assertEqual(15, car.fuel_consumption)
        self.assertEqual(75, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_with_empty_string_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_null_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.make = 0
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_null_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.model = 0
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -10
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_zero_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -10
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_zero_ex_raises(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_fuel_amount(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        car.refuel(80)
        self.assertEqual(75, car.fuel_amount)

    def test_refuel_with_correct_fuel_amount(self):
        car = Car('Nissan', 'GT-R', 15, 75)

        car.refuel(20)
        self.assertEqual(20, car.fuel_amount)

    def test_drive_with_no_enough_fuel_amount(self):
        car = Car('Nissan', 'GT-R', 15, 75)
        car.fuel_amount = 40

        with self.assertRaises(Exception) as ex:
            car.drive(300)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_amount(self):
        car = Car('Nissan', 'GT-R', 15, 75)
        car.fuel_amount = 70
        car.drive(300)
        self.assertEqual(25, car.fuel_amount)


if __name__ == '__main__':
    main()
