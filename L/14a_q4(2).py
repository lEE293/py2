#14a_q4.py
# 포멧을 사용한 문제 만들기

import random

def make_question():
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    op = random.randint(1,3)
    
    if op == 1:
        ops = '+'
    elif op == 2:
        ops = '-'
    else:
        ops = '*'

    q = f'{n1} {ops} {n2}'
    
    return q

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question()
    a= eval(q)
    # print(f'{q} = {a}')
    u = int(input(f'{q} = '))
    if u == a:
        print('정답!')
        sc1 = sc1 + 1
    else:
        print('오답!')
        sc2 = sc2 + 1

print("정답: ", sc1, "오답:", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")
    
