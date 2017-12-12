# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:13:27 2017

@author: Dell
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
copies = int(input("Enter the number of copies you want: "))

age = int(age)

if age >= 100:
    print(copies * (name + ", you're too old.\n"))
elif age < 100:   
    age_100 = 2017 + 100 - age
    age_100 = str(age_100)
    print(copies * (name + ", you will turn 100 in " +age_100 +".\n"))
    