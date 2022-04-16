from turtle import *
t = Turtle()
scrn = Screen()
scrn.bgcolor(0,0,0)
t.color('cyan','blue')
# t.pencolor('cyan')
t.speed(0)
t.hideturtle()   

t.penup()
t.goto(0,10)
t.pendown()
t.begin_fill()
for i in range(200):
    t.circle(190-i,50)
    t.left(900)
    t.circle(190-i,50)
    t.left(508)

t.end_fill()
mainloop()