class UserInput:

    def getCoffeType(self):
        for i in xrange(2):
            drink_number = raw_input(
                "Pick coffe drink or turn off coffee machine - type \'1\' if you want espresso, \'2\' for cappucino, \'3\' for latte macchiato or \'exit\' to turn off coffee machine: ")
            if drink_number == "1":
                drink_type = "espresso"
                return drink_type
            if drink_number == "2":
                drink_type = "capuccino"
                return drink_type
            if drink_number == "3":
                drink_type = "latte macchiato"
                return drink_type
            if drink_number == "exit":
                print "Coffee machine turned off"
                exit(0)
            else:
                if i == 0:
                    print "Wrong input. Try again"
                else:
                    print "Wrong input. Kawa nie moze zostac zrobiona"
        return False

    def getCoffeeStrength(self):
        for i in xrange(2):
            coffee_strength_number = raw_input("Pick coffee strength - type \' 1\' if you want weak coffee, \'2\' for normal lub \'3\' for strong coffee: ")
            if coffee_strength_number == "1":
                coffee_strength = 3
                return coffee_strength
            if coffee_strength_number == "2":
                coffee_strength = 5
                return coffee_strength
            if coffee_strength_number == "3":
                coffee_strength = 7
                return coffee_strength
            else:
                if i == 0:
                    print "Wrong input. Try again"
                else:
                    print "Wrong input. Coffee drink cannot be made"
        return False
