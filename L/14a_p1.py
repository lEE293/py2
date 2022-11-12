# 14a_p1.py
# 덧셈 문제 만들기

import random

n1 = random.randint(1,20)
n2 = random.randint(1,30)
op = random.randint(1,3)

q = str(n1)

if op == 1:
    q = q + '+'
elif op == 2:
    q = q + '-'
else:
    q = q + '*'

q = q + str(n2)

print(q)
