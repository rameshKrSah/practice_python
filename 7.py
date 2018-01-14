# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:28:21 2017

@author: Dell
"""

#Write one line Python that takes this list (a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
#and make a new list that has only the even elements of this list

#List Comprehensions : https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_a = [element for element in a if(element % 2 ) == 0]

print("\n\nOriginal list \n")
print(a)
print("\n\nList with only the even elements\n")
print(even_a)


#find the age with respect to year 2017 for following date of birth
#years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]

age = [2017 - year for year in years_of_birth]

print("\n\nYears of birth: ")
print(years_of_birth)
print("\n\nAge")
print(age)
