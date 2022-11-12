#14a_cale.py
#계산 문제 맞히기

import time
import random

def make_question():
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    op = random.randint(1,3)

    if op == 1:
        ops = '+'
    elif op == 2:
        ops = '-'
        if n1 < n2:
            n1, n2 = n2, n1
    
    else:
        ops = '*'
    q =f'{n1} {ops} {n2}'
    
    return q
n = 5
sc1 = 0
sc2 = 0
start = time.time()
for x in range(n):
    q = make_question()
    a = eval(q)
    u = int(input(f'{q} = '))
    if u == a:
        print('정답!')
        sc1 = sc1 + 1
    else:
        print('오답!')
        sc2 = sc2 + 1
end = time. time()
et = end - start

print(f'풀이시간: {et:.1f}초')
print("정답: ", sc1, "오답:", sc2)
if sc2 == 0 and et < 20:
    print("천재!")

    
