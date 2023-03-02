from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.color('white')
        self.penup()

        self.x_unit = 10
        self.y_unit = 10
        self.move_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_unit
        new_y = self.ycor() + self.y_unit
        self.goto(new_x, new_y)

        if self.ycor() > 280 or self.ycor() < -280:
            self.y_unit *= -1
            self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.x_unit *= -1
        self.move_speed = 0.1
