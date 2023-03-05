from turtle import Turtle

BASIC_FONT = ("Courier", 24, "normal")
END_GAME_FONT = ("Courier", 36, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

        self.level = 1
        self.generate_score()

    def generate_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, 'left', BASIC_FONT)

    def level_up(self):
        self.level += 1
        self.generate_score() 

    def end_game(self):
        self.clear()
        self.write(f"Last level: {self.level}", False, 'left', BASIC_FONT)
        self.goto(0, 0)
        self.write(f"GAME OVER", False, 'center', END_GAME_FONT)
