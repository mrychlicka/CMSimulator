from code.Containers import CoffeeContainer
from unittest import TestCase
from mock import patch


class TestCoffeeContainer(TestCase):

    def test_is_enough_ingredient_1(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=30)
        self.assertTrue(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=3))

    def test_is_enough_ingredient_2(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=3)
        self.assertFalse(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=4))

    def test_is_enough_ingredient_3(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=3)
        self.assertTrue(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=3))

    def test_is_enough_ingredient_4(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=-3)
        self.assertFalse(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=3))

    def test_is_enough_ingredient_5(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=3)
        self.assertFalse(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=-4))

    # ===================================================================================
    def test_refill_container_1(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=3)
        with patch("__builtin__.raw_input", return_value="y"):
            self.assertEqual(self.coffeeContainer._refill_container(), 120)

    def test_refill_container_2(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=-3)
        with patch("__builtin__.raw_input", return_value="y"):
            self.assertNotEqual(self.coffeeContainer._refill_container(), 23)

    # ===================================================================================
    def test_take_needed_amount_1(self):  # TODO: sekcja do poprawy
        self.coffeeContainer = CoffeeContainer(ingredient_available=20)
        with patch("__builtin__.raw_input", return_value="y"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=20), 0)

    def test_take_needed_amount_2(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=40)
        with patch("__builtin__.raw_input", return_value="foo"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=5), 35)

    def test_take_needed_amount_3(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=30)
        with patch("__builtin__.raw_input", return_value="4"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=20), 10)

