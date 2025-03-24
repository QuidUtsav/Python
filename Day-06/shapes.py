from turtle import  Turtle,Screen
from random import randint
t=Turtle()
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
col=["red","purple","blue","pink","yellow","green"]
for i in range(3,10):
    t.pencolor(col[randint(0,5)])
    for j in range(0,i):
        t.forward(100)
        t.right(360/i)
    t.right(0)




screen=Screen()
screen.exitonclick()