import turtle
from turtle import  Turtle,Screen
import random
direct=[0,90,270,180]
turtle.colormode(255)
def col():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    r_c=(r, g, b)
    return  r_c

t=Turtle()
t.pensize(20)
t.speed(0)
for i in range(20):
    t.color(col())
    t.forward(50)
    t.setheading(random.choice(direct))



s=Screen()
s.exitonclick()