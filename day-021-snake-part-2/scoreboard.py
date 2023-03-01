from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.color('white')
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Inter", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write(f"Final score: {self.score}", align='center', font=("Inter", 24, "bold"))
        self.goto(0, 0)
        self.write(f"Game over", align='center', font=("Inter", 24, "bold"))



