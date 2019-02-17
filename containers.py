# -*- coding: utf-8 -*-
from console_progressbar import ProgressBar
from ascii_art import CoffeeDrinksAscii


class Container:
    """ Class represents base functionality of containers"""

    def __init__(self, ingredient_available):
        self.ingredient_available = ingredient_available
        self.max_ingredient_amount_in_container = None
        self.ingredient = "ingredient"
        self.coffeeDrinksAscii = CoffeeDrinksAscii()

    def how_many_ingredient_in_container(self):
        """
        Show container state
        Returns amount of ingredient in container
        """
        return self.ingredient_available

    def print_container_state_progres_bar(self, ingredient_available):
        """
        Show container state as percentage of max capacity of container with state bar
        @ingredient_available: amount of ingredient in container
        Returns None
        """
        max_ingredient = self.max_ingredient_amount_in_container
        how_many_ingredient = ingredient_available * 100 / max_ingredient
        pb1 = ProgressBar(total=100.0, prefix="%s state" % self.ingredient, suffix="in %s container capacity" % self.ingredient, fill="|", decimals=0, length=30, zfill='-')
        pb1.print_progress_bar(how_many_ingredient)

    def _is_enough_ingredient(self, needed_ingredient_amount, hide_debug_prints=False):
        """
        Check if in container is enough of given ingredient
        @needed_ingredient_amount: int - how many ingredient is needed
        @hide_debug_prints: boolean - if True printed text is not shown, if False it is
        Returns True if in container is enough given ingredient, False otherwise
        """
        if not self.ingredient_available >= 0 or not needed_ingredient_amount >= 0:
            if not hide_debug_prints:
                print("[!!!] Number of available and needed %s cannot be negative" % self.ingredient)
            return False
        if not self.ingredient_available >= needed_ingredient_amount:
            if not hide_debug_prints:
                print("[!!!] Not enough %s to make a coffe drink" % self.ingredient)
            return False
        if not hide_debug_prints:
            print("Enough %s to make a coffe drink" % self.ingredient)
        return True

    def _refill_container(self, hide_debug_prints=False):
        """
        Fill or empty container
        @hide_debug_prints: boolean - if True printed text is not shown, if False it is:
        Returns True if container filled successfully, False otherwise
        """
        refilling = input("Wrong %s amount. Please type \'y\' to refill: " % self.ingredient)
        if not refilling == "y":
            if not hide_debug_prints:
                print("[!!!] %s container is not ready. Cannot make coffee" % self.ingredient)
            exit(0)
        self.ingredient_available = self.max_ingredient_amount_in_container
        if not hide_debug_prints:
            print("%s container is ready for making coffee" % self.ingredient)
        return self.ingredient_available

    def _draw_empty_container(self):
        """
        Print ascii drawing of container to refill
        Returns None
        """
        if self.ingredient == "coffee":
            self.coffeeDrinksAscii.print_coffee_beans()
        if self.ingredient == "water":
            self.coffeeDrinksAscii.print_water()
        if self.ingredient == "milk":
            self.coffeeDrinksAscii.print_milk()
        if self.ingredient == "ground space":
            self.coffeeDrinksAscii.print_trashcan()

    def take_needed_ingredient_amount(self, needed_ingredient_amount, hide_drawings=False, hide_debug_prints=False):
        """
        Update amount of available ingredient in container
        @needed_ingredient_amount: int - how many ingredient is needed
        @hide_drawings: boolean - if True ascii drawing is not shown, if False it is
        @hide_debug_prints: boolean - if True printed text is not shown, if False it is
        Returns updated amount of ingredient in container
        """
        if not self._is_enough_ingredient(
                needed_ingredient_amount=needed_ingredient_amount, hide_debug_prints=hide_debug_prints):
            if not hide_drawings:
                self._draw_empty_container()
            self.ingredient_available = self._refill_container(hide_debug_prints=hide_debug_prints)
            if not self.ingredient_available:
                return False
        else:
            self.ingredient_available -= needed_ingredient_amount
        if not hide_debug_prints:
            print("Needed %s amount successfully taken" % self.ingredient)
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