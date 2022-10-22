#09c_calc.py
#곱셈 문제 맞히기

import random

for x in range(100):
    n1= random.randint(1, 9)
    n2= random.randint(1, 9)
    quiz= f'{n1} * {n2}='


    ans= n1 * n2

    user = int(input(quiz))

    if user == ans:
       print('정답!')
    else:
       print('오답!')
     
