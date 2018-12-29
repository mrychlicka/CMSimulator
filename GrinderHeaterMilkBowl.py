from Containers import Container, WaterContainer, CoffeeContainer, MilkContainer, GroundsContainer
import random


class CoffeeGrinder:
    def __init__(self, how_many_coffee):
        self.how_many_coffee = how_many_coffee

    def grid_coffee(self):  # TODO: ta metoda wyglada bardzo prymitywnie
        coffee_ground = False
        if not self.how_many_coffee <= 0:
            for i in xrange(self.how_many_coffee):
                print "Grinding... Ground %s grams of coffee" % (i + 1)
            print "Coffee grounded successfully"
            coffee_ground = True
        print "[!!!] Grinding coffee failed"
        return coffee_ground


class Heater:
    def __init__(self):
        self.room_temperature_of_water = random.randint(15, 25)

    def _heat_water_to_95(self):
        limit = 0
        heating_water = self.room_temperature_of_water
        while heating_water <= 95 and limit < 81:
            yield heating_water
            heating_water += 1
            limit += 1

    def heat_water(self):
        heated = False
        for water_temperature in self._heat_water_to_95():
            if water_temperature % 5 == 0:
                print "Water is heating. Temperature: %s" % water_temperature
            if water_temperature == 95:
                print "Water heated to 95 C. Ready for brewing"
                heated = True
        return heated


class CoffeeBrewingBowl:
    def __init__(self, coffee_ground, water_heated):
        self.coffee_ground = coffee_ground
        self.water_heated = water_heated

    def brew_coffee(self):
        brewed_coffee = self.coffee_ground and self.water_heated
        if brewed_coffee:
            print "Coffee brewing successfully"
        else:
            print "[!!!] Coffee brewing failedy"
        return brewed_coffee


class MilkFrother():
    def __init__(self, howManyMilk):
        self.howManyMilk = howManyMilk

    def _milkFrothing(self):
        milkIsFrothed = False
        for i in xrange(self.howManyMilk):
            if i % 20 == 0:
                print "Milk frothing..."
            if i == self.howManyMilk-1:
                print "Milk frothed successfully"
                milkIsFrothed = True
        return milkIsFrothed

    def pourMilk(self, steamed=False):
        milkInCup = False
        if not self.howManyMilk <= 0:
            milkInCup = True
            if steamed:
                return self._milkFrothing() and milkInCup
            print "Milk poured into a cup"
        return milkInCup
