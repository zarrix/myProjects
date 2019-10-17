#  Colourful Creation

# Colourful Creations


from turtle import *
speed(3)
penup()
s = Screen()
s.setup(400,400)
s.bgcolor("black")
right(90)
goto(0,60)
color('pink')
write("HELLO",align="center",font=('Arial',30,'bold'))


goto(0,-40)
color('orange')
write('WORLD!',align='center',font=('Arial',30,'bold'))
hideturtle()
goto(0,0)
color('#AFD6D8')
circle(30)
dot(350)

color('green')
goto(0,100)

write('If',align='center',font=('Arial',18,'bold'))
forward(50)
color('pink')
write('you want !',align='center',font=('Arial',24,'bold'))
forward(60)
color('orange')
write('to succed',align='center',font=('Arial',45,'bold'))
forward(60)
color('yellow')
write('D\'ONT',align='center',font=('Arial',40,'bold'))
forward(40)
color('black')
write('GIVE UP!',align='center',font=('Arial',20,'bold'))



# The End
