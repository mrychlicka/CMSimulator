from unittest import TestCase
from mock import patch

from containers import CoffeeContainer


class TestCoffeeContainer(TestCase):

    def setUp(self):
        self.true_ingredient_available = (1, 4, 6, 0, 10)
        self.true_needed_ingredient_amount = (0, 3, 5, 0, 10)

        self.false_ingredient_available = (-1, 4, 2, -2.5, 9.9)
        self.false_needed_ingredient_amount = (3, -5, 3, 0, 10)

        self.max_ingredients = (30, 10, 50, 65, 2)

        self.returned_values = ("y", "e", 2, "-", "yy")

    def test_is_enough_ingredient(self):
        for i in range(len(self.true_ingredient_available)):

            self.coffeeContainer = CoffeeContainer(ingredient_available=self.true_ingredient_available[i])
            self.assertTrue(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=self.true_needed_ingredient_amount[i]))

            self.coffeeContainer = CoffeeContainer(ingredient_available=self.false_ingredient_available[i])
            self.assertFalse(self.coffeeContainer._is_enough_ingredient(needed_ingredient_amount=self.false_needed_ingredient_amount[i]))

    def test_refill_container(self):
        for i in range(len(self.true_ingredient_available)):

            self.coffeeContainer = CoffeeContainer(ingredient_available=self.true_ingredient_available[0])
            self.coffeeContainer.max_ingredient_amount_in_container = self.max_ingredients[i]
            with patch("__builtin__.raw_input", return_value="y"):
                self.assertEqual(self.coffeeContainer._refill_container(), self.max_ingredients[i])

            self.coffeeContainer = CoffeeContainer(ingredient_available=self.false_ingredient_available[0])
            self.coffeeContainer.max_ingredient_amount_in_container = self.max_ingredients[i]
            with patch("__builtin__.raw_input", return_value="y"):
                self.assertNotEqual(self.coffeeContainer._refill_container(), self.max_ingredients[i])

    def test_take_needed_amount(self):
        self.coffeeContainer = CoffeeContainer(ingredient_available=20)
        with patch("__builtin__.raw_input", return_value="y"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=20), 0)

        self.coffeeContainer = CoffeeContainer(ingredient_available=40)
        with patch("__builtin__.raw_input", return_value="foo"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=5), 35)

        self.coffeeContainer = CoffeeContainer(ingredient_available=30)
        with patch("__builtin__.raw_input", return_value="4"):
            self.assertEqual(self.coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=20), 10)

