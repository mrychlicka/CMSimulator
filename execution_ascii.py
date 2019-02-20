# -*- coding: utf-8 -*-
import time
import logging

from console_progressbar import ProgressBar
from ascii_art import CoffeeDrinksAscii
from user_input import UserInput
from containers import CoffeeContainer, WaterContainer, MilkContainer, GroundsContainer
from drink_types import Espresso, Cappuccino, LatteMacchiato

coffee_available = 3
water_available = 500
milk_available = 100
grounds_space = 4

coffeeContainer = CoffeeContainer(coffee_available)
waterContainer = WaterContainer(water_available)
milkContainer = MilkContainer(milk_available)
groundsContainer = GroundsContainer(grounds_space)

coffeeDrinksAscii = CoffeeDrinksAscii()

logging.Logger.disabled = True

while True:

    logging.info(" ======= Containers state ======= ")
    containers = {coffeeContainer: coffeeContainer.how_many_ingredient_in_container(),
                  waterContainer: waterContainer.how_many_ingredient_in_container(),
                  milkContainer: milkContainer.how_many_ingredient_in_container(),
                  groundsContainer: groundsContainer.how_many_ingredient_in_container()}

    for container in containers:
        container.print_container_state_progres_bar(ingredient_available=containers[container])
        print("")
        time.sleep(1)

    userInput = UserInput()
    drink_type = userInput.get_coffee_type()
    coffee_strength = userInput.get_coffee_strength()

    pb1 = ProgressBar(total=100, prefix="Containers preparing", suffix="Complete", decimals=0, length=50, zfill='-')
    sleepTime = 0.7

    coffeeContainer.take_needed_ingredient_amount(needed_ingredient_amount=3, hide_debug_prints=True)
    pb1.print_progress_bar(20)
    time.sleep(sleepTime)

    waterContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=False, hide_debug_prints=True)
    pb1.print_progress_bar(40)
    time.sleep(sleepTime)

    milkContainer.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=False, hide_debug_prints=True)
    pb1.print_progress_bar(60)
    time.sleep(sleepTime)

    groundsContainer.take_needed_ingredient_amount(needed_ingredient_amount=1, hide_drawings=False, hide_debug_prints=True)
    pb1.print_progress_bar(80)
    time.sleep(sleepTime)

    pb1.print_progress_bar(100)
    coffeeDrinksAscii.print_coffee_machine()

    pb1 = ProgressBar(total=100, prefix="Coffee drink preparing", suffix="Complete", decimals=0, length=50, zfill='-')
    count = 0
    for i in range(5):
        count += 20
        pb1.print_progress_bar(count)
        time.sleep(sleepTime)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        with HiddenPrints():  # TODO: not existed class
            made_espresso = espresso.make_espresso()
        if made_espresso:
            coffeeDrinksAscii.print_espresso()

    if drink_type == "capuccino":
        cappuccino = Cappuccino(coffee_strength=coffee_strength)
        with HiddenPrints():
            made_cappuccino = cappuccino.make_cappuccino()
        if made_cappuccino:
            coffeeDrinksAscii.print_cappuccino()

    if drink_type == "latte macchiato":
        latte_macchiato = LatteMacchiato(coffee_strength=coffee_strength)
        with HiddenPrints():
            made_latte_macchiato = latte_macchiato.make_latte_macchiato()
        if made_latte_macchiato:
            coffeeDrinksAscii.print_latte_macchiato()
