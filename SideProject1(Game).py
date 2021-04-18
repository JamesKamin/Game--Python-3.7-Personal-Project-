#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 02:44:43 2021

@author: jkenglish
"""

print("Welcome to the game!")


user = int(input("Enter a number: "))




if( 1 <=user<= 3):

   print( "Gandalf")


elif user == 4:

    print( "Saruman")
    
elif user == 5:
    
    print('Aragorn')
    
elif user>6:
    
    print("Too high!")
    
elif user<1:
    
    print("Too low!")



