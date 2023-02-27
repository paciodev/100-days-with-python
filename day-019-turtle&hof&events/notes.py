from turtle import *

def move_fd():
    fd(10)

def move_back():
    back(10)

def rotate_l():
    left(10)

def rotate_r():
    right(10)

listen()
onkey(key='w', fun=move_fd)
onkey(key='s', fun=move_back)
onkey(key='a', fun=rotate_l)
onkey(key='d', fun=rotate_r)
done()