import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print('Your choice:')
print(images[choice])

if choice > 2 or choice < 0:
    print('You typed an invalid number, you lose!')
else:
    computers_choice = random.randint(0, 2)
    print("Computer's choice:")
    print(images[computers_choice])


    if choice == computers_choice:
        print("It's a draw!")
    elif choice == 0 and computers_choice == 1:
        print('You lose!')
    elif choice == 0 and computers_choice == 2:
        print('You win!')
    elif choice == 1 and computers_choice == 0:
        print('You win!')
    elif choice == 1 and computers_choice == 2:
        print('You lose!')
    elif choice == 2 and computers_choice == 0:
        print('You lose!')
    elif choice == 2 and computers_choice == 1:
        print('You win!')
    else:
        print('There was a problem. Please try again later.')

