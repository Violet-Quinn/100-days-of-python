from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        #paddle code
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)


