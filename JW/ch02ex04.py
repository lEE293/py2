#ch02ex04.py
#학점 계산기

score = int(input('점수을 입력하세요: '))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"당신의 학점은 '{grade}'입니다.")
