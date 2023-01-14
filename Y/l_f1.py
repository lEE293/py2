#l_f1.py
# 리스트 출력

s =[80, 90, 70, 60, 85]

for v in s:
    print(v)

print('-' * 30)

cnt = len(s)

for n in range(cnt):
    print(f'{n + 1}번 {s[n]}점')

print('-' * 30)

for i, v in enumerate(s):
    print(f'{i + 1} 번 {v} 점')
