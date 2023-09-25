#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

import os

dir=input('Please enter your target dir: ')
os.chdir(dir)
file=open('namelist.txt','r')
namelist=file.read().split()
#print(namelist)



dir_list=os.listdir()
i=0
for dir in dir_list:
    if  os.path.isfile(dir):
        continue
    try:
        os.rename(dir,namelist[i])
    except:
        exit()
    i+=1



#说明
#与Dirnames.txt文件配合使用
#可以根据读取的的内容来命名目录下的文件夹。

#V1.00 2022年6月25日14:11:57
#更新内容：
#1.完成了基本功能
#Todo：
#1.当namelist数量比dir少的时候会有bug，尝试修复

#V1.01 2022年6月25日13:47:12
#更新内容：
#1.修复了namelist数量比dir少的时报错的bug
#Todo：
#暂无