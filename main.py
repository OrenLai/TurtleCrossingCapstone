from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

# TODO : create the turtle player could control , and only be able to move up when player press Up key
# TODO : randomly generate cars from the right hand side of the screen and let it move toward left
# TODO : detect the collision of the car and turtle , if collision happened , everything stop, and game over
# TODO : if the turtle arrive the top of the screen, send it back to the start point and level up , increase car speed
# TODO : create scoreboard , that shows the score
