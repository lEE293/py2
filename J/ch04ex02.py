# ch04ex02.py
# 도형그리기 함수2

import turtle as t

def draw_rect(n):
    for x in range(4):
        t.forward(n)
        t,left(90)

def draw_tri(n):
    for x in range(3):
        t.forward(n)
        t.left(120)

draw_rect(100)
draw_rect(90)
draw_tri(50)
draw_tri(30)
        
