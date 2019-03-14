from unittest import TestCase
from mock import patch
from user_input import UserInput


class TestUserInput(TestCase):

    def test_get_coffe_type_1(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=1):
            assert userInput.get_coffee_type() == "espresso"

    def test_get_coffe_type_2(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=2):
            assert userInput.get_coffee_type() == "capuccino"

    def test_get_coffee_type_3(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=3):
            assert userInput.get_coffee_type() == "latte macchiato"

    def test_get_coffe_type_4(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=4):
            assert not userInput.get_coffee_type()

    def test_get_coffe_type_5(self):
        userInput = UserInput()
        with patch("builtins.input", return_value="foo"):
            assert not userInput.get_coffee_type()
    # ===================================================================================

    def test_get_coffee_strength_1(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=1):
            assert userInput.get_coffee_strength() == 3

    def test_get_coffee_strength_2(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=2):
            assert userInput.get_coffee_strength() == 5

    def test_get_coffee_strength_3(self):
        userInput = UserInput()
        with patch("builtins.input", return_value=3):
            assert userInput.get_coffee_strength() == 7

    def test_get_coffee_strength_4(self):
        userInput = UserInput()
        with patch("builtins.input", return_value="foo"):
            self.assertRaises(ValueError, userInput.get_coffee_strength())
