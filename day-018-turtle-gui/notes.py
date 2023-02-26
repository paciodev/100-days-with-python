from turtle import Turtle, Screen
from random import randrange, choice

t = Turtle()
t.shape('turtle')

screen = Screen()
screen.colormode(255)

def change_to_random_color():
    R = randrange(0,256,10)
    G = randrange(0,256,10)
    B = randrange(0,256,10)
    t.color(R, G, B)


# for i in range(4, 11):
#     change_to_random_color()
#     for _ in range(i):
#         t.forward(100)
#         t.right(360 / i)



# t.pensize(10)
# t.speed('fastest')
# directions = [0, 90, 180, 270]

# while True:
#     change_to_random_color()

    
#     t.right(choice(directions))
#     t.fd(50)


t.speed('fastest')

for i in range(0, 361, 10):
    change_to_random_color()
    t.circle(100)
    t.right(10)

screen.exitonclick()