from unittest import TestCase
from drink_types import Espresso, Cappuccino, LatteMacchiato


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
    def test_make_cappuccino_1(self):
        self.cappuccino = Cappuccino(coffee_strength=3)
        self.assertTrue(self.cappuccino.make_cappuccino())

    def test_make_cappuccino_2(self):
        self.cappuccino = Cappuccino(coffee_strength=-3)
        self.assertFalse(self.cappuccino.make_cappuccino())

    # ===================================================================================
    def test_make_latte_macchiato_1(self):
        self.latte_macchiato = LatteMacchiato(coffee_strength=3)
        self.assertTrue(self.latte_macchiato.make_latte_macchiato())

    def test_make_latte_macchiato_2(self):
        self.latte_macchiato = LatteMacchiato(coffee_strength=-3)
        self.assertFalse(self.latte_macchiato.make_latte_macchiato())

    # ===================================================================================
