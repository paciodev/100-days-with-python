# Coffee Machine - project
from data import MENU
from os import system

system('cls')
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_machine_on = True
money = 0

def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for key in ingredients:
        if resources[key] < MENU[drink]['ingredients'][key]:
            return False
    return True

def get_money(drink):
    global money
    cost = MENU[drink]['cost']
    customer_money = 0

    print(f'    Please insert coins (${cost})')
    customer_money += int(input('How many quarters?: ')) * 0.25
    customer_money += int(input('How many dimes?: ')) * 0.10
    customer_money += int(input('How many Nickels?: ')) * 0.05
    customer_money += int(input('How many Pennies?: ')) * 0.01

    round(customer_money, 2)

    if customer_money < cost:
        return False
    change = customer_money - cost
    if change != 0:
        print(f"Here is ${change} in change.")
    
    money += cost
    return True

def make_coffee(coffee):
    for key in MENU[coffee]['ingredients']:
        resources[key] -= MENU[coffee]['ingredients'][key]

def get_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def serve():
    global is_machine_on
    client_choice = input(f"    What would you like? ({'/'.join(MENU)}): ").lower()
    system('cls')

    if client_choice == 'report':
        return get_report()
    
    if client_choice == 'off':
        system('cls')
        print('Turning off...')
        is_machine_on = False
        return

    if not check_resources(client_choice):
        return print('We have no resources to make your drink, please try another position from our list.')
    
    money = get_money(client_choice)
    if not money:
        return print("Sorry that's not enough money. Money refunded.")
    
    make_coffee(client_choice)

while is_machine_on:
    serve()