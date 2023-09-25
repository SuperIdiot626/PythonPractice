#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#this program can calculte the latest 50 steps' average data, and output the last 8 rows of data, and the L/D data. can traverse all the secondary dirs.

import os 

targetfilename='minfo1_e1'                              #for different target file

pri_dir=1

show_avera=1                                            #set whether calculate the average value
avera_steps=1000                                         #how many steps to cal the average

show_gap=1                                              #set whether show a gap step
gap_steps=1000                                          #set the value of gap

pri_steps=1                                             #steps, this should usually be 1
pri_time=1                                              #time
pri_Fx=1                                                #force at X direction
pri_Fy=1                                                #force at Y direction
pri_Fz=1                                                #force at Z direction
pri_Mx=1                                                #momentum object to axis X
pri_My=1                                                #momentum object to axis Y
pri_Mz=1                                                #momentum object to axis Z
pri_LiftCoe=1                                           #lift coefficient
pri_DragCoe=1                                           #drag coefficient
pri_LD_ratio=1                                          #Lift/Drag ratio


num_collected=0                                         #count how many files were collected
num_Nonstandard=0                                       #count how many non_standard files were detected


def dataWrite(resultfile,data,output_mode):

    if pri_steps==1:                                    #以下内容用于使输出更规范
        if output_mode==1:
            resultfile.write("          the  latest  step:%7d"%data[0])
        if output_mode==2:
            front_line=str(int(avera_steps)).ljust(7,' ')+" steps' average:   "
            resultfile.write(front_line+str(int(data[0])))
        if output_mode==3:
            front_line=str(int(gap_steps)).ljust(7,' ')+"steps'  before :   "
            resultfile.write(front_line+str(int(data[0])))
    if pri_time==1:
        resultfile.write(' %14.7e'%data[1])
    if pri_Fx==1:
        resultfile.write(' %14.7e'%data[2])
    if pri_Fy==1:
        resultfile.write(' %14.7e'%data[3])
    if pri_Fz==1:
        resultfile.write(' %14.7e'%data[4])
    if pri_Mx==1:
        resultfile.write(' %14.7e'%data[5])
    if pri_My==1:
        resultfile.write(' %14.7e'%data[6])
    if pri_Mz==1:
        resultfile.write(' %14.7e'%data[7])
    if pri_LiftCoe==1:
        resultfile.write(' %14.7e'%data[8])
    if pri_DragCoe==1:
        resultfile.write(' %14.7e'%data[9])
    if pri_LD_ratio==1:
        try:
            resultfile.write('  L/D=%14.7e'%(data[8]/data[9]))
        except ZeroDivisionError:
            resultfile.write('divided by zero')
    resultfile.write('\n') 

def datacollect(dir):                                       #function to collect data
    global num_collected
    global num_Nonstandard
    try:
        file=open(targetfilename,'r')                       #test if target file exists
    except:
        return 0

    wholeTxt=file.readlines()                               #read all the file
    file.close                                              #close file after read

    if wholeTxt[0].split(' ')[1]=="coefficients":           #check if file is output by "coefficients" 
        
        wholeTxt.reverse()
        wholeTxt=wholeTxt[0:-12]

        if show_gap:
            try:
                gap_data=wholeTxt[gap_steps]
            except IndexError:
                gap_data=wholeTxt[-1]
            gap_data=(gap_data[:-1]).split(' ')             #split the line with space and delete all of them
            while '' in gap_data:
                gap_data.remove('')
            for i,data in enumerate(gap_data):              #str to float
                gap_data[i]=float(data)

        if show_avera:
            wholeTxt=wholeTxt[0:avera_steps]                #only need some last lines
            average=[0,0,0,0,0,0,0,0,0,0]                   #initial value of average

        for i,line in  enumerate(wholeTxt):
            line=(line[:-1]).split(' ')                     #split the line with space and delete all of them
            while '' in line:
                line.remove('')
            for j,data in enumerate(line):                  #add all the data
                line[j]=float(data)
                if show_avera:
                    average[j]+=line[j]
            wholeTxt[i]=line                                #set the data

        if show_avera:
            for i,data in enumerate(average):               #calculate average data
                average[i]=data/len(wholeTxt)

        os.chdir(rootDir)
        statistical_result=open('data_statistic.txt','a')   #open the statistic file and recorC:\Users\WYZ\Desktop\CaoPuyud
        #statistical_result.write('\n')
        if pri_dir==1:
            statistical_result.write(dir+'\n')
        dataWrite(statistical_result,wholeTxt[0],1)
        if show_avera==1:
            dataWrite(statistical_result,average,2)
        if show_gap==1:
            dataWrite(statistical_result,gap_data,3)
        statistical_result.close
        num_collected+=1

        print("%s collected"%dir)                           #show which dirs were collected
        
    else:
        num_Nonstandard+=1
        print('Non_standard file decteced in %s'%dir)

def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                                       #first change into target dir
    datacollect(ini_dir)                                    #check if there is target file in the initial dir
    secondarydirlsit=os.listdir(ini_dir)                    #list the secondary dics of the initial dir
    secondarydirlsit.sort()                                 #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            traversedir(wholedir)                           #self recall to traverse secondary dirs      
        else:
            continue


rootDir=input("please enter target dir:")
#rootDir="D:\Code\Python\练习小程序\数据" 
traversedir(rootDir)
print('%d file(s) were collected'%num_collected)
print('%d non_standard file(s) detected'%num_Nonstandard)
print('all done! please check file data_statistic.txt at origial dic')

#2021年8月18日17:30:25 增加了输出文件检测功能。优化了部分细节