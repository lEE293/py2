# g_var.py
# 전역변수, 지역변수

def func():
    a = 7
    print(f'func a: {a}')

def func2():
    print(f'func2 a: {a}')
a = 5
print(a)

func()
print(a)

func2()
