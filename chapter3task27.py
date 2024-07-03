# Scenario
# Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, 
# which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days 
# to travel its entire length!

# The word Mississippi is also used for a slightly different purpose: to count mississippily.

# If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.

# The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore 
# "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek
# to make sure the seeker does an honest count.

# Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print 
# to the screen the final message "Ready or not, here I come!"

# Use the skeleton we've provided in the editor.

#   EXTRA INFO  
# Note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. 
# We're going to talk about them soon.

# For the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent
# print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon 
# learn more about modules and methods.

import time

# Write a for loop that counts to five.
for count in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(count, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
    
print("Ready or not, here i come!!!")
    
