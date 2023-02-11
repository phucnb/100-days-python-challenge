from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffe_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        while True:
            prompt = input(f"What would you like? ({menu.get_items()}): ")
            if prompt == 'report':
                coffe_maker.report()
                money_machine.report()
            elif prompt == 'off':
                exit()
            else:
                drink = menu.find_drink(prompt)
                if drink:
                    break
        if coffe_maker.is_resource_sufficient(drink):
            print(f"The cost for a {drink.name} is ${drink.cost}.")
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

if __name__ == "__main__":
    main()
