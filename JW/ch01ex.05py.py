#ch01ex05.py
#BMI(체질량지수)

print('체질량지수(BMI) 구하기')
print()

t = int(input('키: '))
w = int(input('몸무게: '))

# 키를 m로 변환
t=t/100
bmi = w/ (t * t)

print()
print(f'당신의 체질량지수는 {bmi:.1f}입니다.')





