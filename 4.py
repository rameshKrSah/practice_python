# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:54:53 2017

@author: Dell
"""

#Create a program that asks the user for a number and then prints out a list of
#all the divisors of that number.

#input of a number from the user to find its divisors
num = int(input("Enter any number greater than zero: "))


#creating a list of numbers from 2 to num - 1
lis = list(range(2, num))


#creating a list to store the divisors
div_lis = []

#adding 1 to the divisor list as 1 is divisor of every number
div_lis.append(1)


#finding the divisors
for element in lis:
    if((num % element) == 0):
        div_lis.append(element)

#checking for num is 1 or not and adding itelf to divisor list
if num != 1:
    div_lis.append(num)

#printing the divisors
print("\n\nThe divisors are \n")
print(div_lis)