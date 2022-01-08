import random
from turtle import Turtle

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
INITIAL_STEPS = 5

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        flag = random.randint(1, 6)
        # lower the frequency of creating cars
        if flag == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y_position = random.randint(-250, 250)
            new_car.goto(280, random_y_position)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(INITIAL_STEPS)


