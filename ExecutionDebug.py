# -*- coding: utf-8 -*-
from ascii_art import CoffeeDrinksAscii
from UserInput import UserInput
from Containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from DrinkTypes import Espresso, Cappuccino, LatteMacchiato

coffee_available = 7
water_available = 300
milk_available = 400
grounds_space = 4

coffeeContainer = CoffeeContainer(coffee_available)
waterContainer = WaterContainer(water_available)
milkContainer = MilkContainer(milk_available)
groundsContainer = GroundsContainer(grounds_space)

coffeeDrinksAscii = CoffeeDrinksAscii()

while True:
    userInput = UserInput()
    drink_type = userInput.get_coffee_type()
    coffee_strength = userInput.get_coffee_strength()

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
