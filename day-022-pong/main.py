from turtle import *
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

bgcolor('black')
setup(800, 600)
title('Pong!')
tracer(0)  

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

listen()
onkeypress(l_paddle.go_up, 'w')
onkeypress(l_paddle.go_down, 's')
onkeypress(r_paddle.go_up, 'Up')
onkeypress(r_paddle.go_down, 'Down')

game_is_on = True

while game_is_on:
    sleep(ball.move_speed)
    update()
    ball.move()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_unit == 10 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_unit == -10:
        ball.x_unit *= -1
        ball.move_speed *= 0.9

    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.point_for_l()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.point_for_r()

done()