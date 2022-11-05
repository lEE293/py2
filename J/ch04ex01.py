# Ch04ex01.py
# 도형 그리기 함수

import turtle as t

def draw_rect():
    for x in range(4):
        t.forward(50)
        t.left(90)

def draw_tri():
    for x in range(3):
        t.forward(50)
        t.left(120)

for x in range(10):
    draw_rect()
    draw_tri()
    t.forward(50)
    t.down()
    draw_rect()
    draw_tri()
    t.forward(50)



