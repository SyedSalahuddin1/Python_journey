# print("Hello I'm Syed Salahuddin.")
# print("o----")
# print(" ||||")
# print("*" * 10)
import math

# price = 10
# rating = 4.9  # Float
# name = "Salah"
# is_published = True
# print(price)

# name = "John Smith"
# age = 20
# is_new = True

# name = input("What is Your Name? ")
# color = input("What's your favourite color? ")
# print('Hi ' + name)
# print(name + " Likes " + color)

# birth_year = int(input("Birth year: "))
# print(type(birth_year))
# age = 2025 - birth_year
# print(age)
# print(type(age))

# weight = float(input("What is your weight in pounds? "))
# weight_in_kg = weight / 2.2
# print(f"Weight in Kg: {weight_in_kg:.2f} kg.")

# course = '''
# Hi Salah,
#
# Here is your First Email to you.
#
# Thank you,
# The support team.
#
# '''
# print(course)
#
# name = "Salahuddin"
# print(name[1:-1])

# first = 'Syed'
# last = 'Salahuddin'
# msg = f"{first} [{last}] is a python Developer."
# print(msg)

# course = "Python for Beginners."
# print(len(course))
# print(course)
# # title upper lower
# print(course.find('N'))
# print(course.replace("Beginners", "Absolute Beginners"))
# print("Python" in course)
#

# print(10 // 3)
#
# x = 10 + 3 * 2 ** 2
# print(x)
# Y = (2 + 3) * 10 - 3
# print(Y)
# # BODMAS PEMDAS

# x = 2.9
# print(round(x))
# y = -6.9
# print(abs(round(y)))
# print(math.ceil(x))
# print(math.floor(x))

# weather = input("How's the weather today, Is it hot or cold.\n").lower()
#
# if weather == "hot":
#     print("It's a hot day today.")
#     print("Drink plenty of water.")
# elif weather == "cold":
#     print("It's a Cold Day.")
#     print("Wear a Jerkin to keep yourself warm.")
# else:
#     print("It's a Lovely day.")
# print("Enjoy your Day.")

# credit = input("Tell me what's your credit? \n").lower()
# if credit == "good":
#     print("They Need to put down 10%.")
# else:
#     print("They need to put down 20%.")
# print("The down payment is for $1M.")

# price = 100000
# has_good_credits = False
#
# if has_good_credits:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down Payment: ${down_payment}.")

# has_good_income = True
# has_good_credit = False
#
# if has_good_credit and has_good_income:
#     print("Eligible for loan.")
# else:
#     print("Not Eligible for loan.")
# print("Finish the work as early as possible.")

# AND NOT OR

# COMPARISON OPERATOR

# == >= <= !=
#
# name = input("Write down the name to check? : ")
#
# if len(name) < 3:
#     print("Name must be at least more than 3 characters.")
# elif len(name) > 50:
#     print("Name  must be at less than 50 characters.")
# else:
#     print("Names looks good.")

# WEIGHT CONVERTER PROGRAM
# weight = int(input("Enter your weight: "))
# weight_in_ms = input("(L)lbs or (k)g: \n").lower()
# if weight_in_ms == "k":
#     final_weight = weight * 2.2
#     round(final_weight, 2)
#     print(f"You are {final_weight} pounds.")
# elif weight_in_ms == "l":
#     final_weight = weight // 2.2
#     (round(final_weight), 2)
#     print(f"You are {final_weight} kilos.")

# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("Done")

# GUESSING GAME
# lives = 3
# secret_number = 5
# game_over = False
# while not game_over:
#     guess = int(input("Guess the Number: "))
#
#     if guess != secret_number:
#         lives -= 1
#         print("That's not the correct number.")
#         if lives == 0:
#             game_over = True
#             print(f"The Number was {secret_number}.")
#     else:
#         print(f"That's right. The number is {secret_number}")
#         exit()

# CAR GAME
# game_over = False
# started = False
#
#
# def help_player():
#     print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#     """)
#
#
# def start():
#     print("Car started Ready to go.")
#
#
# def stop():
#     print("Car stopped.")
#
#
# while not game_over:
#     user_input = input("What are your commands: ").lower()
#     if user_input == "help":
#         help_player()
#     elif user_input == "start":
#         if started:
#             print("Car has already been started!")
#         else:
#             started = True
#             start()
#     elif user_input == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             stop()
#
#     elif user_input == "quit":
#         print("Game Over")
#         game_over = True
#     else:
#         print("Sorry,I don't understand that....")

# for loops

# for item in 'Python':
#     print(item)
#     print("\n")
#
# for item in ['Syed', 'Azeem', 'Zubair', 'Zaid']:
#     print(item)

# for item in range(10, 101, 10):
#     print(f"10 * {item//10} = {item}")

# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
# print(total)

# NESTED LOOPS
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# for i in range(1, 6):
#     if i == 1 or i == 3:
#         print("*****")
#     else:
#         print("**")

# numbers = [5, 2, 5, 2, 2]

# print('*' * num)
#     # print(num)
# for num in numbers:
#     output = ''
#     for count in range(num):
#         output += 'L'
#     print(output)

# names = ['John', 'Syed', 'Zaid', 'Mosh', 'Azeem', 'Zubair']
# names[2] = 'Ahmed'
# print(names[-5][2])
# print(names[2:5])

# numbers = [3, 4, 5, 9, 12, 34, 45]
# max_n = 0
# for num in numbers:
#     if num > max_n:
#         max_n = num
# print(max_n)

# 2D LISTS
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # print(matrix[0][0])
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 2, 8, 9, 2, 9, 5]
# numbers.insert(5, 10)
# # print(64 in numbers)
# # print(numbers.sort())
# # print(numbers)
# # print(numbers.reverse())
# # print(numbers)
# uniques = []
# print("\n")
# print("\n")
# print("\n")
#
# for num in numbers:
#     if num in numbers:
#         if num not in uniques:
#             uniques.append(num)
# print(uniques)

# numbers = (1, 2, 3, 4)
# print(numbers[1])
#
# coordinates = (1, 2, 3)
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
#
# x, y, z = coordinates
# print(x, y, z)

# diction = {
#     'Name': 'Syed Salahuddin',
#     'Email': 'syedsalah23@gmail.com',
#     'age': 23,
#     'is_verified': True
# }
#
# print(diction['Name'])
# print(diction.get('birthdate', 'May 11 2002'))
# print(diction)

# phone = input("Phone: ")
# numbers = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six'
# }
# output_string = ''
# for num in phone:
#     output_string += numbers.get(num, "!") + " "
# print(output_string)

# # emoji converter
# message = input('> ')
# words = message.split(' ')
# emojis = {
#     ':)': '😀',
#     ':(': '😭'
# }
# out = ''
# for word in words:
#     out += emojis.get(word, word) + ' '
# print(out)

# # FUNCTIONS positional arguments, keyword arguments
#
#
# def greet_user(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user(last_name="Syed",first_name="Salah")
# greet_user(last_name="Azeem", first_name="Sajid")
# print("Finish")


# def square(number):
#     return number * number
# #     by default all functions in python return none if there is none explicitly typed
#
#
# result = square(3)
# print(result)


# def emoji_conv(message):
#     words = message.split(' ')
#     emojis = {
#         ':)': '😀',
#         ':(': '😭'
#     }
#     out = ''
#     for word in words:
#         out += emojis.get(word, word) + ' '
#     return out
#
#
# message = input('> ')
#
# print(emoji_conv(message))


# Handling error
# try:
#     age = int(input("Age: "))
#     print(age)
# # add as many as excepts
# except ValueError:
#     print("Invalid type.")


# CLASSES
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10, 20)
# point1.draw()

# # Constructor
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"I'm {self.name}")
#
#
# person1 = Person("Salah")
# print(person1.name)
# person1.talk()


# Inheritance
# class Mammal:
#     def walk(self):
#         print("Walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def be_cunning(self):
#         print("Too Good Looking")
#
#
# dog1 = Dog()
# dog1.walk()
#
# cat1 = Cat()
# cat1.be_cunning()

# IMPORTING MODULES USING DIFFERENT FILES
# from mod_prac import find_max
# numbers = [1, 4, 6, 8, 32, 67]
# nom = find_max(numbers)
# print(nom)

# # packages
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# # random modules
import random
# # for i in range(3):
# #     print(random.randint(10, 20))
# #     print(round(random.random(), 2))
# # #     random.choice(list)
#
#
# class Dice:
#     def roll(self):
#         # random.randint(1, 6)
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())


# DIRECTORIES
# mkdir, rmdir, .exists(), glob('*')
from pathlib import Path
path = Path()

for file in path.glob('*'):
    print(file)
