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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


first_decition = input(
    'You are at the cross. You want to turn "left" or "right?" ').lower()
if first_decition == "right":
    print("You fell into hole. Game over")
else:
    second_decition = input(
        'You come to a Lake and there is island in the middle of the lake. You would want to "wait" for boat or "swim" '
    )
    if second_decition != "wait":
        print("You have been eaten by crocodiles. Game over. ")
    else:
        input(
            "You arrived at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which colour you choosing? "
        )
        if input == "red":
            print("You have been eaten by wolwes. Game over.")
        if input == "yellow":
            print("You have been eaten by Gorillas. Game over.")
        else:
            print("You escaped from island. You won.")
