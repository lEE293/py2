#09c_p2_py
#덧셈 문제 맞히기

import random

#1. 문제 출제하기
n1 = random.randint(1,30)
n2 = random.randint(1,30)
quiz = f'{n1} + {n2} ='
#2. 정답 구하기
ans = n1 + n2
#3. 문제 묻기
user = int(input(quiz))
#4. 정답, 오답 판별하기
if user == ans:
    print('정답')
else:
    print('오답')
