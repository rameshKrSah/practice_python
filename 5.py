# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:42:17 2017

@author: Dell
"""
#importing the random library
import random

#Write a program that returns a list that contains only the elements that are 
#common between the lists(without duplicates). Make sure your programs work on 
#list of different sizes

#lis_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#lis_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#randomly generated lists: range upto 20 with 10 elements each
lis_a = random.sample(range(20), 10)
lis_b = random.sample(range(20), 5)

#Getting the lengths of the lists
len_a = len(lis_a)
len_b = len(lis_b)

#list to store the common elements
com_lis = []

print("Length of first list " +str(len_a))
print(lis_a);
     
print("\nLength of second list " +str(len_b))
print(lis_b)

#going through each element in lis_a
for ele_a in lis_a:
    #if it is in lis_b
    if ele_a in lis_b:
        #if it is not already in com_lis
        if ele_a not in com_lis:
            #store the common element in the common list
            com_lis.append(ele_a)
                
#print the common list elements
print("\nThe list with common elements is:")            
print(com_lis)