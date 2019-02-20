# -*- coding: utf-8 -*-
import logging

from ascii_art import CoffeeDrinksAscii
from user_input import UserInput
from containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from drink_types import Espresso, Cappuccino, LatteMacchiato


coffee_available = 3  # TODO: uppercase - as a static values
water_available = 500
milk_available = 100
grounds_space = 4

coffeeContainer = CoffeeContainer(coffee_available)
waterContainer = WaterContainer(water_available)
milkContainer = MilkContainer(milk_available)
groundsContainer = GroundsContainer(grounds_space)

coffeeDrinksAscii = CoffeeDrinksAscii()

while True:

    logging.info(" === Containers state ===")
    print("{} grams of coffee beans in coffee grinder".format(coffeeContainer.how_many_ingredient_in_container()))
    print("{} ml of water in water container".format(waterContainer.how_many_ingredient_in_container()))
    print("{} ml of milk in milk container".format(milkContainer.how_many_ingredient_in_container()))
    print("Space for {} coffee grounds".format(groundsContainer.how_many_ingredient_in_container()))
    print(" ========================")

    userInput = UserInput()
    drink_type = userInput.get_coffee_type()
    coffee_strength = userInput.get_coffee_strength()

    logging.info(" ======= Containers preparing ======= ")
    coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=3, hide_drawings=True)
    waterContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=True)
    milkContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=True)
    groundsContainer.take_needed_ingredient_amount(needed_ingredient_amount=1, hide_drawings=True)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        espresso.make_espresso()

    if drink_type == "capuccino":
        cappuccino = Cappuccino(coffee_strength=coffee_strength)
        cappuccino.make_cappuccino()

    if drink_type == "latte macchiato":
        latte_macchiato = LatteMacchiato(coffee_strength=coffee_strength)
        latte_macchiato.make_latte_macchiato()
