#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:01:45 2019

@author: hallvardr
"""

import os, logging, time

logging.basicConfig(filename='time_recover_terminal.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

print("Welcome to the UPC forensics app. This is the Recovery Filestool.\n")

filename=raw_input("\nWrite the name of the file (ex. image.dd):\n")

fileroute=raw_input("\nWrite the file route (ex. /root/docs):\n")

destroute=raw_input("\nWrite the destinetion route (ex./root/results):\n")

#RECOVER FILES.
startTime = time.time()

commandline=("photorec /debug /log /d "+destroute+"/Recovered_Files /cmd"+fileroute+"/"+filename+" partition_none,options,mode_ext2,fileopt,everything,enable,search")

os.system(commandline);

endTime = time.time()

duration = endTime - startTime

logging.info('Duration: ' + str(duration) + ' seconds')
