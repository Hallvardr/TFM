#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:53:48 2019

@author: hallvardr
"""
from os import system


system('clear') #Clear screen before to show menu, cls is MS Windows command
menulist= '''1. Print the list,
    2. Add a name to the list,
    3. Remove a name from the list,
    4. Change an item in the list,
    9. Quit''' #assuming you want to display menulist, having it as a tuple is useless

lst=("johny","tom","kim","tim","jim") #don't use reserved names for variables, may mess up things


while True:
    
    print(menulist)
    target=raw_input("Pick an item from the menu:")
    
    if target=="1": #this is an equality operator, whereas = is used to assign a variable (This checks the equality basically)
        print(lst)
        continue
    
    elif target=="2":
        Addname=raw_input("Type in a name to add:")
        list=list.append(Addname) #use append instead of insert, insert is for a specific position in list
        print(menulist) #no parentheses, menulist is not a function; also this doesn't have to be indented
    
    elif target=="3":
        Removename=raw_input("What name would you like to remove:")
        list=list.remove(Removename)
        print(menulist) #again, I took the parentheses away
    
    elif target=="4":
        Changename=raw_input("What name would you like to change:") #you'd missed the " at the beginning
        changetoname=raw_input("What is the new name:")
        list=list.replace(Changename, changetoname) #removed the '. They're the variables, not the strings 'Changename' etc that you want to replace.
        print(menulist)
    
    elif target=="9":
        print("good bye") #excessive indenting
    
    else: #this replaces the initial while
        #do nothing if the initial input is not 1,2,3,4 or 9
        print(menulist)