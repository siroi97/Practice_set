# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:38:06 2024

@author: priya
"""

import time
import random

print ('Welcome to rock_paper_scissors game \n')

list=['rock','paper','scissors']
player_score=0
computer_score=0



ask=input("do you want to continue type 'y' for yes and 'n' for no: ")
if ask.lower()=='y':
        print("lets's start the game \n")
        while True:
            ask1=input("type rock/paper/scissors or 'q' to quit: ")
            if ask1.lower() =='q':
                print('Goodbye')
                break
            
            elif ask1.lower() !='q':
                x=random.randint(0, 2)
                computer_guess=list[x]
                print("computer_guess is",computer_guess+'.')
                if ask1.lower()=='rock' and computer_guess=='scissors':
                    print('You won')
                    player_score += 1
                elif ask1.lower()=='paper' and computer_guess=='rock':
                   print('You won')
                   player_score += 1
                elif ask1.lower()=='scissors' and computer_guess=='paper':
                   print('You won')
                   player_score += 1
                elif ask1.lower()==computer_guess:
                    print('You both guesses the same')
                    continue
                else:
                   print('You lost')
                   computer_score +=1
            else: 
                  print('Please enter valid input')
                  continue
            
        
elif ask.lower()=='n':
    print("Let's play later")
    
else:
      print("Please enter valid input to start the game")
print('Your score is: ', player_score)
print('Computer score is: ',computer_score)
      
time.sleep(5)