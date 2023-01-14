#ch06ex01.py
# 카트 리스트

cart = []

cart.append('사과')
cart.append('수박')
print(cart, '리스트에 원소 추가')

pack = []
pack.append('홈런볼')
pack.append('우유')
print(pack)

print(cart + pack)

cart = cart + pack
print(cart)
