#14a_p2.py
# 계산 문제 만들기

import random

for x in range(5):
    n1 = random.randint(10,20)
    n2 = random.randint(10,20)
    op = random.randint(1,3)

    q= str(n1)

    if op == 1:
        q= q + '+'
    elif op == 2:
        q = q + '-'
    else:
        q = q + '*'

    q = q + str(n2)

    a= eval(q)

    print(f'{q}={a}')
