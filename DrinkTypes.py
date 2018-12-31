from GrinderHeaterMilkBowl import CoffeeGrinder, Heater, CoffeeBrewingBowl, MilkFrother


class Espresso:
    def __init__(self, coffee_strength):
        self.coffee = coffee_strength
        self.woda = 100
        self.coffeeGrinder = CoffeeGrinder(how_many_coffee=self.coffee)
        self.heater = Heater()

    def make_espresso(self):
        espressoInCup = False
        coffee_ground = self.coffeeGrinder.grid_coffee()
        water_heated = self.heater.heat_water()
        brewed_coffee = CoffeeBrewingBowl(coffee_ground=coffee_ground, water_heated=water_heated).brew_coffee()
        if brewed_coffee:
            print "Espresso is ready"
            espressoInCup = True
            return espressoInCup
        print "Making espresso failed"
        return espressoInCup


class Cappucino(Espresso):
    def __init__(self, coffee_strength):
        Espresso.__init__(self, coffee_strength)
        self.coffee = coffee_strength
        self.milk = 100

    def make_cappucino(self):
        espresso = self.make_espresso()
        steamed_milk = MilkFrother(howManyMilk=self.milk).pourMilk(steamed=True)
        return espresso and steamed_milk


class LatteMacchiato(Espresso):
    def __init__(self, coffee_strength):
        Espresso.__init__(self, coffee_strength)
        self.coffee = coffee_strength
        self.milk = 200

    def make_latte_macchiato(self):
        milkFrother = MilkFrother(howManyMilk=self.milk/2)
        no_steamed_milk = milkFrother.pourMilk(steamed=False)
        espresso = self.make_espresso()
        steamed_milk = milkFrother.pourMilk(steamed=True)
        return no_steamed_milk and espresso and steamed_milk
