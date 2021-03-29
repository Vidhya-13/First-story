# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:45:43 2021

@author: nvidh
"""
P = 10000
r = 0.08
n = 12
time = float(input("Please enter the number of years:"))
a1 = float(0.08/n)
a2 = float(12*time)
a3 = int(10000*(1+a1)**a2)
print ("The final amount after", time, " years is: ",a3)