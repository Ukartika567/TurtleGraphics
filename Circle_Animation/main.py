from turtle import *

# create obj of Turtle class 
t = Turtle()
scrn = Screen()
scrn.bgcolor(0,0,0)
scrn.title('Animation Graphics')
# t.pencolor('cyan')
t.color('cyan', 'blue')
# t.shape('turtle')

t.speed(0)
t.begin_fill()
for i in range(100):
    # Drawing circle
    t.circle(i*2)
    t._rotate(8) #turning turtle face 5 degree 
t.end_fill()
done()
