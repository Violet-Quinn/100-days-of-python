import turtle
import random
from turtle import Turtle, Screen


screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race: ")

# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def return_home():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards,"w")
# screen.onkey(move_backwards,"s")
# screen.onkey(move_right,"d")
# screen.onkey(move_left,"a")
# screen.onkey(return_home,"c")

colors=["violet","blue","green","yellow","orange","red"]
y_positions=[-70,-40,-10,20,50,80]
is_race_on=False
all_turtles=[]

for iterator in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colors[iterator])
    tim.penup()
    tim.goto(x=-230,y=y_positions[iterator])
    all_turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won. {winning_color} is the winner.")
            else:
                print(f"You've lost. {winning_color} is the winner.")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

# tim2=Turtle(shape="turtle")
# tim2.penup()
# tim2.goto(x=230,y=-100)
#
# tim3=Turtle(shape="turtle")
# tim3.penup()
# tim3.goto(x=230,y=-100)
#
# tim4=Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(x=230,y=-100)
#
# tim5=Turtle(shape="turtle")
# tim5.penup()
# tim5.goto(x=230,y=-100)
#
# tim6=Turtle(shape="turtle")
# tim6.penup()
# tim6.goto(x=230,y=-100)


screen.exitonclick()
