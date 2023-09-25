#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

import os
import time


def main():
    dir=input('please input yout target directory: ')
    os.chdir(dir)
    file=open('output','r')
    text=file.readlines()
    text=text[::-1]
    for i in text:
        if i[:18]=='Timestamp at Step#':
            laststamp=text.index(i)
            cflline=laststamp+2
            step_time=i[18:].split(':',1)
            time_str= step_time[1].split()[1:]
            step= step_time[0]
            break
    cfl=float(text[cflline].split()[-1])
    time_gap=time_to_now(time_str)
    print('last step is '+step,end=', ')
    print('CFL is '+'%.3e'%cfl,end=', ')
    print('time gap since then is '+time_gap)

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

main()


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

