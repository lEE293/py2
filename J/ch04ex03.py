# ch04ex03.py
# 도형 그리기 함수

import turtle as t

def draw_rect(x,y,d):
    t.up()
    t.goto(x,y)
    t.down()

    
    for x in range(4):
        t.forward(d)
        t.left(90)

def draw_tri(x,y,d):
    t.up()
    t.goto(x,y)
    t.down()

    
    for x in range(3):
        t.forward(d)
        t.left(120)

t.speed(0)
draw_rect(800, 800, 700)
draw_rect(-200, -200. 700)
draw_tri(-200, 200, 100)
draw_tri(200, -200, 100)
