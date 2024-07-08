# chapter4task3-4.py
# 4.3.4   LAB   A leap year: writing your own functions
# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

# The seed of the function is already shown in the skeleton code in the editor.

# Note: we've also prepared a short testing code, which you can use to test your function.

# The code uses two lists ‒ one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.

def is_year_leap(year): #function names is_leap_year with parameter named year
    
    #if year is less than 1582, it is not in the gregorian calendar
    if year < 1582:
	    print("Not within the Gregorian calendar period")
     
        else:
        # otherwise working out if year is not divisible by 4, and therefore a COMMON YEAR
        if year % 4 != 0:         
            print("Common year") 

        #otherwise working out if year is not divisible by 100, it is a leap year
        elif year % 100 != 0:
            print("leap year")

        #otherwise working out if the year is not divisible by 400, it is a common year  
        elif year % 400 != 0:
            print("Common year")
        #if non of the above arguments have been satisfied, it's a leap year
        else:
            print ("leap year")



test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")