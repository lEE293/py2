# 14a_p3.py
# 문제 생성 함수 make_question

import random

def make_question():
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    op = random.randint(1,3)

    q = str(n1)

    if op == 1:
        q = q + '+'
    elif op == 2:
        q = q + '-'
    else:
        q = q + '*'

    q= q + str(n2)
    return q


for x in range(5):
    q= make_question()
    a= eval(q)
    print(f'{q} = {a}')
