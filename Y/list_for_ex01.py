#list_for_ex01.py

g = [80, 95, 77, 82, 99]

for v in g:
    print(v)

for i, v in enumerate(g):
    print(f'{i + 1} 번 {v} 점')
