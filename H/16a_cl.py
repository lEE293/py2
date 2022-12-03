#16a_cl.py
#배경 그리기

import turtle as t
import random

#각도 조절 함수
def turn_up():
    t.left(2)
def turn_up():
    t.right(2)
    

#바닥 그리기
t.goto(-300, 0)
t.goto(300, 0)

#타겟 그리기
tx = random.randint(50, 150)
print(f'타겟위치:  {tx}')
t.pensize(5)
t.color('green')
t.up()
t.goto(tx-25,3)
t.down()
t.goto(tx+25,3)

#대포 초기화
t.up()
t.color('black')
t.goto(-200, 10)
t.setheading(20)

#키 입력
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.listen()
