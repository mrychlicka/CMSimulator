from unittest import TestCase
from mock import patch
from code.UserInput import UserInput


class TestUserInput(TestCase):

    def testGetCoffeType1(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="1"):
            assert userInput.get_coffee_type() == "espresso"

    def testGetCoffeType2(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="2"):
            assert userInput.get_coffee_type() == "capuccino"

    def testGetCoffeType3(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="3"):
            assert userInput.get_coffee_type() == "latte macchiato"

    def testGetCoffeType4(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="4"):
            assert not userInput.get_coffee_type()

    def testGetCoffeType5(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="foo"):
            assert not userInput.get_coffee_type()
    # ===================================================================================

    def TestGetCoffeeStrength1(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="1"):
            assert userInput.get_coffee_strength() == 3

    def TestGetCoffeeStrength2(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="2"):
            assert userInput.get_coffee_strength() == 5

    def TestGetCoffeeStrength3(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="3"):
            assert userInput.get_coffee_strength() == 7

    def TestGetCoffeeStrength4(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="foo"):
            assert not userInput.get_coffee_strength()