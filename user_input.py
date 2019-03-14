import logging

from termcolor import cprint
from pyfiglet import figlet_format

logging.basicConfig(level=logging.INFO)


class UserInput:
    """ Class represents user input """

    def get_coffee_type(self, hide_ASCII=False):
        """
        Take user choice - which coffee drink wants to be done
        :param boolean hide_ASCII: if True ascii drawings is not shown, if False it is
        :return: typed coffee type, False if user input is wrong
        """
        drink_number = input("Pick coffe drink or turn off coffee machine - type \'1\' for espresso, \n"
                             "\'2\' - cappuccino, \'3\' - latte macchiato or "
                             "\'exit\' to turn off coffee machine: ")
        try:
            if drink_number not in (1, 2, 3, "exit"):
                raise ValueError
        except ValueError:
            logging.info("Wrong value. Type only specified values: 1, 2, 3 or exit")
            exit(0)

        else:
            drinks = {1: "espresso",
                      2: "capuccino",
                      3: "latte macchiato"}

            for key in drinks:
                if drink_number == key:
                    drink_type = drinks[key]
                    return drink_type

            if drink_number == "exit":
                if not hide_ASCII:
                    cprint(figlet_format("TURNED OFF", font="standard"), "white")
                logging.info("Coffee machine turned off")

    def get_coffee_strength(self):
        """
        Take user choice - coffee strength
        :return: typed coffee strength, False if user input is wrong
        """
        coffee_strength_number = input("Pick coffee strength - type \' 1\' if you want weak coffee, "
                                       "\'2\' for normal or \'3\' for strong coffee: ")
        try:
            if coffee_strength_number not in (1, 2, 3):
                raise ValueError
        except ValueError:
            logging.info(" Wrong value. Type only specified values: 1, 2 or 3")
            exit(0)
        else:
            strengths = {
                1: 3,
                2: 5,
                3: 7,
            }
            for key, val in strengths.items():
                if coffee_strength_number == key:
                    coffee_strength = val
                    return coffee_strength
