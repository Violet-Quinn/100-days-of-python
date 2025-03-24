from idlelib.colorizer import color_config
import random
from turtle import Turtle,Screen
tim_turtle=Turtle()
# tim_turtle.shape("turtle")
# tim_turtle.color("red")
# tim_turtle.forward(100)
# tim_turtle.right(90)
# tim_turtle.forward(100)
# tim_turtle.right(90)
# tim_turtle.forward(100)
# tim_turtle.right(90)

# for iterator in range(4):
#     tim_turtle.forward(100)
#     tim_turtle.right(90)

# for iterator in range(30):
#     tim_turtle.forward(10)
#     tim_turtle.up()
#     tim_turtle.forward(10)
#     tim_turtle.down()


#drawing with number of sides
# colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'brown', 'black']
#
#
# def draw_shape(num_side):
#         angle=360/num_side
#         for _ in range(num_side):
#             tim_turtle.forward(100)
#             tim_turtle.right(angle)
#
# for shape_side in range(3,11):
#     tim_turtle.color(random.choice(colors))
#     draw_shape(shape_side)

#for random walk
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan', 'brown', 'black']
def random_walk(iterations):
    tim_turtle.pensize(15)
    for _ in range(iterations):
        tim_turtle.forward(random.choice(range(30,100)))
        path_choice=random.choice([0,1])
        if path_choice==0:
            tim_turtle.left(90)
        else:
            tim_turtle.right(90)
        tim_turtle.color(random.choice(colors))

random_walk(50)







screen=Screen()
screen.exitonclick()
