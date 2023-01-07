#list01.py
#리스트 다루기

cart = []
cart.append('우유')
cart.append('아이스크림')
cart.append('사과')

print(cart)

cart.remove('아이스크림')
print(cart)

cart.append('홈런볼')
cart.append('바나나')

print(cart)

cart.remove('홈런볼')
print(cart)

cart.insert(1, '딸기')
print(cart)

cart.insert(3, '귤')
print(cart)
