#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:04:30 2019

@author: hallvardr
"""

import logging, time, sys, os, stat, time, hashlib, argparse, csv

def WalkPath(rootPath, reportPath):
        processCount = 0
        errorCount = 0
        reportPath = os.path.join(reportPath, "Timeline_Results.csv")
        oCVS = _CSVWriter(reportPath)
        if rootPath.endswith('\\') or rootPath.endswith('/'):
            rootPath = rootPath
        else:
            rootPath = rootPath+'/'
        for root, dirs, files in os.walk(rootPath):
            for file in files:
                fname = os.path.join(root, file)
                result = getInfo(fname, file, oCVS)
                if result is True:
                    processCount += 1
                else:
                    errorCount += 1
        oCVS.writerClose()
        return(processCount)
        
def getInfo(theFile, simpleName, o_result):
    if os.path.exists(theFile):
        if not os.path.islink(theFile):
            if os.path.isfile(theFile):
                try:
                    f = open(theFile, 'rb')
                except IOError:
                    logging.warning('Open Failed: '+ theFile)
                    return
                else:
                    try:
                        theFileStats = os.stat(theFile)
                        (mode, ino, dev, nlink,uid, gid, size, atime, mtime, ctime) = os.stat(theFile)
                        rd = f.read()
                    except IOError:
                        f.close()
                        logging.warning('FileAccess Error: ' + theFile)
                        return
                    else:
                        fileSize = str(size)
                        modifiedTime = time.ctime(mtime)
                        accessTime = time.ctime(atime)
                        createdTime = time.ctime(ctime)
                        ownerID = str(uid)
                        groupID = str(gid)
                        fileMode = bin(mode)
                        resultList = [simpleName, theFile, fileSize, modifiedTime, accessTime, createdTime, ownerID, groupID, str(mode)]
                        o_result.writeCSVRow(resultList)
                        return True
            else:
                logging.warning('[' + repr(simpleName)+ ', Skipped NOT a File' + ']')
                return False
        else:
            logging.warning('[' + repr(simpleName) + ',Skipped Link NOT a File' + ']')
            return False
    else:
        logging.warning('[' + repr(simpleName) + ', Path doesNOT exist' + ']')
        return False
    
class _CSVWriter:
    
    def __init__(self, fileName):
        try:
            if (sys.version_info > (3, 0)):
                self.csvFile = open(fileName,'w',newline="\r\n")
            else:
                self.csvFile = open(fileName, 'w')
                tempList = ['File', 'Path', 'Size', 'Modified Time', 'Access Time', 'Created Time', 'Owner', 'Group', 'Mode']
                outStr = ",".join(tempList)
                self.csvFile.write(outStr)
                self.csvFile.write("\n")
        except:
            logging.error('CSV File Open Failure')
            quit()
                        
    def writeCSVRow(self, outList):
        outStr = ",".join(outList)
        self.csvFile.write(outStr)
        self.csvFile.write("\n")
    
    def writerClose(self):
        self.csvFile.close()
    
logging.basicConfig(filename='time_timeline_terminal.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

rootPath=raw_input("\nWrite the root folder path (ex. /root/docs):\n")

reportPath=raw_input("\nWrite the destinetion path (ex./root/results):\n")

startTime = time.time()

filesProcessed = WalkPath(rootPath, reportPath)

endTime = time.time()

duration = endTime - startTime

logging.info('Timeline Duration: ' + str(duration)+' seconds')                      