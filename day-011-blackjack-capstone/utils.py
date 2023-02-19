# Utility functions for project.py
import random

def get_random_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def generate_final_computer_cards(base_cards, users_score):
    final = base_cards
    if users_score < 21:
        while sum(final) < users_score and sum(final) < 20:
            final.append(get_random_card())
            print(final)
    return final

def divider():
    print('------------------------')

def check_game_status(user, dealer):
    if (user == dealer):
        return "You have the same value of cards. It's a draw!"
    if (user > 21):
        return "Unlucky! You have higher value of cards than 21. You lose!"
    if (dealer > 21):
        return "Nice one! Dealer has higher value of cards than 21. You win!"
    if (dealer == 21):
        return 'Ultra unlucky, Dealer has the BLACKJACK! You lose!'
    if (dealer > user):
        return "Unlucky! Dealer is closer to blackjack than you. You lose!"
    if (user == 21):
        return "BLACKJACK!!! You win!"
    return 'Nice one! You are closer to blackjack than dealer. You win!'