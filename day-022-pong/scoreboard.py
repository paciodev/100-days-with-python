from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()
        
        self.l_score = 0
        self.r_score = 0

        self.write_scoreboard()
        
    def write_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Inter', 64, 'bold'))
        
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Inter', 64, 'bold'))

    def point_for_l(self):
        self.l_score += 1
        self.write_scoreboard()

    def point_for_r(self):
        self.r_score += 1
        self.write_scoreboard()