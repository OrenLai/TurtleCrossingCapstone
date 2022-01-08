from turtle import Screen
import time
from player import Player
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_on = True

# TODO : create the turtle player could control , and only be able to move up when player press Up key
player = Player()
# TODO : randomly generate cars from the right hand side of the screen and let it move toward left
cars = Cars()


def game_over():
    global game_on
    game_on = False
    print("Game over")


screen.onkey(game_over, "s")
screen.onkey(player.move_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

screen.exitonclick()


# TODO : detect the collision of the car and turtle , if collision happened , everything stop, and game over
# TODO : if the turtle arrive the top of the screen, send it back to the start point and level up , increase car speed
# TODO : create scoreboard , that shows the score
