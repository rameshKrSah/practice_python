# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:35:29 2017

@author: Dell
"""

num = int(input("Enter a number: "))
check = int(input("Enter the divisor: "))

flag_oe = num % 2
flag_4 = num % 4
flag_user = num % check

print("\n\nResult::")
if(flag_oe == 0):
    print(str(num) +" is an even.")
else:
    print(str(num) +" is an odd.")

if(flag_4 == 0):
    print("Is exactly divisible by 4.")

if(flag_user == 0):
    print("And " +str(check) +" exactly divides it.")