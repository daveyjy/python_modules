# chapter4task3-5.py
# 4.3.5   LAB   How many days: writing and using your own functions
# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given 
# year-month pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use 
# a list filled with the months' lengths. You can create it inside the function ‒ this trick will significantly shorten the code.

# We've prepared a testing code. Expand it to include more test cases.


#continued from chapter4task3-4 lab

def is_year_leap(year):
    
    if year % 4 != 0:        #working out if year is not divisible by 4, and therefore a COMMON YEAR      
        #print("Common year") 
        return False
        
    elif year % 100 != 0:    #otherwise working out if year is not divisible by 100, it is a leap year
        #print("leap year")
        return True
        
    elif year % 400 != 0:    #otherwise working out if the year is not divisible by 400, it is a common year  
        #print("Common year")
        return False
    else:                    #if non of the above arguments have been satisfied, it's a leap year
        #print ("leap year")
        return True
        
        
def days_in_month(year, month):
    
    #if is_year_leap == True:
        
    daysRef = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]      #reference list inside of function that states days in each month
    
    # daysRef = [["Jan", 31], ["Feb", 28], ["Mar", 31], ["Apr", 30], ["May", 31], ["Jun", 30], ["Jul", 31], ["Aug", 31], ["Sep", 30], ["Oct", 31], ["Nov", 30], ["Dec", 31]]
    #2D list comprehension i want to use above
    
    if month == 2 and is_year_leap == True:       #first condition of module checks that month is february and year is a leap year
        print("There are", (month in daysRef - 1), "days in this month and year.")     #if both conditions are TRUE, print that the leap year has the daysRef 01 index + 1 (29 days)
        
    else:
        days = i-1 in range(len(daysRef))                         #if the first condition in false and the parameters do not present a leap year and feb, then take month -1 to find days within daysRef index
        print("There are", days, "in this month and year.")
        
#test date for functions above
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")