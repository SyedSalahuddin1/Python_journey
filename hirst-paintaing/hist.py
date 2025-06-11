import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()

color_list = [(217, 155, 83), (230, 213, 98), (58, 98, 136),(125, 174, 201), (158, 84, 43), (162, 53, 77),
               (190, 157, 27), (208, 135, 150), (166, 20, 43), (217, 61, 90),(59, 25, 44), (43, 180, 140),
               (119, 192, 161), (25, 33, 68), (223, 78, 56), (46, 131, 92), (235, 163, 183),(43, 51, 110),
               (143, 220, 192), (221, 218, 11), (107, 111, 172), (47, 163, 176), (142, 210, 227), (75, 27, 15),
            (145, 27, 19), (171, 185, 226)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.hideturtle()


screen = turtle_module.Screen()
screen.exitonclick()



