#ch08lab3.py

zoo = ['곰', '강아지', '고양이', '사자',
       '호랑이', '여우', '늑대', '원숭이',
       '뱀', '코끼리']

like = []
hate = []

for one in zoo:
    a = input(f'{one} 좋아하세요?')
    if a == '네':
        like.append(one)
    else:
        hate.append(one)

print(f'좋아하는 동물: {like}')
print(f'싫어하는 동물: {hate}')
