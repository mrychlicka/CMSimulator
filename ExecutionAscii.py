# -*- coding: utf-8 -*-
import time

from console_progressbar import ProgressBar


from ascii_art import CoffeeDrinksAscii
from UserInput import UserInput
from Containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from DrinkTypes import Espresso, Cappucino, LatteMacchiato
from HidePrint import HiddenPrints

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
    drink_type = userInput.get_coffee_type(hideDebugPrint=True)
    coffee_strength = userInput.get_coffee_strength()

    pb1 = ProgressBar(total=100, prefix="Containers preparing", suffix="Complete", decimals=3, length=50, zfill='-')
    sleepTime = 0.7
    # with HiddenPrints():
    coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=3, hideDebugPrints=True)  # TODO: zrobic parametr - ukryj obrazki, i ukryj printy debugujace
    pb1.print_progress_bar(20)
    time.sleep(sleepTime)

    # with HiddenPrints():
    waterContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hideDrawings=False, hideDebugPrints=True)
    pb1.print_progress_bar(40)
    time.sleep(sleepTime)

    # with HiddenPrints():
    milkContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hideDrawings=False, hideDebugPrints=True)
    pb1.print_progress_bar(60)
    time.sleep(sleepTime)

    # with HiddenPrints():
    groundsContainer.take_needed_ingredient_amount(needed_ingredient_amount=1, hideDrawings=False, hideDebugPrints=True)
    pb1.print_progress_bar(80)
    time.sleep(sleepTime)

    pb1.print_progress_bar(100)
    coffeeDrinksAscii.print_coffee_machine()


    pb1 = ProgressBar(total=100, prefix="Coffee drink preparing", suffix="Complete", decimals=3, length=50, zfill='-')
    count = 0
    for i in range(5):
        count += 20
        pb1.print_progress_bar(count)
        time.sleep(sleepTime)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        with HiddenPrints():
            made_espresso = espresso.make_espresso()
        if made_espresso:
            coffeeDrinksAscii.print_espresso()

    if drink_type == "capuccino":
        cappucino = Cappucino(coffee_strength=coffee_strength)
        with HiddenPrints():
            made_cappucino = cappucino.make_cappucino()
        if made_cappucino:
            coffeeDrinksAscii.print_capuccino()

    if drink_type == "latte macchiato":
        latteMacchiato = LatteMacchiato(coffee_strength=coffee_strength)
        with HiddenPrints():
            made_latte_macchiato = latteMacchiato.make_latte_macchiato()
        if made_latte_macchiato:
            coffeeDrinksAscii.print_latte_macchiato()
