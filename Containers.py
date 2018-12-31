# -*- coding: utf-8 -*-
from ascii_art import CoffeeDrinksAscii


class Container:

    def __init__(self, ingredient_available):
        self.ingredient_available = ingredient_available
        self.max_ingredient_amount_in_container = None
        self.ingredient = "ingredient"
        self.coffeeDrinksAscii = CoffeeDrinksAscii()

    def _is_enough_ingredient(self, needed_ingredient_amount, hide_debug_prints=False):
        if not self.ingredient_available >= 0 or not needed_ingredient_amount >= 0:
            if not hide_debug_prints:
                print "[!!!] Number of available and needed %s cannot be negative" % self.ingredient
            return False
        if not self.ingredient_available >= needed_ingredient_amount:
            if not hide_debug_prints:
                print "[!!!] Not enough %s to make a coffe drink" % self.ingredient
            return False
        if not hide_debug_prints:
            print "Enough %s to make a coffe drink" % self.ingredient
        return True

    def _refill_container(self, hide_debug_prints=False):
        refilling = raw_input("Wrong %s amount. Please type \'y\' to refill: " % self.ingredient)
        if not refilling == "y":
            if not hide_debug_prints:
                print "[!!!] %s container is not ready. Cannot make coffee" % self.ingredient
            exit(0)
        self.ingredient_available = self.max_ingredient_amount_in_container
        if not hide_debug_prints:
            print "%s container is ready for making coffee" % self.ingredient
        return self.ingredient_available

    def _draw_empty_container(self):
        if self.ingredient == "coffee":
            self.coffeeDrinksAscii.print_coffee_beans()
        if self.ingredient == "water":
            self.coffeeDrinksAscii.print_water()
        if self.ingredient == "milk":
            self.coffeeDrinksAscii.print_milk()
        if self.ingredient == "ground space":
            self.coffeeDrinksAscii.print_trashcan()

    def take_needed_ingredient_amount(self, needed_ingredient_amount, hide_drawings=False, hide_debug_prints=False):
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
            print "Needed %s amount successfully taken" % self.ingredient
        return self.ingredient_available


class CoffeeContainer(Container):

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 300
        self.ingredient = "coffee"


class WaterContainer(Container):

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 200
        self.ingredient = "water"


class MilkContainer(Container):

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 300
        self.ingredient = "milk"


class GroundsContainer(Container):

    def __init__(self, ingredient_available):
        Container.__init__(self, ingredient_available)
        self.max_ingredient_amount_in_container = 8
        self.ingredient = "ground space"
