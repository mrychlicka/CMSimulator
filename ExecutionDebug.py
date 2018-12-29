# -*- coding: utf-8 -*-
from ascii_art import CoffeeDrinksAscii

from UserInput import UserInput
from Containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from DrinkTypes import Espresso, Cappucino, LatteMacchiato

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
    drink_type = userInput.getCoffeType()
    coffee_strength = userInput.getCoffeeStrength()

    coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=3, hideDrawings=True)
    waterContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hideDrawings=True)
    milkContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hideDrawings=True)
    groundsContainer.take_needed_ingredient_amount(needed_ingredient_amount=1, hideDrawings=True)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        espresso.make_espresso()

    if drink_type == "capuccino":
        cappucino = Cappucino(coffee_strength=coffee_strength)
        cappucino.make_cappucino()

    if drink_type == "latte macchiato":
        latteMacchiato = LatteMacchiato(coffee_strength=coffee_strength)
        latteMacchiato.make_latte_macchiato()
