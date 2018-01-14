# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:38:33 2017

@author: Dell
"""

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
#(using inputs), compare them, print out amessage of congratulations to the winner
#, and ask if the player want to start a new game)

"""
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    
"""
print("*******************************************************")
print("-------Welcome to Rock - Paper - Scissor Game----------")
print("*******************************************************")
print("The plays are : \n1.rock \n2.paper \n3.scissor.")
print("\n\nEnter your plays:\n")

winner = 0

while True:
    p1_play = input("Player 1 play: ")
    p2_play = input("Player 2 play: ")
    print("\n")
    
    pp = str(p1_play[0] + p2_play[0])
    pq = str(p2_play[0] + p1_play[0])
    
    if(pp == "rs"):
        winner = 1
    elif(pp == "sp"):
        winner = 1
    elif(pp == "pr"):
        winner = 1
    elif(pq == "rs"):
        winner = 2
    elif(pq == "sp"):
        winner = 2
    elif(pq == "pr"):
        winner = 2
    else:
        winner  = 0 
    if(winner != 0):
        print("Player " +str(winner) +" won !!")
    else:
        print("No winner :(")
    
    play_flag = input("\nPlay again ? Y or N: ")
    if(play_flag == 'Y'):
        continue
    elif(play_flag == 'N'):
        print("\n*******************************************************")
        print("--------------Bye, Thank you for playing :)------------")
        print("*******************************************************")
        break
    
    