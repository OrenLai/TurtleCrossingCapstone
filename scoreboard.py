from turtle import Turtle

FONT = ("Comic Sans MS", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto((-280, 260))
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
