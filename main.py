from turtle import *

# obj of turtle class 
t = Turtle() #open screen for few sec

# To change the screen attribute 
scrn = Screen() #obj of Screen class 
scrn.title('My First Graphics') #Change title name
# scrn.bgcolor(0.2,0.5,0.9) #change bg color
scrn.bgpic('492a36494fc89228bf30580f2387ff86.gif')
t.shape('turtle') #change shape
t.color('yellow','black') #pencolor, fillcolor

# Move turtle 
t.speed(1)
# t.hideturtle()

# Draw Ractangle
t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# using loop 
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()    
t.left(250)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
done()  #To hold the screen
