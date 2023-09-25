#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#this program can calculte the latest 50 steps' average data, and output the last 8 rows of data, and the L/D data. can traverse all the secondary dirs.

import os 

num=0                                                   #count how many files were collected
targetfilename='minfo1_e'                              #for different target file
rootDir=input("please enter target dir:")
#rootDir="D:\Code\Python\练习小程序\数据"

def datacollect(dir,targetfilename):                    #function to collect data
    global num
    os.chdir(dir)
    try:
        file=open(targetfilename,'r')                   #test if target file exists
        #print(targetfilename)
    except:
        return 0
    print(dir,targetfilename)                           #show which dirs were collected
    wholeTxt=file.readlines()                           #read all the file
    file.close                                          #close file after read
    wholeTxt.reverse()
    wholeTxt=wholeTxt[0:1]                              #only need the last 1 line 
    for i,line in  enumerate(wholeTxt):
        line=(line[:-1]).split(' ')                     #split the line with space and delete all of them
        while '' in line:
	        line.remove('')
        del line[1]                                     #delete the first useless data
        wholeTxt[i]=line                                #set the data

    
    os.chdir(rootDir)
    statistical_result=open('data_statistic.txt','a')   #open the statistic file and record 
    statistical_result.write(dir+'\\'+targetfilename+'\n')

    statistical_result.write("    latest steps          "+wholeTxt[0][0]+'      ') 
    statistical_result.write(wholeTxt[0][1]+'   ') 
    #statistical_result.write(wholeTxt[0][2]+'   ') 
    #statistical_result.write(wholeTxt[0][3]+'   ') 
    #statistical_result.write(wholeTxt[0][4]+'   ') 
    #statistical_result.write(wholeTxt[0][5]+'   ') 
    #statistical_result.write(wholeTxt[0][6]+'   ') 
    #statistical_result.write(wholeTxt[0][7]+'   ') 
    #statistical_result.write(wholeTxt[0][8]+'   ') 
    #statistical_result.write(wholeTxt[0][9]+'   ') 
    statistical_result.write('\n')
    statistical_result.close
    num+=1

def traversedir(ini_dir):                           #traverse all dirs, secondary dirs included
    global targetfilename
    os.chdir(ini_dir)                               #first change into target dir
    for i in range(1,43):
        targetfilename='minfo1_e'+str(i)
        datacollect(ini_dir,targetfilename)             #check if there is target file in the initial dir
    secondarydirlsit=os.listdir(ini_dir)            #list the secondary dics of the initial dir
    secondarydirlsit.sort()                         #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            traversedir(wholedir)                   #self recall to traverse secondary dirs      
        else:
            continue

    
traversedir(rootDir)

print('%d files were collected'%num)
print('all done! please check file data_statistic.txt at origial dic')
