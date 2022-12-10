# t_timer.py
# 타이머 설정

import turtle as t

def run():
    t.forward(10)
    print(f'x: {t.xcor()}')
    if t.xcor() < 200:
        t.ontimer(run, 1000)

t.setup(600, 300)
t.bgcolor('orange')

t.shape('turtle')
t.color('white')
t.up()
t.goto(-250, 0)

run()



