#chapter3task4-6.py
# 3.4.6 LAB The basics of lists
# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

# Your task is to:

# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user to replace the middle number with an integer number entered by the user.

hat_list[2]=int(input("Pick your first number:"))

print("\n New list content is:", (hat_list)) #shows user input number added to middle index

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]


# Step 3: write a line of code that prints the length of the existing list.

print("\n New list length is:", len(hat_list))