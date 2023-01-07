#t.run5.py
#터틀런

import turtle as t
import random

def set_turtle(tn, ts, tc, tx, ty):
    tn.shape(ts)
    tn.color(tc)
    tn.speed(0)
    tn.up()
    tn.goto(tx, ty)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_left():
    t.setheading(180)

def turn_right():
    t.setheading(0)

def game_init():
    global score
    score = 0
    set_turtle(te, 'turtle', 'red', 0, 200)
    set_turtle(ts, 'circle', 'green', 0, -200)
    set_turtle(t, 'turtle', 'white', 0, 0)

def message(m1, m2):
    t.up()
    t.speed(0)
    t.goto(0, 100)
    t.write(m1, False, 'center', ('D2Coding', 30))
    t.goto(0, -100)
    t.write(m2, False, 'center', ('D2coding', 20))

def check_feed():
    global score
    d = t.distance(ts)
    if d < 15:
        score += 1
        t.write(score)
        ts_x = random.randint(-230, 230)
        ts_y = random.randint(-230, 230)
        ts.goto(ts_x, ts_y)
        
def move_enemy():
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        if ang < 90:
            ang = 0
        elif ang < 180:
            ang = 90
        elif ang < 270:
            ang = 180
        else:
            ang = 270
        te.setheading(ang)
    te_speed = score + 5
    if te_speed > 20:
        te_speed = 20
    te.forward(te_speed)

def check_enemy():
    global playing
    d = t.distance(te)
    if d < 15:
        playing = False
        message('GAME OVER', f'SCORE: {score}')
        game_init()
        
def play():
    global playing
    
    t.forward(10)
    check_feed()
    move_enemy()
    check_enemy()
    
    d = t.distance(te)
    if  d < 15:
        playing = False
    if playing:
        t.ontimer(play, 100)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

playing = False


t.setup(500, 500)
t.bgcolor('orange')

te = t.Turtle()
ts = t.Turtle()
message('TURTLE RUN', '[SPACE]')
game_init()

t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(start, 'space')
t.listen()
