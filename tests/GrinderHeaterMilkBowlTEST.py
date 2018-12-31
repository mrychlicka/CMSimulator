import unittest

from code.GrinderHeaterMilkBowl import CoffeeGrinder, Heater, CoffeeBrewingBowl, MilkFrother


class TestGrinder(unittest.TestCase):
    def test_grind_coffee_1(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=4)
        self.assertTrue(coffeeGrinder.grid_coffee())

    def test_grind_coffee_2(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=0)
        self.assertFalse(coffeeGrinder.grid_coffee())

    def test_grind_coffee_3(self):
        coffeeGrinder = CoffeeGrinder(how_many_coffee=-2)
        self.assertFalse(coffeeGrinder.grid_coffee())


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
        self.milkFrother = MilkFrother(howManyMilk=100)
        self.assertTrue(self.milkFrother.pourMilk(steamed=False))

    def test_pour_milk_2(self):
        self.milkFrother = MilkFrother(howManyMilk=-400)
        self.assertFalse(self.milkFrother.pourMilk(steamed=False))

    def test_pour_milk_3(self):
        self.milkFrother = MilkFrother(howManyMilk=100)
        self.assertTrue(self.milkFrother.pourMilk(steamed=True))

    def test_pour_milk_4(self):
        self.milkFrother = MilkFrother(howManyMilk=-110)
        self.assertFalse(self.milkFrother.pourMilk(steamed=True))


if __name__ == '__main__':
    unittest.main()
