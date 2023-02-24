# Coffee machine but with OOP
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_turned_on = True
def serve():
    global machine_turned_on
    
    items = menu.get_items()
    choice = input(f"What would you like? ({items}): ").lower()
    if choice == 'off':
        system('cls')
        print('Bye!')
        machine_turned_on = False
        return
    
    if choice == 'report':
        coffee_maker.report()
        print('')
        machine.report()
        return
    
    drink = menu.find_drink(choice)
    if not drink:
        return
    
    if not coffee_maker.is_resource_sufficient(drink):
        return
    
    if not machine.make_payment(drink.cost):
        return

    coffee_maker.make_coffee(drink)

while machine_turned_on:
    serve()