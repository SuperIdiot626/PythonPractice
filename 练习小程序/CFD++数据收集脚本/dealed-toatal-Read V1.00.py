#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#this program can calculte the latest 50 steps' average data, and output the last 8 rows of data, and the L/D data. can traverse all the secondary dirs.

import os 
dataneeded=[]
targetfilename='dealed-total-cof-zx.txt'                    #for different target file
num_collected=0

def readfile():
    global dataneeded
    file=open(targetfilename,'r') 
    wholefile=file.readlines()
    for num,line in enumerate(wholefile):
        if line[-5:]=='all \n':
            a=wholefile[num+2]
            a=a.split('\t')
            while '' in a:
                a.remove('')
            a.remove('\n')
            b=[a[0]]
            b.extend( [     float(a[8])  ,  float(a[-1])       ] )
            print(b)
            dataneeded.append(b)
            a=wholefile[num+3]
            a=a.split('\t')
            while '' in a:
                a.remove('')
            a.remove('\n')
            b=[a[0]]
            b.extend( [     float(a[8])  ,  float(a[-1])       ] )
            print(b)
            dataneeded.append(b)

def writetxt():
    os.chdir(rootDir)
    file=open('wyz.txt','w') 
    for data in dataneeded:
        for num,i in enumerate(data):
            i=str(i)
            if num==0:
                i=i.ljust(110,' ')
            file.write(i+'\t')
        file.write('\n')
    file.close()

rootDir=input("please enter target dir:")
os.chdir(rootDir)
readfile()
writetxt()



print('%d file(s) were collected'%num_collected)
print('all done! please check file data_statistic.txt at origial dic')

#2021年8月18日17:30:25 增加了输出文件检测功能。优化了部分细节