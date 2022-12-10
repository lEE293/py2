#t_run.py

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

    d = t.distance(ts)

    if d < 20:
        ts_x = random.randint(-230, 230)
        ts_y = random.randint(-230, 230)
        ts.goto(ts_x, ts_y)

    ang = te.towards(t.xcor(), t.ycor())
    te.setheading(ang)
    te.forward(5)

    de = t.distance(te)
    if de >= 20:
        t.ontimer(play, 100)
    

t.setup(500, 500)
t.bgcolor('orange')

te = t.Turtle()
te.color('red')
te.shape('turtle')
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()
ts.color('green')
ts.shape('circle')
ts.up()
ts.speed(0)
ts.goto(0, -200)

t.color('white')
t.shape('turtle')
t.up()
t.speed(0)

t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.listen()

play()
