# My Art

import time
from turtle import *
from random import *


def randomcolor():
    color(choice(colors))

def randomplace():
    x=randint(-200,200)
    y=randint(-200,200)
    goto(x,y)

def drawrectangle():
    l=randint(10,100)
    h=randint(10,100)
    begin_fill()
    forward(l)
    right(90)
    forward(h)
    right(90)
    forward(l)
    right(90)
    forward(h)
    right(90)
    end_fill()

def drawstar():
    l=randint(10,200)
    begin_fill()
    for i in range(5):
        forward(l)
        right(145)
    end_fill()    
        

colors=['black','blue','brown','gold','green','grey','orange','pink','purple','red','silver','yellow']

speed('fast')
penup()



for i in range(0,50):
    a=randint(1,5)
    shape("turtle")
    shapesize(a,a,a)
    randomcolor()
    randomplace()
    stamp()


time.sleep(2)

reset()
shape('classic')


hideturtle()
speed(0)
for i in range(0,50):
    randomcolor()
    pendown()
    drawrectangle()
    penup()
    randomplace()
    
time.sleep(2)
reset()

speed(0)
penup()
hideturtle()
for i in range(0,50):
    randomcolor()   
    dot(randint(10,100))
    randomplace()

time.sleep(2)
reset()

speed(0)
for i in range(0,50):
    penup()
    randomcolor()
    randomplace()
    pendown()
    drawstar()


time.sleep(2)


# The End
