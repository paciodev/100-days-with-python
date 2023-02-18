# Calculator
from art import logo
print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1 = float(input("What's the first number?: "))

for key in operations:
    print(key)
operation = input('Pick an operation from the line above: ')
num2 = float(input(f"{num1} {operation} "))

answer = operations[operation](num1, num2)
print(f'{num1} {operation} {num2} = {answer}')



def next_operation():
    operation = input('Pick another operation: ')
    num3 = float(input(f"{answer} {operation} "))
    second_answer = operations[operation](answer, num3)
    print(f'{answer} {operation} {num3} = {second_answer}')

wants_to_operate = True
while wants_to_operate:
    is_another = input("Do you want to perform new action with current result? Type 'y' or 'n'\n")
    if is_another == 'y':
        next_operation()
    else:
        wants_to_operate = False