import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
screen = Screen()
# screen.setup(width=200, height=300, startx=10, starty=25)

tim.shape("turtle")
# tim.speed(2)
# tim.color("green")
# tim.pencolor("violet")


# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        tim.circle(70)
        tim.color(random_color())
        tim.setheading(tim.heading() + 10)
    # tim.color((random_color()))
    # tim.forward(30)
    # tim.setheading(random.choice(directions))


draw_spirograph(5)

# for _ in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# colours = ["dark green", "maroon", "dark magenta", "lime", "dark violet", "indigo", "firebrick", "saddle brown",
#            "olive", "dark goldenrod", "pale violet red", "firebrick"]


# def draw_shape(num_sides):
#
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)









screen.exitonclick()
