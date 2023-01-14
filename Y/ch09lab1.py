#ch09lab.py
#가위, 바위, 보

import random

com = ['가위', '바위', '보']



def judge(u , c):
    if u == '가위':
        if c == '가위':
            j = 'draw'
        elif c =='바위':
            j = 'lose'
        else:
            j = 'win'
    if u == '바위':
        if c == '가위':
            j = 'lose'
        elif c =='바위':
            j = 'draw'
        else:
            j = 'win'
    if u == '보':
        if c == '가위':
            j = 'lose'
        elif c =='바위':
            j = 'win'
        else:
            j = 'draw'
    return j

com = ['가위', '바위', '보']


while True:
    u = input('가위바위보: ')
    c = random.choice(com)

    j = judge(u , c)

    print(f'사용자: {u}, 컴퓨터: {c}, {j}')

    
