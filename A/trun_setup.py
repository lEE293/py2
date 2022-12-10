#Trun_setup.py

import turtle as t

t.setup(500, 500)
t.bgcolor('black')

te = t.Turtle()
te.shape('turtle')
te.color('red')
te.up()
te.goto(0, 200)
t.speed(0)

ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.up()
ts.goto(0, -200)
ts.speed(0)

t.shape('turtle')
t.color('white')
t.goto(0, 0)
t.speed(0)
