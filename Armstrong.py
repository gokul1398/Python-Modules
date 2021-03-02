# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:56:02 2021

@author: grass
"""

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10
    
if num == sum:
    print("{0} is Armstrong".format(num))
    
else:
    print("{0} is not Armstrong".format(num))