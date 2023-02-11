print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input('You see two paths in the forest left and right one. Type "left" if you want to go left or "right" if you want to go right\n')

if left_or_right.lower() == 'left':
    swim_or_wait = input('You see a little lake. Type "swim" if you want to swim through it or type "wait" if you want to wait for help.\n')
    if swim_or_wait.lower() == 'wait':
        which_door = input('You waited and someone took you in front of the three doors. Type "red" if you want to go through the red one, "blue" if you want to go through the blue one or "yellow" if you want to go through the yellow one.\n')
        if which_door.lower() == 'red':
            print('You burned yourself because the room was full of fire. Game Over.')
        elif which_door.lower() == 'blue':
            print('You were eaten by beasts. Game Over.')
        elif which_door.lower() == 'yellow':
            print('You win!')
        else:
            print("You didn't choose wisely. Game Over.")
    else:
        print('You have been attacked by trout. Game Over.')
else:
    print('You fell into a hole. Game over.')
