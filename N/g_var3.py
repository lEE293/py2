#g_var3.py
#초기화 함수
#init()
#init함수는 첫 실행 시
#'초기화를 진행합니다'
#두번째 이후 실행 시
#'이미 초기화하였습니다'

init_state = False

def init():
    global  init_state
    if init_state == False:
        print('초기화를 진행합니다.')
        init_state = True
    else:
        print('이미 초기화하였습니다')
    

init()
init()
init()
