# -*- coding: utf-8 -*-
import logging

from console_progressbar import ProgressBar
from ascii_art import CoffeeDrinksAscii


class Container:
    """ Class represents base functionality of containers """

    def __init__(self, ingredient_available):
        self.ingredient_available = ingredient_available
        self.max_ingredient_amount_in_container = None
        self.ingredient = "ingredient"
        self.coffeeDrinksAscii = CoffeeDrinksAscii()

    def how_many_ingredient_in_container(self):
        """
        Show container state
        :return: amount of ingredient in container
        """
        return self.ingredient_available

    def print_container_state_progres_bar(self, ingredient_available):
        """
        Show container state as percentage of max capacity of container with state bar
        :param str ingredient_available: amount of ingredient in container
        :return: None
        """


        max_ingredient = self.max_ingredient_amount_in_container
        how_many_ingredient = ingredient_available * 100 / max_ingredient
        pb1 = ProgressBar(total=100.0, prefix="%s state" % self.ingredient, suffix="in %s container capacity" % self.ingredient, fill="|", decimals=0, length=30, zfill='-')
        pb1.print_progress_bar(how_many_ingredient)

    def _is_enough_ingredient(self, needed_ingredient_amount):
        """
        Check if in container is enough of given ingredient
        :param int needed_ingredient_amount: how many ingredient is needed
        :return: True if in container is enough given ingredient, False otherwise
        """
        if not self.ingredient_available >= 0 or not needed_ingredient_amount >= 0:
            logging.debug("[!!!] Number of available and needed %s cannot be negative" % self.ingredient)
            return False
        if not self.ingredient_available >= needed_ingredient_amount:
            logging.debug("[!!!] Not enough %s to make a coffee drink" % self.ingredient)
            return False
        logging.debug("Enough %s to make a coffe drink" % self.ingredient)
        return True

    def _refill_container(self):
        """
        Fill or empty container
        :return: True if container filled successfully, False otherwise
        """
        refilling = input("Wrong {} amount. Please type 1 to refill: ".format(self.ingredient))
        if not refilling == 1:
            logging.debug("[!!!] %s container is not ready. Cannot make coffee" % self.ingredient)
            exit(0)
        self.ingredient_available = self.max_ingredient_amount_in_container
        logging.debug("%s container is ready for making coffee" % self.ingredient)
        return self.ingredient_available

    def _draw_empty_container(self):
        """
        Print ascii drawing of container to refill
        :return: None
        """
        if self.ingredient == "coffee":
            self.coffeeDrinksAscii.print_coffee_beans()
        if self.ingredient == "water":
            self.coffeeDrinksAscii.print_water()
        if self.ingredient == "milk":
            self.coffeeDrinksAscii.print_milk()
        if self.ingredient == "ground space":
            self.coffeeDrinksAscii.print_trashcan()

    def take_needed_ingredient_amount(self, needed_ingredient_amount, hide_drawings=False):
        """
        Update amount of available ingredient in container
        :param int needed_ingredient_amount: how many ingredient is needed
        :param boolean hide_drawings: if True ascii drawing is not shown, if False it is
        :return: updated amount of ingredient in container
        """
        if not self._is_enough_ingredient(
                needed_ingredient_amount=needed_ingredient_amount):
            if not hide_drawings:
                self._draw_empty_container()
            self.ingredient_available = self._refill_container()
            if not self.ingredient_available:
                return False
        else:
            self.ingredient_available -= needed_ingredient_amount
        logging.debug("Needed %s amount successfully taken" % self.ingredient)
        return self.ingredient_available


class CoffeeContainer(Container):
    """ Class represents coffee container """

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 30
        self.ingredient = "coffee"


class WaterContainer(Container):
    """ Class represents water container """

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 500
        self.ingredient = "water"


class MilkContainer(Container):
    """ Class represents milk container """

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 300
        self.ingredient = "milk"


class GroundsContainer(Container):
    """ Class represents container for grounds"""

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 8
        self.ingredient = "ground space"
