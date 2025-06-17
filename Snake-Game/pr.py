from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# segment_1 = Turtle("square")
# segment_1.color("White")
#
# segment_2 = Turtle("square")
# segment_2.color("White")
# segment_2.goto(-20, 0)
# segment_3 = Turtle("square")
# segment_3.color("White")
# segment_3.goto(-40, 0)
#
# turtles = (segment_1, segment_2, segment_3)
#
# print(turtles)

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)





















screen.exitonclick()