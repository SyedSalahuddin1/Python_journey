print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!.")
print("Your mission is to find the Treasure")
print("You are at a Cross Road,Where do you want to go")
direction = input(     "Type left or right\n")
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    next_step= input(     "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if next_step == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        next_door = input(     "One red, one yellow and one blue. Which colour do you choose?\n")
        if next_door == "yellow":
            print("You Found The TREASURE! You Win.")
        elif next_door =="blue":
            print("Eaten by Beats.Game Over!")
        elif next_door == "red":
            print("Burned by fire.Game Over!")
        else:
            print("Gameee Overrr!")
    elif next_step == "swim":
        print("You got attacked by an angry trout. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
elif direction == "right":
    print("You fell into a hole. Game Over!")
else:
    print("You fell into a hole. Game Over!")










