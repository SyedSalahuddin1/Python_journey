from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.back(25)


def turn_right():
    new_heading = tim.heading() + 90
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() - 90
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="b", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
