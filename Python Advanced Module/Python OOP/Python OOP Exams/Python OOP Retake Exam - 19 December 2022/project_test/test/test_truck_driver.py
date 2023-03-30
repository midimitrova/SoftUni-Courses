from project_test.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver('Ivan', 1.40)

    def test_is_initialized_correct(self):
        self.assertEqual('Ivan', self.truck_driver.name)
        self.assertEqual(1.40, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0.0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_are_validate_correct(self):
        self.truck_driver.earned_money = 5
        self.assertEqual(5, self.truck_driver.earned_money)

    def test_earned_money_under_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -5
        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_when_adding_cargo_location_again(self):
        self.truck_driver.available_cargos = {'Italy', 2000}

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer('Italy', 2000)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_when_adding_cargo_location_for_first_time(self):
        result = self.truck_driver.add_cargo_offer('France', 2000)

        expected_result = "Cargo for 2000 to France was added as an offer."
        self.assertEqual(expected_result, result)
        self.assertEqual({'France': 2000}, self.truck_driver.available_cargos)

    def test_bankrupt(self):
        self.truck_driver.money_per_mile = 0.01
        self.truck_driver.add_cargo_offer('Italy', 2000)

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.drive_best_cargo_offer()

        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_drive_vest_cargo_offer_correct(self):
        self.truck_driver.add_cargo_offer('Italy', 20000)
        self.truck_driver.add_cargo_offer('France', 2000)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual("Ivan is driving 20000 to Italy.", result)
        self.assertEqual(4000, self.truck_driver.earned_money)
        self.assertEqual(20000, self.truck_driver.miles)

    def test_drive_vest_cargo_offer_incorrect(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_eat(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        self.truck_driver.eat(500)

        self.assertEqual(60, self.truck_driver.earned_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(10, self.truck_driver.earned_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)

        self.assertEqual(1000, self.truck_driver.earned_money)

    def repair_truck(self):
        self.truck_driver.earned_money = 16000

        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(1000, self.truck_driver.earned_money)

    def test_repr(self):
        self.assertEqual("Ivan has 0 miles behind his back.", str(self.truck_driver))


if __name__ == '__main__':
    main()
