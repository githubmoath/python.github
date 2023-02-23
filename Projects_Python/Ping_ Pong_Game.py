#import turtle module
import turtle
#screen
wind= turtle.Screen()  
wind.title('Ping Pong')
wind.bgcolor('black')
wind.colormode('read')
wind.setup(width=800 , height=500)
wind.tracer(0)
#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape('square')
madrab1.shapesize(stretch_wid=4 ,stretch_len=1)
madrab1.penup()
madrab1.goto(-380,0)
madrab1.color('blue')
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape('square')
madrab2.shapesize(stretch_wid=4 ,stretch_len=1)
madrab2.penup()
madrab2.goto(380,0)
madrab2.color('red')
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.color('white')
ball.dx = 1.5
ball.dy = -1.5
#score
score1 =0
score2 =0
score=turtle.Turtle()
score.speed(0)
score.color('pink')
score.penup()
score.hideturtle
score.goto(0,220)
score.write('0 , 0',align='center' ,font=('Courier', 20, 'bold'))

def madrab1_up():
    y = madrab1.ycor()
    y +=50
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y -=50
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y +=50
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -=50
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab1_up, 'w')
wind.onkeypress(madrab1_down, 's')
wind.onkeypress(madrab2_up, 'Up')
wind.onkeypress(madrab2_down, 'Down')


while True:
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >240 :
        ball.sety(240)
        ball.dy *=-1

    if ball.ycor() <-240 :
        ball.sety(-240)
        ball.dy *=-1

    if ball.xcor() >390 :
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write('{} , {}'.format(score1, score2),align='center' ,font=('Courier', 20, 'bold'))


    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write('{} , {}'.format(score1, score2),align='center' ,font=('Courier', 20, 'bold'))


    if (ball.xcor() >360 and ball.xcor() <380)  and (ball.ycor() < madrab2.ycor()+35 and ball.ycor() > madrab2.ycor()-35  ):
        ball.setx(360)
        ball.dx *= -1
    if (ball.xcor() <-360 and ball.xcor() >-380)  and (ball.ycor() < madrab1.ycor()+35 and ball.ycor() > madrab1.ycor()-35  ):
        ball.setx(-360)
        ball.dx *= -1
#The_End