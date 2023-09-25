#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 


num=0                                                   #count how many files were collected
targetfilename='minfo1_e1'                              #for different target file
rootDir=input("please enter target dir:")
#rootDir="D:\Code\Python\练习小程序\数据"

def datacollect(dir):                                   #function to collect data
    global num
    try:
        file=open(targetfilename,'r')                   #test if target file exists
    except:
        return 0
    wholeTxt=file.readlines()                           #read all the file
    file.close                                          #close file after read
    wholeTxt.reverse()
    wholeTxt=wholeTxt[0:50]                             #only need the last 50 lines 
    #print(wholeTxt[0])
    average=[0,0,0,0,0,0,0,0,0]                         #initial value of average
    for i,line in  enumerate(wholeTxt):
        line=(line[:-1]).split(' ')                     #split the line with space and delete all of them
        while '' in line:
	        line.remove('')
        del line[1]                                     #delete the first useless data
	
        for j,data in enumerate(line):                  #add all the data
            average[j]+=float(line[j])
        wholeTxt[i]=line                                #set the data
        #del wholeTxt[i][1]
    for i,data in enumerate(average):                   #calculate average data
        average[i]=data/50

    os.chdir(rootDir)
    statistical_result=open('data_statistic.txt','a')   #open the statistic file and record 
    statistical_result.write(dir+'\n')

    statistical_result.write("    latest steps          "+wholeTxt[0][0]+'     ') 
    for i in wholeTxt[0][1:]:
        statistical_result.write(i+'  ') 
    lift_coe=float(wholeTxt[0][-2])
    drag_coe=float(wholeTxt[0][-1])
    statistical_result.write('L/D=') 
    try:
        statistical_result.write(str(lift_coe/drag_coe)[:10]) 
    except ZeroDivisionError:
        statistical_result.write('divided by zero') 
    statistical_result.write('\n')

    statistical_result.write('average for near 50 steps ') 
    for i,data in enumerate(average):
        if i==0:
            statistical_result.write('%d'%data+'      ')
        else:
            statistical_result.write('%1.7e'%data+'   ') 
    statistical_result.write("L/D=") 
    try:
        statistical_result.write(str(average[-2]/average[-1])[:10]) 
    except ZeroDivisionError:
        statistical_result.write('divided by zero')
    statistical_result.write('\n')

    statistical_result.write('\n')
    statistical_result.close
    num+=1

def traversedir(ini_dir):                           #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                               #first change into target dir
    datacollect(ini_dir)                            #check if there is target file in the initial dir
    secondarydirlsit=os.listdir(ini_dir)            #list the secondary dics of the initial dir
    secondarydirlsit.sort()                         #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            print(wholedir)                         #show which dirs were collected 
            traversedir(wholedir)                   #self recall to traverse secondary dirs      
        else:
            continue

    
traversedir(rootDir)

print('%d files were collected'%num)
print('all done! please check file data_statistic.txt at origial dic')
