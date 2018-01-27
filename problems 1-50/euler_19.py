# Project Euler
# Problem 19

# Number letter counts

import numpy as np


'''
Returns a value 0-6 where 0 is Sunday, 1 is Monday, ... (Gauss's algorithm)
https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
''' 
def getDay(day, month, year):
    A = year
    firstJan = (1 + 5 * ((A-1)%4) + 4 * ((A-1)%100) + 6 * ((A-1)%400)) % 7
   
    leapYear = True if year % 4 == 0 else False
    leapYear = False if (year % 100 == 0 and year % 400 != 0) else leapYear
    
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    # Calculate the day
    day = firstJan
    day += sum(months[:(month-1)]) + (day - 1)
    day %= 7
    return day

count = 0
for month in range(1,13):
    for year in range(1901,2001):
        day = getDay(1,month,year)
        count = count + 1 if day == 0 else count

print(count)
    
