# Silent action program

from os import system
from art import logo
print(logo)

bids = {}
bidding = True

while bidding:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bids[name] = bid
    any_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if any_bidders == 'yes':
        system('cls')
    else:
        bidding = False

system('cls')

highest_bid = 0
winner = ''
for key in bids:
    if bids[key] > highest_bid:
        winner = key
        highest_bid = bids[key]

print(f'The winner is {winner} with a bid of ${highest_bid}')
