#trun01.py

import turtle as t

t.setup(500, 500)
t.bgcolor('orange')
#te 거북이
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.goto(100, 100)
te.forward(100)

#ts 거북이
ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.goto(-100, -100)
ts.forward(50)

#t 거북이
t.shape('turtle')
t.color('blue')
t.forward(150)
