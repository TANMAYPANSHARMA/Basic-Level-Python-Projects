# Password Generator Project

import random

# Making 3 lists of all letters, numbers and symbols which are usually used in passwords.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

# Input the number of letters, symbols and numbers user wants in their password.
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""   
    From line number 28 - 38, we do the following:

      Step 1: Declaring an empty list for letters, symbols, numbers individually.
      Step 2: Declaring a 'for' loop, which will run from {0 to [(nr_letters/nr_symbols/nr_numbers) - 1]}.
      Step 3: The 'for' loops will insert any random letter/symbol/number at index 'i' in the empty list. 

      Hence, we obtion lists for totally random letters, symbols and numbers, which have lengths equal to user's input.
"""

random_letters = []
for i in range(0, nr_letters):
  random_letters.insert(i , random.choice(letters))

random_symbols = []
for i in range(0, nr_symbols):
  random_symbols.insert(i, random.choice(symbols))

random_numbers = []
for i in range(0, nr_numbers):
  random_numbers.insert(i, random.choice(numbers))

"""
      We now create an empty list: random_sequence
      And by using .extend() method, we add the lists of random letters, symbols and integers to its end.
      By doing this, we obtain a single list containing all random letters, symbols and integers.  
"""

random_sequence = []
random_sequence.extend(random_letters)
random_sequence.extend(random_symbols)
random_sequence.extend(random_numbers)

"""
      In order to obtain a fully random sequence, 
      We use the .shuffle() method to shuffle our above formed list of random letters, symbols and integers.
"""

random.shuffle(random_sequence)

"""
      To convert list to string,
      We declare an empty string: random_password
      And join our list to it by using the .join() method.
"""

random_password = "".join(random_sequence)

# Output :
print("Here is your password: " + random_password)