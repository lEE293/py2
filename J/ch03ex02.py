# ch03ex02.py
# BMI(체질량지수) 구하기

def bmi(t, w) :
    #bmi  구하기
    t = t/100
    b= w / (t * t)
    
    # 판정(yes) 구하기
    if b<20:
        res = '저체중'
    elif b<25:
        res = '정상'
    elif b < 30:
        res = '과체중'
    else:
        res = '비만'
    
    return res

print('체칠량지수(BMI) 구하기')
t = int(input('키: '))
w= int(input('몸무게: '))

r = bmi(t,w)

print(f'당신은 {r}입니다.')
