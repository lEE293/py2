#터틀런

import random
import turtle as t

score = 0
playing = False

def turn_up():
    t.setheading(90)
    
def turn_down():
    t.setheading(270)
    
def turn_left():
    t.setheading(180)
    
def turn_right():
    t.setheading(0)

def start():
    global playing
    if playing == False:
        t.clear()
        play()
        playing = True
    
def play():
    global score
    
    t.forward(10)

    if t. xcor() > 250:
        t.setx(-250)
    if t.xcor() < -250:
        t.setx(250)
    if t.xcor() > -250:
        t.setx(250)
    if t.xcor() < 250:
        t.setx(-250)
        

    d = t.distance(ts)
    print(f'먹이와 거리 :  {d} px')
    if d < 20:
        score = score + 1
        t.write(score)
        ts_x = random.randint(-230, 230)
        ts_y = random.randint(-230, 230)
        ts.goto(ts_x, ts_y)

    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(10)

    d_te = t.distance(te)
    if d_te > 20:
        t.ontimer(play, 100)

t.setup(500, 500)
t.bgcolor('orange')

te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0, -200)

t.shape('turtle')
t.color('white')
t.speed(0)
t.up()
t.goto(0, 0)

t.goto(0, 100)
t.write('TURTLE RUN!', False, 'center', ('D2coding', 35))
t.goto(0, -100)
t.write('[SPACE]', False, 'center', ('D2coding', 20))
t.goto(0, 0)


t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(start,'space')
t.listen()

