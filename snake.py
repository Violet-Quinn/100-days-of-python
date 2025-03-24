from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move_snake(self):
        for turtle_number in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_number - 1].xcor()
            new_y = self.turtles[turtle_number - 1].ycor()
            self.turtles[turtle_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.turtles.append(tim)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]