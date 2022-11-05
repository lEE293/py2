# 13a_line.py
# 태극 모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(500):
    if x % 3 == 0:
        col = 'red'
    elif x % 3 == 1:
        col = 'yellow'
    elif x % 3 == 2:
        col == 'green'
    else:
        col = 'blue'

        

    # print(f'x: {x}, x % 3: {x % 3}, col: {col}')
    t.color(col)
    t.forward(x * 2)
    t.left(119)
