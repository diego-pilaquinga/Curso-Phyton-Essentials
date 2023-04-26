# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:01:21 2023

@author: diego
"""

def isYearLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def daysInMonth(year, month):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")