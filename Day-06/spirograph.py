from turtle import Turtle,Screen
import turtle
import random

def col():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    cols=(r,g,b)
    return cols
t=Turtle()
turtle.colormode(255)
t.speed(0)
for i in range(0,72):
    t.color(col())
    t.circle(70)
    t.setheading(t.heading()+5)


s=Screen()
s.exitonclick()