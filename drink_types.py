from grinder_heater_milk_bowl import CoffeeGrinder, Heater, CoffeeBrewingBowl, MilkFrother


class Espresso:
    """ Class represents espresso coffee drink """

    def __init__(self, coffee_strength):
        self.coffee = coffee_strength
        self.water = 100
        self.coffeeGrinder = CoffeeGrinder(how_many_coffee=self.coffee)
        self.heater = Heater()

    def make_espresso(self):
        """
        Prepare espresso coffee drink
        Returns True if espresso prepared successfully, False otherwise
        """
        espressoInCup = False
        coffee_ground = self.coffeeGrinder.grind_coffee()
        water_heated = self.heater.heat_water()
        brewed_coffee = CoffeeBrewingBowl(coffee_ground=coffee_ground, water_heated=water_heated).brew_coffee()
        if brewed_coffee:
            print "Espresso is ready"
            espressoInCup = True
            return espressoInCup
        print "Making espresso failed"
        return espressoInCup


class Cappuccino(Espresso):
    """ Class represents cappuccino coffee drink """

    def __init__(self, coffee_strength):
        Espresso.__init__(self, coffee_strength)
        self.coffee = coffee_strength
        self.milk = 100

    def make_cappuccino(self):
        """
        Prepare cappuccino coffee drink
        Returns True if cappuccino prepared successfully, False otherwise
        """
        espresso = self.make_espresso()
        steamed_milk = MilkFrother(how_many_milk=self.milk).pour_milk(steamed=True)
        return espresso and steamed_milk


class LatteMacchiato(Espresso):
    """ Class represents latte macchiato coffee drink """

    def __init__(self, coffee_strength):
        Espresso.__init__(self, coffee_strength)
        self.coffee = coffee_strength
        self.milk = 200

    def make_latte_macchiato(self):
        """
        Prepare latte macchiato coffee drink
        Returns True if latte macchiato prepared successfully, False otherwise
        """
        milk_frother = MilkFrother(how_many_milk=self.milk/2)
        no_steamed_milk = milk_frother.pour_milk(steamed=False)
        espresso = self.make_espresso()
        steamed_milk = milk_frother.pour_milk(steamed=True)
        return no_steamed_milk and espresso and steamed_milk
