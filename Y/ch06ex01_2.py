#ch06ex01_2.py

cart = ['사과', '수박', '홈런볼' , '우유']

cart[1] = '멜론'
print(cart)

del cart[2]
print(cart)

cart.insert(2, '요거트')
print(cart)

cart.remove('요거트')
print(cart)

cnt = len(cart)
print(f'cart 원소의 개수 : {cnt}개')

j1 = '사과' in cart
j2 = '과자' in cart
print(j1 , j2)

if '우유' in cart:
    print('카트에 있다.')
else:
    print('카트에 없다.')
