#16a_cannon.py
#대포 게임 만들기

import random
import turtle as t
def turn_up():
    ang = t. heading()
    if ang < 90:
        t.left(2)

def turn_down():
    ang = t.heading()
    if  ang > 90:
        t.right(2)
def prn_msg(msg, col):
    t.color(col)
    t.write(msg, False, 'Center', ('D2coding', 20))

def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(10)
        t.right(5)
    d = t.distance(tx, 0)
    if d < 25:
        prn_msg('GOOD', 'red')
    else:
        prn_msg('BAD!', 'blue')
        reset_cannon()
    

def draw_line(sx, sy, ex, ey):
    t.up()
    t.goto(sx, sy)
    t.down()
    t.goto(ex, ey)

def draw_target(sx, sy, ex, ey, ps, col):
    t.pensize(ps)
    t.color(col)
    draw_line(sx, sy, ex, ey)

def reset_cannon():
    t.up()
    t.color('black')
    t.goto(-200, 10)
    t.setheading(20)


#바닥그리기
draw_line(-300, 0, 300, 0)

#타겟 그리기
tx = random. randint(50, 150)
draw_target(tx - 25, 3, tx + 25, 3, 5, 'green')

#대포 초기화
reset_cannon()

#키 입력처리
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()

