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

choice = input(
    'It is dusk.\nYou are walking down a path in the middle of a jungle.\nThe path ends at a cross road.\nWhere do you want to go? Type "left" or "right" : ')

if choice == "left":

    lake_choice = input(
        'The path ends up to a lake. Your destination lies on the island on the other end of the lake. What do you do?\nType "wait" to wait for a boat or "swim" to swim across the lake. : ')

    if lake_choice == "wait":
        print("A pirate ship arrives and steals your treasure map. Game Over.")

    elif lake_choice == "swim":

        door = input(
            'You follow the treasure map, and find yourself at the end of a tunnel.\nThere are 3 closed doors in front of you, which one do you choose? Type "red", "black" or "green" : ')

        if door == "red":
            print("You've entered a dragon's chamber. Game Over.")
        elif door == "black":
            print("Hurray!! You've found the treasure!")
        elif door == "green":
            print("You fall into a deep pit. Game Over.")
        else:
            print("Invalid Choice! Game Over.")

    else:
        print("Invalid Choice! Game Over.")

elif choice == "right":
    print("You encounter a group of deadly wild beasts. Game Over.")

else:
    print("Invalid Choice! Game Over.")