#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:29:24 2019

@author: hallvardr
"""

import logging, time, os.path
import hashlib

#logging.basicConfig(filename='time_binarycopy_terminal.log',level=logging.DEBUG,format'%(asctime)s %(message)s')

filename=raw_input("\nEnter name of file to copy: (/home/hallvardr/TFM/image.txt)\n")

os.path.exists(filename)
os.stat(filename)

destroute=raw_input("\nWrite the destination route (/home/hallvardr/TFM):\n")

startTime =time.time()

#Create hash original device.

def md5Checksum(filename):
    with open(filename, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

completeName = os.path.join(destroute, "hashoriginal.txt")
f = open(completeName,"w+")
f.write(md5Checksum(filename))
f.close()


#Create binary copy.

commandline="sudo dd if="+filename+" of="+destroute+"/copia_image.txt"
os.system(commandline)

#Create hash binary copy.
commandline="sudo md5sum "+destroute+"/copia_image.txt >"+destroute+"/hashcopy.txt"
os.system(commandline)

endTime =time.time()

duration =endTime -startTime

logging.info('Timeline Duration: '+str(duration)+' seconds')