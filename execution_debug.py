# -*- coding: utf-8 -*-
import logging.handlers

from ascii_art import CoffeeDrinksAscii
from user_input import UserInput
from containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from drink_types import Espresso, Cappuccino, LatteMacchiato

logging.basicConfig(level=logging.INFO)
coffee_available = 3  # TODO: uppercase - as a static values
water_available = 500
milk_available = 100
grounds_space = 4

coffee_container = CoffeeContainer(coffee_available)
water_container = WaterContainer(water_available)
milk_container = MilkContainer(milk_available)
grounds_container = GroundsContainer(grounds_space)

coffee_drinks_ascii = CoffeeDrinksAscii()

while True:

    logging.info(" === Containers state ===")
    print("{} grams of coffee beans in coffee grinder".format(coffee_container.how_many_ingredient_in_container()))
    print("{} ml of water in water container".format(water_container.how_many_ingredient_in_container()))
    print("{} ml of milk in milk container".format(milk_container.how_many_ingredient_in_container()))
    print("Space for {} coffee grounds".format(grounds_container.how_many_ingredient_in_container()))
    print(" ========================")

    user_input = UserInput()
    drink_type = user_input.get_coffee_type()
    coffee_strength = user_input.get_coffee_strength()

    logging.info(" ======= Containers preparing ======= ")
    coffee_container.take_needed_ingredient_amount(needed_ingredient_amount=3, hide_drawings=True)
    water_container.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=True)
    milk_container.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=True)
    grounds_container.take_needed_ingredient_amount(needed_ingredient_amount=1, hide_drawings=True)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        espresso.make_espresso()

    if drink_type == "capuccino":
        cappuccino = Cappuccino(coffee_strength=coffee_strength)
        cappuccino.make_cappuccino()

    if drink_type == "latte macchiato":
        latte_macchiato = LatteMacchiato(coffee_strength=coffee_strength)
        latte_macchiato.make_latte_macchiato()
