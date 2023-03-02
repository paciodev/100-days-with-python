from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(xpos, 0)

    def go_up(self):
        if self.ycor() > 250:
            return
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() < -230:
            return
        y = self.ycor() - 20
        self.goto(self.xcor(), y)