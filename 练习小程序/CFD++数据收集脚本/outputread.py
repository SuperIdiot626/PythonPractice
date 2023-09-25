#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

import os,time

def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                                       #first change into target dir
    output_read(ini_dir)                                    #check if there is target file in the initial dir
    secondarydirlsit=os.listdir(ini_dir)                    #list the secondary dics of the initial dir
    secondarydirlsit.sort()                                 #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            traversedir(wholedir)                           #self recall to traverse secondary dirs
        else:
            continue

def output_read(dir):
    global rootdir
    os.chdir(dir)
    try:
        file=open('output','r')
    except FileNotFoundError:
        return 0
    catch=0
    text=file.readlines()
    text=text[::-1]
    print(text[0][:15])
    if text[0][:15]=='MPI Application':
        os.chdir(rootdir)
        record=open(filename,'a')
        record.write(dir+'\n')
        record.write('Dead Case Found\n')
        record.close()

    for i in text:
        if i[:18]=='Timestamp at Step#':
            laststamp=text.index(i)
            step_time=i[18:].split(':',1)
            time_str= step_time[1].split()[1:]
            
            catch=1
            break
    if catch==0:
        os.chdir(rootdir)
        record=open(filename,'a')
        record.write(dir+'\n')
        record.write('Nothing found just started\n')
        record.close() 
        return 0
    
    

    if laststamp==0 or text[laststamp-1][:4]=='FILE':
        cflline=laststamp+2
        cfl=float(text[cflline].split()[-1])
        step= step_time[0]
    elif laststamp-5>0:
        laststamp-=5
        while laststamp-4>0:
            laststamp-=4
        step=text[laststamp].split()[0]
        cflline=laststamp-2
        cfl=float(text[cflline].split()[-1])
    
    time_gap=time_to_now(time_str)
    print(dir,end=', ')
    print('last step '+step,end=', ')
    print('CFL '+'%.3e'%cfl,end=', ')
    print('time gap '+time_gap)
    os.chdir(rootdir)
    record=open(filename,'a')
    record.write(dir+'\n')
    record.write('last step '+step+', ')
    record.write('CFL '+'%.3e'%cfl+', ')
    record.write('time gap since then '+time_gap+'\n')
    record.close()



def time_to_now(str_time,choose=3):
    monthlist=[ 'Jan','Feb','Mar','Apr','May','Jun',
            'Jul','Aug','Sept','Oct','Nov','Dec',]
    if choose==1:       #秒
        parameter=1
        unit=' secs'
    if choose==2:       #分钟
        parameter=60
        unit=' mins'
    if choose==3:       #小时
        parameter=3600
        unit=' hours'
    if choose==4:       #天
        parameter=86400
        unit=' days'
    
    strtime=str_time[-1]+'-'+str(monthlist.index(str_time[0])+1)
    strtime=strtime+'-'+str_time[1]+' '+str_time[-2]
    timestamp_then=time.strptime(strtime, '%Y-%m-%d %X')
    timestamp_then=time.mktime(timestamp_then)
    timestamp_now=time.time()
    time_gap=(timestamp_now-timestamp_then)/parameter
    return ('%.2f'%time_gap)+unit
timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())
filename='output_record'+timenow+'.txt'

rootdir=input('please input yout target directory: ')
traversedir(rootdir)



#说明
#可以读取output文件，可以查看目前最大计算步数以及当前的cfl数等数据，目前只能看一个

#0.99     
#更新内容
#完成了最基本的功能，可以对单个文件夹进行输出了。
#toDo：
#1.增加穿越次级文件夹的功能
#2.尝试输出真最后一步，而不是最后的整十步
#3.增加cfl平均统计功能
#4.查看算例是否完成、被杀以及已死等功能

#1.00     
#更新内容
#1.可以穿越文件夹了
#2.在算例刚开始的时候也可以读取了
#toDo：
#1.尝试输出真最后一步，而不是最后的整十步
#2.增加cfl平均统计功能
#3.查看算例是否完成、被杀以及已死等功能

#1.01
#更新内容
#1.增加了结果加时间的功能
#toDo：
#暂无