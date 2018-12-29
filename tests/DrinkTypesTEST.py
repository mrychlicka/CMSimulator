from unittest import TestCase
from code.DrinkTypes import Espresso, Cappucino, LatteMacchiato


class TestDrinkTypes(TestCase):

    def test_make_espresso_1(self):
        self.espresso = Espresso(coffee_strength=3)
        self.assertTrue(self.espresso.make_espresso())

    def test_make_espresso_2(self):
        self.espresso = Espresso(coffee_strength=300)
        self.assertTrue(self.espresso.make_espresso())

    def test_make_espresso_3(self):
        self.espresso = Espresso(coffee_strength=-3)
        self.assertFalse(self.espresso.make_espresso())

    # ===================================================================================
    def test_make_cappucino_1(self):
        self.cappucino = Cappucino(coffee_strength=3)
        self.assertTrue(self.cappucino.make_cappucino())

    def test_make_cappucino_2(self):
        self.cappucino = Cappucino(coffee_strength=-3)
        self.assertFalse(self.cappucino.make_cappucino())

    # ===================================================================================
    def test_make_latte_macchiato_1(self):
        self.latteMacchiato = LatteMacchiato(coffee_strength=3)
        self.assertTrue(self.latteMacchiato.make_latte_macchiato())

    def test_make_latte_macchiato_2(self):
        self.latteMacchiato = LatteMacchiato(coffee_strength=-3)
        self.assertFalse(self.latteMacchiato.make_latte_macchiato())

    # ===================================================================================
