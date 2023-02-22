# Higher or lower game
import random
from data import data
from art import logo
from utils import choose
from os import system

account_a = random.choice(data)
account_b = random.choice(data)
score = 0
in_game = True

while account_a == account_b:
    account_b = random.choice(data)

while in_game:
    system('cls')
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    is_answer_good = choose(account_a, account_b)
    if not is_answer_good:
        in_game = False
    else:
        score += 1
        account_a = account_b
        account_b = random.choice(data)

system('cls')
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")