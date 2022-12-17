#t_run4.py
#터틀런

import random
import turtle as t

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
    print(f'먹이와 거리 : {d}px')
    if d < 20:
        ts_x = random.randint(-230, 230)
        ts_y = random.randint(-230, 230)
        ts.goto(ts_x, ts_y)

    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(5)

    d_te = t.distance(te)
    if d_te > 20:
        t. ontimer(play, 100)

t.setup(500, 500)
t.bgcolor('orange')

ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0, -200)

te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

t.shape('turtle')
t.color('white')
t.speed(0)
t.up()
t.goto(0, 0)

t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')

t.listen()
play()
