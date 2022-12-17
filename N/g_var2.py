#g_var2.py
#글로벌 변수

def cnt_num():
    global cnt
    cnt = cnt + 1
    print(cnt)

cnt = 0
cnt_num()
cnt_num()
cnt_num()
