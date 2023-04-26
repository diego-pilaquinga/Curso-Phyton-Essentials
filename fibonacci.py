# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:56:05 2023

@author: diego
"""
def fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        """c=a+b
        a=b
        b=c"""
        a, b = b, a+b
    print()
fibonacci(50)