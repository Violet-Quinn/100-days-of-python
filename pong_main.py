from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from pong_scoreboard import Scoreboard
import time

#window setup
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right=Paddle((350,0))
paddle_left=Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(paddle_right)<50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect paddle miss
    #right
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.point_left()
    #left
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.point_right()

screen.exitonclick()