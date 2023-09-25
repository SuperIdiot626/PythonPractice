#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#this program can calculte the latest 50 steps' average data, and output the last 8 rows of data, and the L/D data. can traverse all the secondary dirs.

import os 

fileneeded=[]
num_collected=0

def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                                       #first change into target dir
    secondarydirlsit=os.listdir(ini_dir)                    #list the secondary dics of the initial dir
    secondarydirlsit.sort()                                 #sort the dir list
    for dir in secondarydirlsit:
        if dir[-3:]=='log':
            record(dir)
        else:
            continue
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        record('\n')
        if os.path.isdir(wholedir):
            traversedir(wholedir)
        else:
            continue

def record(filename):
    global fileneeded
    fileneeded.append(filename)

def writetxt(fileneeded):
    filename_previous=''
    os.chdir(rootDir)
    file=open('zx.txt','w') 
    file.write('ar\n')
    file.write('* 3 0\n')
    for filename in fileneeded:
        if filename=='\n':
            if filename_previous=='\n':
                continue
            else:
                file.write('\n')
                filename_previous=filename
        else:
            file.write(filename+'\n')
            filename_previous=filename
    file.close()

rootDir=input("please enter target dir:")
#rootDir="D:\Code\Python\练习小程序\数据" 
traversedir(rootDir)
for filename in fileneeded:
    print(filename)
writetxt(fileneeded)
while '\n' in fileneeded:
    fileneeded.remove('\n')
num_collected=len(fileneeded)
print('%d file(s) were collected'%num_collected)
print('all done! please check file data_statistic.txt at origial dic')

#2021年8月18日17:30:25 增加了输出文件检测功能。优化了部分细节