# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

print("Welcome to my Computer quiz")
start=input('Do you want to start the game?')

if start.lower()=="yes":
    print("Okay, let's start the game")
    ans1=input('What is the full form of CPU? ')
    count=0
    if ans1.lower()=="central processing unit":
        print('Correct!')
        count=count+1
    else:
        print("Incorrect!!")
  
    ans2=input('What is the full form of GPU? ')  
    if ans2.lower()=="graphics processing unit":
        print('Correct!')
        count=count+1
    else:
        print("Incorrect!!")
    
    ans3=input('What does PSU stand for? ')   
    if ans3.lower()=="power supply":
        print('Correct!')
        count=count+1
    else:
        print("Incorrect!!")
    print("Your score is: ",count)
    print("Your percentage is: ",(count/3)*100)
else:
    print("let's play again later")

print("This game will end now")

time.sleep(5)

