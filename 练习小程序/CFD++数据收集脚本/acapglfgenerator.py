#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time


targetfilename='mcfd.acap'                           #for different target file
timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())
filename='data_statistic'+timenow+'.txt'

glf_pre=[   'set _TMP(mode_1) [pw::Application begin Create]\n',
            '  set _TMP(PW_1) [pw::SegmentSpline create]\n',]
glf_back=[  '  set _CN(1) [pw::Connector create]\n',
            '  $_CN(1) addSegment $_TMP(PW_1)\n',
            '  unset _TMP(PW_1)\n',
            '  $_CN(1) calculateDimension\n',
            '$_TMP(mode_1) end\n',
            'unset _TMP(mode_1)\n',
            'pw::Application markUndoLevel {Create 2 Point Connector}\n',]



'  $_TMP(PW_1) addPoint {-10 5 -0}'
'  $_TMP(PW_1) addPoint {0 0 0}'





scale_factor=1000
x= 0*scale_factor
y=30*scale_factor
z=30*scale_factor

num_collected=0                                         #count how many files were collected
num_Nonstandard=0                                       #count how many non_standard files were detected


def acapread():
    try:
        file=open(targetfilename,'r')                       #test if target file exists
    except:
        return 0
    wholeTxt=file.readlines()                               #read all the file
    file.close                                              #close file after read
    length=len(wholeTxt)
    i=0
    while i <length:
        length=len(wholeTxt)
        if i >len(wholeTxt)-1:
            break
        if wholeTxt[i][0]=='#':
            wholeTxt.pop(i)
            i=i
            continue
        else:
            wholeTxt[i]=(wholeTxt[i].split())[3:6]
            wholeTxt[i] = list(map(float, wholeTxt[i]))
            wholeTxt[i] = list(map(lambda x:x*scale_factor, wholeTxt[i]))
        i=i+1
    return wholeTxt

def glf_write(nums):
    file=open('ACAP_pos.glf','w')
    file.write('package require PWI_Glyph 5.18.5\n')
    times=0
    for j in nums:
        for i in glf_pre:
            file.write(i)
        file.write('  $_TMP(PW_1) addPoint {%.3f %.3f %.3f}\n'%(j[0],j[1],j[2],))
        file.write('  $_TMP(PW_1) addPoint {%.3f %.3f %.3f}\n'%(x,times//10*500+y,times%10*500+z))
        for i in glf_back:
            file.write(i)
        file.write('\n')
        times+=1


def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                                       #first change into target dir
    result=acapread()
    if result!=0:
        glf_write(result)
    secondarydirlsit=os.listdir(ini_dir)                    #list the secondary dics of the initial dir
    secondarydirlsit.sort()                                 #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            traversedir(wholedir)                           #self recall to traverse secondary dirs      
        else:
            continue


def write_log(text,write_time=0):
    print(text)


if __name__=='__main__':
    rootDir=input("please enter target dir:")
    traversedir(rootDir)
    print('%d file(s) were collected'%num_collected)
    print('%d non_standard file(s) detected'%num_Nonstandard)
    print('all done! please check file data_statistic.txt at origial dic')

