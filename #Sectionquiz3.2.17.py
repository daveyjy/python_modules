#Sectionquiz3.2.17.py
#Section quiz 3.2.17

#Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

# for i in range(1, 11):
#     if i % 2 == 1:
#         print(i)
#         continue

#Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

# x = 1
# while x < 11:
#     for x in range (1,11,2):
#         print(x,"\n")
#     break

#Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     else:
#         print ("", ch, end="")

# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace 
# each 0 with x, and print the modified string to the screen. Use the skeleton below:

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

#Question 5: What is the output of the following code?

# n = 3
 
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# Question 6: What is the output of the following code?

# n = range(4)
 
# for num in n:
#     print(num - 1)
# else:
#     print(num)

# Question 7: What is the output of the following code?

for i in range(0, 6, 3):
    print(i)
 
#  0, 3 