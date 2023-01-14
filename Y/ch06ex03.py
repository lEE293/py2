#ch06ex03.py

lec = ['python', 'c']

lec.append('office')
lec.append('cad')
lec.append('game')

print(lec)

lec.remove('game')

print(lec)

cnt = len(lec)

print(cnt)

if 'python' in lec:
    print('파이썬 포함')
