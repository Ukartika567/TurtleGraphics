from  turtle import *
# create obj of Turtle class 
t = Turtle()
scrn = Screen()
scrn.bgcolor(0,0,0)
# t.color('yellow', 'white')
t.pencolor('white')

a= 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
t.begin_fill()
while True:
    t.forward(a)
    t.right(b)
    a += 3
    print(a)
    b += 1
    print(b)
    if b == 200:
        break
    t.hideturtle()
    
t.end_fill()
done()