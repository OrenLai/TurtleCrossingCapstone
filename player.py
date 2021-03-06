from turtle import Turtle
STARTING_POSITION = (0, -290)
UP = 90
STEP_SIZE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset_position()
        self.setheading(UP)

    def move_up(self):
        self.forward(STEP_SIZE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
