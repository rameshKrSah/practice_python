# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:46:40 2017

@author: Dell
"""

import random as rn
correct_guess = 0
total_guess = 0
print("Guess the number between 0 and 10, to stop playing type exit")

while(1):
    a = rn.randint(0, 5)
    b = input("Your guess: ")
    if(b == "exit"):
        break;
    else:
        total_guess = total_guess + 1
        b = int(b)
        if(a == b):
            correct_guess = correct_guess + 1
            print(":) You guessed it RIGHT !!")
        else:
            print(":( Wrong guess")


print("\n\nThank You for playing, here are your stats::\n")
print("Total guesses "+str(total_guess) +", correct guesses "+str(correct_guess))
