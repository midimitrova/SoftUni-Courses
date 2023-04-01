from project_test.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart('Test', 200)
        self.cart_two = ShoppingCart('TestTwo', 300)

    def test_is_initialized_correct(self):
        self.assertEqual('Test', self.cart.shop_name)
        self.assertEqual(200, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_with_no_upper_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'test'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_with_letters_and_digits(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'Test2'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_with_valid_data(self):
        self.assertEqual('Test', self.cart.shop_name)

    def test_add_to_cart_with_invalid_data_equal_to_price(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('pizza', 100.0)
        self.assertEqual("Product pizza cost too much!", str(ve.exception))

    def test_add_to_cart_with_invalid_data_more_than_price(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('pizza', 203.0)
        self.assertEqual("Product pizza cost too much!", str(ve.exception))

    def test_add_to_cart_with_valid_data(self):
        result = self.cart.add_to_cart('pizza', 50)
        self.assertEqual(1, len(self.cart.products))
        self.assertEqual({'pizza': 50}, self.cart.products)
        self.assertEqual("pizza product was successfully added to the cart!", result)

    def test_remove_from_cart_with_invalid_product_name(self):
        self.cart.add_to_cart('pizza', 50)
        self.cart.add_to_cart('chocolate', 20)

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('milk')
        self.assertEqual("No product with name milk in the cart!", str(ve.exception))

    def test_remove_from_cart_with_valid_product_name(self):
        self.cart.add_to_cart('pizza', 50)
        self.cart.add_to_cart('chocolate', 20)

        result = self.cart.remove_from_cart('pizza')

        self.assertEqual(1, len(self.cart.products))
        self.assertEqual({'chocolate': 20}, self.cart.products)
        self.assertEqual("Product pizza was successfully removed from the cart!", result)

    def test_add_method(self):
        self.cart.add_to_cart('pizza', 50)
        self.cart_two.add_to_cart('chocolate', 20)
        merged = self.cart.__add__(self.cart_two)
        self.assertEqual('TestTestTwo', merged.shop_name)
        self.assertEqual(500, merged.budget)
        self.assertEqual(2, len(merged.products))
        self.assertEqual({'pizza': 50, 'chocolate': 20}, merged.products)

    def test_buy_products_with_no_enough_budget(self):
        self.cart.budget = 100
        self.cart.add_to_cart('pizza', 50)
        self.cart.add_to_cart('chocolate', 80)

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 30.00lv!", str(ve.exception))

    def test_buy_products_with_enough_budget(self):
        self.cart.add_to_cart('pizza', 50)
        self.cart.add_to_cart('chocolate', 80)

        result = self.cart.buy_products()

        self.assertEqual('Products were successfully bought! Total cost: 130.00lv.', result)


    if __name__ == '__main__':
        main()
