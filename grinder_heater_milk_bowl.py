import random
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)

class CoffeeGrinder:
    """Class represents grinder functionality"""

    def __init__(self, how_many_coffee):
        self.how_many_coffee = how_many_coffee

    def grind_coffee(self):
        """
        Grind coffee beans
        :return: True if grinder successfully, False otherwise
        """
        coffee_ground = False
        if not self.how_many_coffee <= 0:
            for i in range(self.how_many_coffee):
                logging.info("Grinding... Ground {} grams of coffee".format(i + 1))
            logging.info("Coffee grounded successfully")
            coffee_ground = True
        else:
            logging.info("[!!!] Grinding coffee failed")
        return coffee_ground


class Heater:
    """ Class represents water heater """

    def __init__(self):
        self.room_temperature_of_water = random.randint(15, 25)

    def _heat_water_to_95(self):
        """
        Heat water from room temperature (15-25C) to to 95C
        :return: True if heated successfully, False otherwise
        """
        limit = 0
        heating_water = self.room_temperature_of_water
        while heating_water <= 95 and limit < 81:
            yield heating_water
            heating_water += 1
            limit += 1

    def heat_water(self):
        """
        :return: True if heated successfully, False otherwise
        """
        heated = False
        for water_temperature in self._heat_water_to_95():
            if water_temperature % 5 == 0:
                logging.info("Water is heating. Temperature: {}".format(water_temperature))
            if water_temperature == 95:
                logging.info("Water heated to 95 C. Ready for brewing")
                heated = True
        return heated


class CoffeeBrewingBowl:
    """ Class represents coffee brewing bowl functionality """

    def __init__(self, coffee_ground, water_heated):
        self.coffee_ground = coffee_ground
        self.water_heated = water_heated

    def brew_coffee(self):
        """
        :return: True if coffee brewed successfully, False otherwise
        """
        brewed_coffee = self.coffee_ground and self.water_heated
        if brewed_coffee:
            logging.info("Coffee brewing successfully")
        else:
            logging.info("[!!!] Coffee brewing failed")
        return brewed_coffee


class MilkFrother():
    """ Class represents coffee milk frother functionality """

    def __init__(self, how_many_milk):
        self.how_many_milk = how_many_milk

    def _milk_frothing(self):
        """
        Steam milk
        :return: True if milk steamed, False otherwise
        """
        milk_is_frothed = False
        for i in range(self.how_many_milk):
            if i % 20 == 0:
                logging.info("Milk frothing...")
            if i == self.how_many_milk-1:
                logging.info("Milk frothed successfully")
                milk_is_frothed = True
        return milk_is_frothed

    def pour_milk(self, steamed=False):
        """
        :param boolean steamed: if True froth milk, False if not
        :return: True if milk poured to the cup, False otherwise
        """
        milk_in_cup = False
        if not self.how_many_milk <= 0:
            milk_in_cup = True
            if steamed:
                return self._milk_frothing() and milk_in_cup
            logging.info("Milk poured into a cup")
        return milk_in_cup
