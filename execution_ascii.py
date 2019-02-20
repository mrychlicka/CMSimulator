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

coffee_container = CoffeeContainer(coffee_available)
water_container = WaterContainer(water_available)
milk_container = MilkContainer(milk_available)
grounds_container = GroundsContainer(grounds_space)

coffee_drinks_ascii = CoffeeDrinksAscii()

logging.Logger.disabled = True

while True:

    logging.info(" ======= Containers state ======= ")
    containers = {coffee_container: coffee_container.how_many_ingredient_in_container(),
                  water_container: water_container.how_many_ingredient_in_container(),
                  milk_container: milk_container.how_many_ingredient_in_container(),
                  grounds_container: grounds_container.how_many_ingredient_in_container()}

    for container in containers:
        container.print_container_state_progres_bar(ingredient_available=containers[container])
        print("")
        time.sleep(1)

    user_input = UserInput()
    drink_type = user_input.get_coffee_type()
    coffee_strength = user_input.get_coffee_strength()

    pb1 = ProgressBar(total=100, prefix="Containers preparing", suffix="Complete", decimals=0, length=50, zfill='-')
    sleep_time = 0.7

    coffee_container.take_needed_ingredient_amount(needed_ingredient_amount=3)
    pb1.print_progress_bar(20)
    time.sleep(sleep_time)

    water_container.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=False)
    pb1.print_progress_bar(40)
    time.sleep(sleep_time)

    milk_container.take_needed_ingredient_amount(needed_ingredient_amount=100, hide_drawings=False)
    pb1.print_progress_bar(60)
    time.sleep(sleep_time)

    grounds_container.take_needed_ingredient_amount(needed_ingredient_amount=1, hide_drawings=False)
    pb1.print_progress_bar(80)
    time.sleep(sleep_time)

    pb1.print_progress_bar(100)
    coffee_drinks_ascii.print_coffee_machine()

    pb1 = ProgressBar(total=100, prefix="Coffee drink preparing", suffix="Complete", decimals=0, length=50, zfill='-')
    count = 0
    for i in range(5):
        count += 20
        pb1.print_progress_bar(count)
        time.sleep(sleep_time)

    if drink_type == "espresso":
        espresso = Espresso(coffee_strength=coffee_strength)
        made_espresso = espresso.make_espresso()
        if made_espresso:
            coffee_drinks_ascii.print_espresso()

    if drink_type == "capuccino":
        cappuccino = Cappuccino(coffee_strength=coffee_strength)
        made_cappuccino = cappuccino.make_cappuccino()
        if made_cappuccino:
            coffee_drinks_ascii.print_cappuccino()

    if drink_type == "latte macchiato":
        latte_macchiato = LatteMacchiato(coffee_strength=coffee_strength)
        made_latte_macchiato = latte_macchiato.make_latte_macchiato()
        if made_latte_macchiato:
            coffee_drinks_ascii.print_latte_macchiato()
