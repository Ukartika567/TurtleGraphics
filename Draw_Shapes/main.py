from turtle import *

# create obj of Turtle class 
t = Turtle()

# screen obj 
scrn = Screen()
scrn.bgcolor(0.0,0.0,0.0)
# scrn.colormode(50)
t.shape('turtle')
t.color('white', 'green')
t.hideturtle()
t.speed(1)

# Square 
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-270,-200)
t.pendown() 

# ractangle
for i in range(4):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-250, 130)
t.pendown()

# circle
t.circle(70)

t.penup()
t.goto(250,250)
t.pendown()

# line 
t.left(-135)
t.forward(150)
   
t.penup()
t.goto(200,-200)   
t.pendown()
# Triangle
t.left(135)
t.forward(100)
t.left(135)
t.forward(100)
t.left(113)
t.forward(78)
done()