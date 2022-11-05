#ch05ex01.py
#태극모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(500):
    if x % 4 == 0:
        col = 'red'
    elif x % 4 == 1:
        col = 'yellow'
    elif x % 4 == 2:
        col = 'blue'
    else:
        col = 'green'

        
    # print(f'x: {x}, x % 3: {x % 3}, col: {col}')
    t.color(col)
    t.forward(x * 2)
    t.left(89)
