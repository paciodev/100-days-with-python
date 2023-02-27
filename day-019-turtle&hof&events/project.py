from turtle import *
from random import randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

setup(width=500, height=400)

bet = ''
while bet == '':
    bet = textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
    in_list = False
    
    for color in colors:
        if bet == color:
            in_list = True
    
    if in_list == False and bet != None:
        bet = ''

if bet != None:
    for i in range(len(colors)):
        turtle = Turtle()

        turtle.shape('turtle')
        turtle.color(colors[i])
        turtle.penup()

        y = (25 * i) - 50
        turtle.goto(x=-225, y=y)

        turtles.append(turtle)

    is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == bet.lower():
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    print(f"You've lost. The {winning_color} turtle is the winner")
            else:
                turtle.fd(randint(1, 10))

    exitonclick()