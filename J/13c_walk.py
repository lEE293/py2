# 13c_walk.py
# 

import turtle as t

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_right():
    t.setheading(0)
    t.forward(10)

def p_up():
    t.up()
    t.color('red')

def p_down():
    t.up()
    t.color('black')

def ps1():
    t.pensize(1)

def ps5():
    t.pensize(5)

def ps10():
    t.pensize(10)

def blank():
    t.clear() #화면 지우기 


t.shape('turtle')
t.speed(0)

t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(p_up, 'u')
t.onkeypress(p_down, 'd')
t.onkeypress(ps1, '1')
t.onkeypress(ps5, '2')
t.onkeypress(ps10, '3')
t.listen()
