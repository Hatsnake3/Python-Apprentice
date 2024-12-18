import turtle
import time
t = turtle.Turtle()
t.shape('arrow')
t.speed(0)
t.hideturtle()

s = turtle.Screen()

while True:
    for i in range(40):
        time.sleep(.5)
        if i % 2 == 0:
            s.bgcolor('red')
        else:
            s.bgcolor('green')

        t.penup()
        t.goto(0, -200)
        t.pendown()
        t.begin_fill()
        t.color('black')
        t.circle(80)
        t.end_fill()

        t.penup()
        t.goto(0, -40)
        t.pendown()
        t.begin_fill()
        t.color('black')
        t.circle(50)
        t.end_fill()

        t.penup()
        t.goto(0, 60)
        t.pendown()
        t.begin_fill()
        t.color('black')
        t.circle(30)
        t.end_fill()

        t.penup()
        t.goto(0, 75)
        t.pendown()
        t.begin_fill()
        t.color('blue')
        t.circle(7.5, steps = 3)
        t.end_fill()                                                         
        
        t.penup()
        t.goto(-12, 90)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(5)
        t.end_fill()

        t.penup()
        t.goto(12, 90)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(5)
        t.end_fill()

        t.penup()
        t.goto(0, 35)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(8)
        t.end_fill()

        t.penup()
        t.goto(0, 10)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(8)
        t.end_fill()

        t.penup()
        t.goto(0, -20)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(8)
        t.end_fill()

        t.penup()
        t.goto(0, -120)
        t.pendown()
        t.begin_fill()
        t.color('white')
        t.circle(15)
        t.end_fill()



