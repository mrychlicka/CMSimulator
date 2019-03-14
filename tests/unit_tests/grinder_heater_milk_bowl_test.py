import unittest

from grinder_heater_milk_bowl import CoffeeGrinder, Heater, CoffeeBrewingBowl, MilkFrother


class TestGrinder(unittest.TestCase):
    def test_grind_coffee_1(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=4)
        self.assertTrue(coffeeGrinder.grind_coffee())

    def test_grind_coffee_2(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=0)
        self.assertFalse(coffeeGrinder.grind_coffee())

    def test_grind_coffee_3(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=-2)
        self.assertFalse(coffeeGrinder.grind_coffee())


class TestHeater(unittest.TestCase):
    def test_heat_water_1(self):
        self.heater = Heater()
        self.assertTrue(self.heater.heat_water())

    def test_heat_water_2(self):
        self.heater = Heater()
        self.assertTrue(self.heater.heat_water())

    def test_heat_water_3(self):
        self.heater = Heater()
        self.assertTrue(self.heater.heat_water())


class TestCoffeeBrewingBowl(unittest.TestCase):
    def test_brew_coffee_1(self):
        self.coffeeBrewingBowl = CoffeeBrewingBowl(coffee_ground=True, water_heated=True)
        self.assertTrue(self.coffeeBrewingBowl.brew_coffee())

    def test_brew_coffee_2(self):
        self.coffeeBrewingBowl = CoffeeBrewingBowl(coffee_ground=False, water_heated=True)
        self.assertFalse(self.coffeeBrewingBowl.brew_coffee())

    def test_brew_coffee_3(self):
        self.coffeeBrewingBowl = CoffeeBrewingBowl(coffee_ground=True, water_heated=False)
        self.assertFalse(self.coffeeBrewingBowl.brew_coffee())

    def test_brew_coffee_4(self):
        self.coffeeBrewingBowl = CoffeeBrewingBowl(coffee_ground=False, water_heated=False)
        self.assertFalse(self.coffeeBrewingBowl.brew_coffee())


class TestMilkFrother(unittest.TestCase):
    def test_pour_milk_1(self):
        self.milk_frother = MilkFrother(how_many_milk=100)
        self.assertTrue(self.milk_frother.pour_milk(steamed=False))

    def test_pour_milk_2(self):
        self.milk_frother = MilkFrother(how_many_milk=-400)
        self.assertFalse(self.milk_frother.pour_milk(steamed=False))

    def test_pour_milk_3(self):
        self.milk_frother = MilkFrother(how_many_milk=100)
        self.assertTrue(self.milk_frother.pour_milk(steamed=True))

    def test_pour_milk_4(self):
        self.milk_frother = MilkFrother(how_many_milk=-110)
        self.assertFalse(self.milk_frother.pour_milk(steamed=True))


if __name__ == '__main__':
    unittest.main()
