from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_is_initialized_vehicle_correct(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        distance = 10
        burned_fuel = distance * 1.25
        expected_result = self.vehicle.fuel - burned_fuel
        self.vehicle.drive(distance)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_with_incorrect_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_fuel_amount(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)
        self.assertEqual(100, self.vehicle.fuel)

    def test_str_method(self):
        result = f"The vehicle has 150 " \
                 f"horse power with 100 fuel left and 1.25 fuel consumption"
        expected_result = str(self.vehicle)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
