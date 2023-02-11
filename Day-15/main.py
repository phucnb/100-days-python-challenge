
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'quaters' : 0.25,
    'dimes' : 0.1,
    'nickles' : 0.05,
    'pennies' : 0.01
}

def main():
    while True:
        while True:
            drink = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
            if drink in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
                break
        if drink == 'report':
            print_report()
        elif drink == 'off':
            exit()
        else:
            if check_resource_for(drink) != 'enough':
                print(f"Sorry there is not enough {check_resource_for(drink)}")
            else:
                print(f"{drink.title()} is ${MENU[drink]['cost']}. Please insert coins:")
                total = process_coins()
                if not is_enough_money_for(drink, total)[0]:
                    print("Sorry that's not enough money. Money refunded.​")
                else:
                    change = is_enough_money_for(drink, total)[1]
                    if change > 0:
                        print(f"Here is ${change} dollars in change.")
                    update_profit(drink)
                    update_resources(drink)
                    print(f"Here is your {drink}. Enjoy!")
                
            
         
    
def print_report():
    for key, value in resources.items():
        print(f"{key.title()}: {value}{'ml' if key != 'coffee' else 'g'}")
    print(f"Money: ${profit}")

def check_resource_for(drink):
    for ingredient, value in MENU[drink]['ingredients'].items():
        if resources[ingredient] < value:
            return ingredient
    return 'enough'

def process_coins():
    total = 0
    for coin, value in coins.items():
        while True:
            try:
                quantity = int(input(f"How many {coin}?: "))
                break
            except:
                pass
        total += quantity * value
        print(f"Inserted ${round(total, 2)}")
    return round(total, 2)

def is_enough_money_for(drink, total):
    if total < MENU[drink]['cost']:
        return False, 0
    else:
        return True, round(total - MENU[drink]['cost'], 2)

def update_profit(drink):
    global profit
    profit += MENU[drink]['cost']

def update_resources(drink):
    for ingredient, value in MENU[drink]['ingredients'].items():
        resources[ingredient] -= value
        
if __name__ == "__main__":
    main()