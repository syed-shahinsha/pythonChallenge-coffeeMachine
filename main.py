from data import menu, resources

money = 0
is_on = True


def checkIngredientsAvailable(coffee_type):
    resp = {
        'ingredientsAvailable': True,
        'missingIngredient': ''
    }
    for item in menu[coffee_type]['ingredients']:
        if resources[item] < menu[coffee_type]['ingredients'][item]:
            resp = {
                'ingredientsAvailable': False,
                'missingIngredient': item
            }
        else:
            return resp


def processCoffee(coffee_type):
    response = {
        'coffeeProcessed': True,
        'remainingChange': 0
    }
    print(f"Price of {coffee_type} is ${menu[coffee_type]['cost']}. Please provide coins.")
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total < menu[coffee_type]['cost']:
        response['coffeeProcessed'] = False
        return response

    # if total amount is sufficient to process coffee
    for item in menu[coffee_type]['ingredients']:
        resources[item] -= menu[coffee_type]['ingredients'][item]

    # to refer money variable which is declared globally
    global money
    money += menu[coffee_type]['cost']

    response['remainingChange'] = total - menu[coffee_type]['cost']
    return response


while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    elif choice == 'off':
        is_on = False
    else:
        ingredientsCheckResponse = checkIngredientsAvailable(choice)
        if not ingredientsCheckResponse['ingredientsAvailable']:
            print(f"Sorry there isn't enough {ingredientsCheckResponse['missingIngredient']}!")
        else:
            cashCheckResponse = processCoffee(choice)
            if cashCheckResponse['coffeeProcessed']:
                print(f"Here's your remaining balance ${cashCheckResponse['remainingChange']}. Enjoy your {choice}!")
            else:
                print(f"Sorry, that's not enough money! Money refunded")
