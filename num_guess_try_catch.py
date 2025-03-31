#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if the user enters the correct chosen number
import random

# Step 1: GET user_num_str
user_num_str = input("Enter a number between 0 and 9: ")

# Step 2: GENERATE chosen_number (0-9)
chosen_number = random.randint(0, 9)

# Step 3: TRY user_num_str
try:
    # Step 4: Check if user_num_str is equal to chosen_number
    user_num = int(user_num_str)  # Convert input to integer
    if user_num == chosen_number:
        print("You got the right number!")
    else:
        print(f"You did not get the right number. The right number is {chosen_number}")
except ValueError:
    # Step 5: EXCEPT Invalid input
    print(f"Error. You entered {user_num_str}. Please enter an integer.")
