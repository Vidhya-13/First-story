# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

n = input("Please enter a number greater than zero: ")
def f1(an_int):
    p = int(math.log(an_int, 3))
    return int(pow(3, p))
    
an_int = int(n)
print (f1(an_int))


