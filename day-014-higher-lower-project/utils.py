# Utility functions for project.py
from art import vs

def choose(a, b):
    correct_answer = 'A'
    if a['follower_count'] < b['follower_count']:
        correct_answer = 'B'

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    print(f"Pssst! Correct answer is {correct_answer}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if answer == correct_answer:
        return True
    return False