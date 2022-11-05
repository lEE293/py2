# ch04ex03.py
# 도형 그리기 함수

import turtle as t

def draw_poly(n,d,x,y):
    t.up()
    t.goto(x, y)
    t.down()

    for x in range(n):
        t.forward(d)
        t.left(360/n)

draw_poly(5, 50, 150, -150)
draw_poly(6, 70, 150, -150)
draw_poly(7, 90, 150, -150)
draw_poly(8, 110, 150, -150)
    
