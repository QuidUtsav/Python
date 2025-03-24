import heroes
from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("turtle")
timmy.color("LightSteelBlue3")
col=['red','blue','green']
for i in range(5):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen=Screen()
screen.exitonclick()
