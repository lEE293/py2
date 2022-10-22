#07c_timer.py
# 20초 맞히기

import time

input('엔터를 누르고 20초를 셉니다')

start = time. time() # 시작 시간

input('20초 후에 엔터를 누르세요')

end = time. time() # 종료 시간

et = int(end-start)
d = abs(20 - et)

print(f'실제시간 : {et}초')
print(f'차이 : {d}초')
