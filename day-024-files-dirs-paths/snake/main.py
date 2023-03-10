# Snake game
from turtle import *
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

setup(width=600, height=600)
bgcolor('black')
title('Snake Game')
tracer(0)

snake = Snake()

listen()
onkey(snake.up, 'Up')
onkey(snake.down, 'Down')
onkey(snake.left, 'Left')
onkey(snake.right, 'Right')

food = Food()
scoreboard = Scoreboard()

in_game = True
while in_game:
    update()
    sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh_pos()
        scoreboard.increase_score()
        snake.extend_snake()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

exitonclick()