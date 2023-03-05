import time
from turtle import *
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

setup(width=600, height=600)
tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

onkeypress(player.move, 'Up')

listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    update()
    car_manager.create_car(scoreboard.level)
    car_manager.move_cars(scoreboard.level)

    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level_up()
        player.goto(STARTING_POSITION)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.end_game()

done()

