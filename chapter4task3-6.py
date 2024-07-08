#chapter4task3-6.py

# 4.3.6   LAB   Day of the year: writing and using your own functions
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns 
# the corresponding day of the year, or returns None if any of the arguments is invalid.

# Use the previously written and tested functions. Add your own test cases to the code.

#CONTINUED BELOW WITH CODE FROM CHAPTER4 LABS 3.4 AND 3.5

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

#CODE FROM PREVIOUS LABS ENDS HERE. NEW CODE FOR LAB 4.3.6 BEGINS BELOW

def day_of_year(year, month, day): 
    if 