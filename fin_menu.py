#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:53:48 2019

@author: hallvardr
"""
from os import system
#import deep_copy
#import sys
import hashlib
import logging, time, os.path

def md5Checksum(filename):
    with open(filename, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

system('clear') #Clear screen before to show menu, cls is MS Windows command
menulist= '''
    1. MD5 Checksum + Bit-to-bit copy,
    2. Add a name to the list,
    3. Remove a name from the list,
    4. Change an item in the list,
    5. MD5Checksum
    9. Quit''' #assuming you want to display menulist, having it as a tuple is useless

while True:
    
    print(menulist)
    target=raw_input("Please, pick an item from the menu:\t")
    
    if target=="1": 
        print("Which file would you like to copy?:\nThis action will calculate the MD5 Checksum of the original file\nand perform a bit-to-bit copy of it.")#this is an equality operator, whereas = is used to assign a variable (This checks the equality basically)
        
        #logging.basicConfig(filename='time_binarycopy_terminal.log',level=logging.DEBUG,format'%(asctime)s %(message)s')

        filename=raw_input("\nEnter name of file to copy: (/home/hallvardr/TFM/image.txt)\n")
    
        os.path.exists(filename)
        os.stat(filename)
        
        destroute=raw_input("\nWrite the destination route (/home/hallvardr/TFM):\n")
        
        startTime =time.time()
        
        #Create hash original device.
        completeName = os.path.join(destroute, "hashoriginal.txt")
        f = open(completeName,"w+")
        f.write(md5Checksum(filename))
        f.close()
        
        #Create binary copy.       
        commandline="sudo dd if="+filename+" of="+destroute+"/copia_image.txt"
        os.system(commandline)
        
        #Create hash binary copy.
        #commandline="sudo md5sum "+destroute+"/copia_image.txt >"+destroute+"/hashcopy.txt"
        #os.system(commandline)
        
        endTime =time.time()       
        duration =endTime -startTime
        
        logging.info('Timeline Duration: '+str(duration)+' seconds')
        
        cont=raw_input("Continue: Y/N\n")
        if cont == "y":
            system('clear')
            continue
        if cont == "n":
            break
        else: cont=raw_input("Continue: Y/N\n")

    elif target=="2":
        
        cont=raw_input("Continue: Y/N\n")
        if cont == "y":
            system('clear')
            continue
        if cont == "n":
            break
        else: cont=raw_input("Continue: Y/N\n")
    
    elif target=="3":
        Removename=raw_input("What name would you like to remove:")
        list=list.remove(Removename)
        print(menulist) #again, I took the parentheses away
    
    elif target=="4":
        Changename=raw_input("What name would you like to change:") #you'd missed the " at the beginning
        changetoname=raw_input("What is the new name:")
        list=list.replace(Changename, changetoname) #removed the '. They're the variables, not the strings 'Changename' etc that you want to replace.
        print(menulist)
        
    elif target=="5":
        Removename=raw_input("Which file would you like to Checksum?:")
        
        inputfile=raw_input("\nWrite the inputfile (/home/hallvardr/TFM):\n")
        outputfile=raw_input("\nWrite the outputfile (/home/hallvardr/TFM):\n")
        
        commandline="sudo md5sum "+inputfile+" >"+outputfile+""
        os.system(commandline)
        cont=raw_input("Continue: Y/N\n")
        if cont == "y":
            system('clear')
            continue
        if cont == "n":
            break
        else: cont=raw_input("Continue: Y/N\n")
        
    elif target=="9":
        print("good bye") #excessive indenting
    
    else: #this replaces the initial while
        #do nothing if the initial input is not 1,2,3,4,5 or 9
        print(menulist)