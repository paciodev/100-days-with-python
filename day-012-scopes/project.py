# Number Guessing Game
from os import system
from art import logo
from random import randint

def start_game():
    number = randint(1, 100)
    number_of_attempts = 10
    guess = 101

    system('cls')
    print(logo)
    print('Welcone to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'hard':
        number_of_attempts = 5

    while guess != number and number_of_attempts > 0:
        system('cls')
        print(logo)

        if guess == 101:
            print("Good luck!")
        elif guess < number:
            print('Too low')
            print('Guess again.')
        else:
            print('Too high')
            print('Guess again.')
        print(f'You have {number_of_attempts} attempts remaining to guess the number.')
        
        guess = int(input("Make a guess: "))
        if guess != number:
            number_of_attempts -= 1


    system('cls')
    print(logo)
    print('You win! Good job!')
    print(f"The number was {number}")
    print(f"You had {number_of_attempts - 1} attempts left to guess the number.")

    wants_to_play = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if wants_to_play == 'yes':
        start_game()

start_game()