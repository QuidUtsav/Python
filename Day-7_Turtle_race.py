from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
color=["red","purple","yellow","blue","orange","black","green","brown"]
all_turtle=[]
def game():
    for i in range(0,8):
        tim=Turtle(shape="turtle")
        tim.penup()
        tim.goto(x=-240,y=-175+i*50)
        tim.color(color[i])
        all_turtle.append(tim)
    user_bet= screen.textinput(title="Make a bet",prompt="Enter a color of winning turtle")
    if user_bet:
        race_on=True
    while race_on:
        for turtle in all_turtle:
            if turtle.xcor()>220:
                race_on=False
                winner=turtle.pencolor()
                if user_bet==winner:
                    print(f'The winning turtle is {winner}.You Win!!!!')
                else:
                    print(f'The winning turtle is {winner}.You Lose!!!!')
            turtle.forward(random.randint(5,20))

p=True
while p:
    game()
    y=screen.textinput(title="Play again?",prompt="enter y to play again.")
    if y!="y":
        p=False
    screen.clear()
screen.exitonclick()
