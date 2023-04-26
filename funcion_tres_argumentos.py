# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:35:58 2023

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

def dayOfYear(year, month, day):
    days = 0
    
    # año valido
    if year < 1:
        return None
    
    # mes valido
    daysInThisMonth = daysInMonth(year, month)
    if daysInThisMonth is None:
        return None
    
    # dia valido
    if day < 1 or day > daysInThisMonth:
        return None
    
    # calculo de los dias del año
    for m in range(1, month):
        days += daysInMonth(year, m)
    days += day
    
    return days

# entrada valida
print(dayOfYear(2000, 12, 31)) 
print(dayOfYear(2010, 10, 15)) 
print(dayOfYear(2023, 4, 20)) 

# año no valido
print(dayOfYear(-1, 1, 1)) 

# mes no valido
print(dayOfYear(2000, 13, 1)) 

# dia no valido
print(dayOfYear(2000, 2, 30)) 
