#ch08lab4.py

import random

n = []
c = 0

while c < 6:
    v = random. randint(1, 20)
    print(f'선택 수: {v}')

    if v not in n:
        n.append(v)
        c = c + 1

print(f'선택된 복권 번호 : {n}')
