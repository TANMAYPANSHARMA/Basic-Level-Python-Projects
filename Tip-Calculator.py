"""
      If the bill was $150.00, split between 5 people, with 12% tip.
      Each person should pay (150.00 / 5) * 1.12 = 33.6
      Format the result to 2 decimal places = 33.60
"""
print("Welcome to the tip calculator.")

# Input bill amount.
bill = float(input("What's your total bill? $"))

# Input tip percentage.
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Calculate total tip amount.
tip_amount = (tip / 100) * bill

# Calculate final bill amount = bill amount + tip amount, and round it to 2 decimal places.
final_bill_amount = round(bill + tip_amount, 2)

# Input no. of people to split the total bill amount.
no_of_people = int(input("How many people to slip the bill? "))

# Calculate amount splitted for each person = final bill amount / no. of people, and round it to 2 decimal places.
split_bill = "{:.2f}".format(final_bill_amount / no_of_people)
# split_bill has been turnt from float to string with 2 decimal places format.

print(f"Each person should pay: ${split_bill}")