# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:44:20 2017

@author: Dell
"""

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

check_num = int(input("Enter the upper boundry number: "))

for element in list_a:
    if(element < check_num):
        new_list.append(element)
  #      print(str(element) +"\n")

if len(new_list) != 0:
    print("\n\nThe numbers that are less than " +str(check_num) +" are:")
    print(new_list)
else:
    print("\n\nThere are no numbers in the list less than " +str(check_num)
    +". Try again with higher value")