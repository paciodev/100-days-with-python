from art import logo
from utils import get_random_card, generate_final_computer_cards, divider, check_game_status
from os import system

def start_game():
    system('cls')
    print(logo)

    users_cards = []
    computers_cards = []
    for _ in range(2):
        users_cards.append(get_random_card())
        computers_cards.append(get_random_card())

    print(f'Your cards: {users_cards}, current score: {sum(users_cards)}')
    print(f"Computer's first card: {computers_cards[0]}")

    y_or_n = input("Type 'y' to get another card, type 'n' to pass: ")
    wants_cards = False
    if y_or_n == 'y':
        wants_cards = True

    while wants_cards:
        system('cls')
        print(logo)
        users_cards.append(get_random_card())
        print(f'Your cards: {users_cards}, current score: {sum(users_cards)}')

        if sum(users_cards) > 21:
            wants_cards = False
        else:
            y_or_n = input("Type 'y' to get another card, type 'n' to pass: ")
            if y_or_n != 'y':
                wants_cards = False

    computers_cards = generate_final_computer_cards(computers_cards, sum(users_cards))
    system('cls')

    print(logo)
    print(f"Your final hand: {users_cards}, final score: {sum(users_cards)}")
    print(f"Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")
    divider()

    final_message = check_game_status(sum(users_cards), sum(computers_cards))
    print(final_message)
    divider()
    wants_to_play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if wants_to_play_again == 'y':
        start_game()
    else:
        print('Bye!')        

start_game()