# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 00:39:05 2024

@author: priya
"""
import random
import time 
print('welcome to number guessing game')

up=input('Please enter the upper bound number: ')

if up.isdigit():
    
    up=int(up)
    if up <=0:
        print('Please enter a number greater than 0')
        quit()
else:
    print("Please enter a number")
    quit()

random_number= random.randint(0,up)
print(random_number)
guess=0
count=0
while guess!=random_number:
    guess=int(input('Please enter a number'))
    if guess<random_number:
        print("Please guess higher")
    elif guess>random_number:
        print("please guess lower")
    else:
        print("you have guess correctly")
    count=count+1

print("you have gussed in {} tries".format(count))

time.sleep(5)

