# Turtle Race 



from random import randint
from turtle import *
hideturtle()
speed(50)

penup()
goto(-140,140)
right(90)
a=20

for i in range(15):
    write(i, align='center')
    forward(10)
   
    for j in range(7):
        pendown()
        forward(20)
        penup()
        forward(20)
    goto(-140+a,140)
    a=a+20

    
r=Turtle()
r.color('red')
r.shape('turtle')
r.penup()
r.goto(-160,100)

b=Turtle()
b.color('blue')
b.shape('turtle')
b.penup()
b.goto(-160,40)

g=Turtle()
g.color('green')
g.shape('turtle')
g.penup()
g.goto(-160,-20)

y=Turtle()
y.color('yellow')
y.shape('turtle')
y.penup()
y.goto(-160,-80)

r.pendown()
b.pendown()
g.pendown()
y.pendown()



while True :
    r.forward(randint(1,6))
    b.forward(randint(1,6))
    g.forward(randint(1,6))
    y.forward(randint(1,6))
    if r.xcor()>160 :
        result="red"
        break
    elif b.xcor()>160 :
        result="blue"
        break
    elif g.xcor()>160 :
        result="green"
        break
    elif y.xcor()>160:
        result="yellow"
        break



    



setpos(-100,-200)
color(result)

write("The Winner is : "+result,move=True,font=("Arial",18,"normal"))



#The End
