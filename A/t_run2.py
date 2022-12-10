#t_run2.py
#터틀런

import turtle as t
import random

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_left():
    t.setheading(180)

def turn_right():
    t.setheading(0)

def play():
    t.forward(10)
    t.ontimer(play, 100)


t.setup(500, 500)
t.bgcolor('orange')

t.shape('turtle')
t.color('white')
t.speed(0)
t.up()

t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')

t.listen()

play()
