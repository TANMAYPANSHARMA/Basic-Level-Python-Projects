# ASCII art for rock, paper and scissors:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Making a list of rock, paper and scissors.
rps = [rock, paper, scissors]

import random

# Input user's choice.
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors : "))

# Print the ASCII art corresponding to user's choice.
if user_choice >= 0 and user_choice <= 2 :
  print(rps[user_choice])
else :
  print("Oh no, wrong number!")

# Generate a random number for computer's choice, and print its corresponding ASCII art.
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(rps[computer_choice])

"""
      The rules for determining who wins are as follows:

      • Rock wins against Scissors.
      • Scissors win against Paper.
      • Paper wins against Rock.

      Following are 2 methods to determine who wins. Use whichever you like:
"""

# " ------ METHOD 1 ------ "
# if user_choice == computer_choice :
#   print("It's a draw.")
# elif user_choice == 0 :
#   if computer_choice == 1 :
#     print("You lose!")
#   elif computer_choice == 2 :
#     print("You win!!")
# elif user_choice == 1 :
#   if computer_choice == 0 :
#     print("You win!!")
#   elif computer_choice == 2 :
#     print("You lose!")
# elif user_choice == 2 :
#   if computer_choice == 0 :
#     print("You lose!")
#   elif computer_choice == 1 :
#     print("You win!!")
# else :
#   print("Wrong number. You lose!")

" ------ METHOD 2 ------ "
if user_choice == computer_choice :
  print("It's a draw.")
elif user_choice == 0 and computer_choice == 2 :
    print("You win!!")
elif computer_choice == 0 and user_choice == 2 :
    print("You lose!")
elif computer_choice > user_choice :
    print("You lose!")
elif user_choice > computer_choice :
    print("You win!!")
else :
  print("Wrong number. You lose!")
