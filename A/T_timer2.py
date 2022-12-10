#t_timer2.py

import random
import turtle as t

def run():
    t.forward(t_s)
    te.forward(te_s)
    ts.forward(ts_s)

    if t.xcor() < 300 and te.xcor() < 300 and ts.xcor() < 300:
        t.ontimer(run, 100)
t.setup(700, 300)
t.bgcolor('orange')

ts = t.Turtle()
ts.shape('turtle')
ts.color('red')
ts.up()
ts.goto(-300, -50)

te = t.Turtle()
te.shape('turtle')
te.color('blue')
te.up()
te.goto(-300, 0)

t.shape('turtle')
t.color('white')
t.up()
t.goto(-300, 50)

t_s = random.randint(3, 10)
te_s = random.randint(3, 10)
ts_s = random.randint(3, 10)

run()
