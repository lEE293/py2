#09c_p1.py
#random

import random

#1~30사이의 수를 생성해 변수 n1에 넣기
n1= random. randint(1,30)
print(n1)

#10~20 사이의 수를 생성해 변수 n2에 넣기
n2= random. randint(10,20)
print(n2)

#변수 quiz에 'n1 + n2 = ' 문자열 넣기
quiz=f'{n1} + {n2}='
print(quiz)

#정답을 ans 변수에 대입하기
ans= n1 + n2
print(ans)
