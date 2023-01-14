#ch06ex04.py

bs = ['파이썬', 'C', '캐드', '포토샵', 'JAVA', '엑셀']

bs.append('파워포인트')

print(bs)

bs.remove('JAVA')

print(bs)

bs.insert(4, '포토샵')

print(bs)

cnt = len(bs)
print(f'총 도서 {cnt}권')

b = input('대여할 책: ')
if b in bs:
    print('대여 가능')
else:
    print('대여 불가')
