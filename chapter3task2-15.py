# chapter3task2-15.py

# Scenario
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, go back to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), 
# but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.

# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the 
# steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.

c0 = int(input("Enter your number that is a non-negative or non-zero number:"))

# if c0 <= 1:
#      print("The number you entered was a negative or zero, please try again:")

steps = 0 

while c0 > 1: #checks c0 input is greater than 1
    if c0 % 2 == 1: #check even number 
        print(c0 / 2)
        steps += 1
    # if c0 % 2 == 1: #first argument checks c0 is even, if true enter while loop

    else:
        print (c0 * 3+1)
        steps += 1
else:
    print("Steps =", steps)

