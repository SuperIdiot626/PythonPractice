#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 
import os
def main():
    writen_num=0
    dire_location=input('please enter the location of your calculation files:')
    os.chdir(dire_location)
    secondary_dires=os.listdir(dire_location)
    secondary_dires.sort()
    for dir in secondary_dires:
        wholedir=os.path.join(dire_location,dir)
        if os.path.isdir(wholedir):
            os.chdir(wholedir)       
            try:
                file=open('job1.cfd','r')
            except:
                continue
            texts=file.readlines()
            texts[2]='#PBS -N '+dir+'\n'
            file.close()
            file=open('job1.cfd','w')
            for i in texts:
                file.write(i)
            file.close
            writen_num+=1
    print('All done! '+str(writen_num)+' files written in total!')

main()

#可以把文件夹下的job1.cfd的任务名改成和文件夹名相同