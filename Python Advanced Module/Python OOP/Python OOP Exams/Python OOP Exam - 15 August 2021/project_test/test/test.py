from project_test.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self):
        self.shop = PetShop('PetWorld')

    def test_shop_is_initialized_correct(self):
        self.assertEqual('PetWorld', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_when_quantity_is_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('meat', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_when_quantity_is_under_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('meat', -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_when_it_is_not_in_foods(self):
        result = self.shop.add_food('meat', 2)
        self.assertEqual("Successfully added 2.00 grams of meat.", result)
        self.assertEqual({'meat': 2}, self.shop.food)
        self.assertEqual(1, len(self.shop.food))

    def test_add_food_when_it_is_already_in_foods(self):
        self.shop.add_food('meat', 2)

        result = self.shop.add_food('meat', 3)

        self.assertEqual("Successfully added 3.00 grams of meat.", result)
        self.assertEqual({'meat': 5}, self.shop.food)
        self.assertEqual(1, len(self.shop.food))

    def test_add_pet_when_pet_is_not_in_shop(self):
        result = self.shop.add_pet('Kiki')

        self.assertEqual("Successfully added Kiki.", result)
        self.assertEqual(['Kiki'], self.shop.pets)
        self.assertEqual(1, len(self.shop.pets))

    def test_add_pet_when_pet_is_already_in_shop(self):
        self.shop.add_pet('Kiki')

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('Kiki')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

        self.assertEqual(['Kiki'], self.shop.pets)
        self.assertEqual(1, len(self.shop.pets))

    def test_feed_pet_when_pet_is_not_in_pets(self):
        self.shop.add_pet('Kiki')
        self.shop.add_food('meat', 2)

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('meat', 'Shushi')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_pet_is_not_in_pets_food_in_foods(self):
        self.shop.add_pet('Kiki')
        self.shop.add_food('meat', 2)

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('vegetables', 'Shushi')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_food_is_not_in_food(self):
        self.shop.add_pet('Kiki')
        self.shop.add_food('meat', 2)

        result = self.shop.feed_pet('vegetables', 'Kiki')
        self.assertEqual('You do not have vegetables', result)

    def test_feed_pet_when_adding_food(self):
        self.shop.add_pet('Kiki')
        self.shop.add_food('meat', 2)

        result = self.shop.feed_pet('meat', 'Kiki')
        self.assertEqual("Adding food...", result)
        self.assertEqual({'meat': 1002.0}, self.shop.food)

    def test_feed_pet_when_food_is_enough(self):
        self.shop.add_pet('Kiki')
        self.shop.add_food('meat', 105)

        result = self.shop.feed_pet('meat', 'Kiki')
        self.assertEqual("Kiki was successfully fed", result)
        self.assertEqual({'meat': 5}, self.shop.food)

    def test_repr_method(self):
        self.shop.add_pet('Kiki')
        self.shop.add_pet('Shushi')
        self.shop.add_food('meat', 105)

        result = 'Shop PetWorld:\nPets: Kiki, Shushi'
        self.assertEqual(result, str(self.shop))


if __name__ == '__main__':
    main()
