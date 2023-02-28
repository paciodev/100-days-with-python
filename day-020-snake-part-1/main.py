# Snake game
from turtle import *
from time import sleep
from snake import Snake

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

in_game = True
while in_game:
    update()
    sleep(0.1)

    snake.move()

done()
