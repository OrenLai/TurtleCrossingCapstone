from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_on = True

# TODO : create the turtle player could control , and only be able to move up when player press Up key
player = Player()
# TODO : randomly generate cars from the right hand side of the screen and let it move toward left
car_manager = CarManager()
# TODO : create scoreboard , shows final score when game over
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
# TODO : detect the collision of the car and turtle , if collision happened , everything stop, and game over
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

# TODO : turtle arrive finish line, send it back to the start point and level up , increase car speed ,update level
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.level_up()
        scoreboard.update_level()


screen.exitonclick()
