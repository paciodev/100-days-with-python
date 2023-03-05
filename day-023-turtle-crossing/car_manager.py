from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5

class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self, lvl):
        rand_num = 7 - lvl
        if rand_num <= 2:
            rand_num = 2

        if random.randint(1, rand_num) != 1:
            return
        
        turtle = Turtle()
        turtle.shape('square')
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        turtle.penup()
        turtle.color(random.choice(COLORS))
        turtle.goto(x=300, y=random.randint(-250, 280))
        turtle.seth(180)
        self.cars.append(turtle)

    def move_cars(self, lvl):
        for i in range(len(self.cars)):
            car = self.cars[i]
            car.forward(lvl * MOVE_DISTANCE)
            if car.xcor() > 300:
                del self.cars[i]
