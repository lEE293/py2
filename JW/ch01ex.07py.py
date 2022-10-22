#ch01ex07.py
#bmi(체질량지수)

print('체질량지수(BMI) 구하기')
print()

t = int(input('키 : '))
w = int(input('몸무게 : '))

t=t/100
bmi = w/ (t*t)

if bmi < 20:
    res = '저체중'
elif bmi < 25:
    res = '정상'
elif bmi < 30:
    res = '과체중'
else:
    res = '비만'
    


print()
print(f'당신의 체질량지수는 {bmi:.1f}입니다.')
print(f'당신은 {res}입니다.')
