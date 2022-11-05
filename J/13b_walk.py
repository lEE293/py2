# 13c_walk.py
# 거북이 그림판

import turtle as t

def turn_up():
    t.setheading(90)
    t.forward(10)

t.shape('turtle')
t.speed(0)

t.onkeypress(turn_up, 'Up')
t.listen()
