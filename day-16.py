# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral", "green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Friends name", ["Faisal", "Nabeel", "Ali", "Azeem", "Mujtaba"])
table.add_column("School Friends fields", ["Business", "Medical", "Self-employed", "Graduated", "Graduated"])
table.align = "r"
print(table)
