from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open(f"{__file__}/../high_score.txt") as f:
            self.high_score = int(f.read())

        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.update_scoreboard()
        self.ht()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align='center', font=("Inter", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{__file__}/../high_score.txt", 'w') as f:
                f.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()