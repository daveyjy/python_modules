#chapter3task6-6.py

# Scenario
# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, 
# and this is the clue. We don't want any repetitions. We want them to be removed.

# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers 
# appear not more than once.

# Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add 
# a part that can carry out a conversation with the user and obtain all the data from her/him.

# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #number list being searched in for loop

non_repeated_list = [1] #list that will store repeated elements and will be used as reference for the for loop.

for number in range(len(my_list)): #gives for loop access to my_list elements 0 to -1
    
    if [number] in non_repeated_list: #if the current loop number is found in repeated_list condition is true then...
        
        non_repeated_list.append(number)
        #non_repeated_list.remove(number) #removes current for-loop number from my_list if it is a repetition (true last statement)
    print(number)   
        
    #else: #if number is unique, and false for if-statement it gets inserted to repeated_list ready to be matched on the next for loop.
     #   repeated_list.append (number)

print("The list with unique elements only:", non_repeated_list) #prints numbers that have not been deleted by for-loop
        
#not working for some reason???   
#print(my_list)
