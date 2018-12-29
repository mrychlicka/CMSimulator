from unittest import TestCase
from mock import patch
from code.UserInput import UserInput


class TestUserInput(TestCase):

    def testGetCoffeType1(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="1"):
            assert userInput.getCoffeType() == "espresso"

    def testGetCoffeType2(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="2"):
            assert userInput.getCoffeType() == "capuccino"

    def testGetCoffeType3(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="3"):
            assert userInput.getCoffeType() == "latte macchiato"

    def testGetCoffeType4(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="4"):
            assert not userInput.getCoffeType()

    def testGetCoffeType5(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="foo"):
            assert not userInput.getCoffeType()
    # ===================================================================================

    def TestGetCoffeeStrength1(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="1"):
            assert userInput.getCoffeeStrength() == 3

    def TestGetCoffeeStrength2(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="2"):
            assert userInput.getCoffeeStrength() == 5

    def TestGetCoffeeStrength3(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="3"):
            assert userInput.getCoffeeStrength() == 7

    def TestGetCoffeeStrength4(self):
        userInput = UserInput()
        with patch("__builtin__.raw_input", return_value="foo"):
            assert not userInput.getCoffeeStrength()