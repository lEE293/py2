#16a_c3.py
#대포 조작

import random
import turtle as t

#각도 조절함수
def turn_up():
    ang = t.heading()
    if ang < 90:
        t.left(2)
    
def turn_down():
    t.right(2)

#발사 함수
def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
        #print(f'x: {t.xcor()}, y: {t.year()}')

    d= t.distance(target, 0)
    t.sety(random.randint(10, 100))
    if d <= 25:
        t.color('blue')
        t.write('GOOD', False, 'center', ('D2coding' ,20))
    else:
        t.color('red')
        t.write('BAD', False, 'center', ('D2coding' ,20))
        t.color('black')
        t.goto(-200,10)
        t.setheading(20)
#바닥 그리기
t.goto(-300, 0)
t.goto(300, 0)

#타겟 그리기 (50~150)
target = random.randint(50, 150)
t.up()
t.pensize(7)
t.color('blue')
t.goto(tx - 25, 3)
t.down()
t.goto(tx + 25, 3)

##대포 초기화
t.up()
t.color('black')
t.goto(-200, 10)
t.setheading(20)

#키 입력
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()
