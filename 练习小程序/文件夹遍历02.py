#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 

num=0                                               #汇总的数据文件数量

while 1:
    rootDir=input('请输入目标路径：')
    #rootDir="D:\Code\Python\练习小程序\数据"
    try:
        secondarydirlsit=os.listdir(rootDir)        #获得当前目录下的所有文件夹以及文件
    except FileNotFoundError:
        print('路径输入错误,请重新输入')
    else:
        break


for dir in secondarydirlsit:                        #遍历文件夹以及文件
    wholedir=os.path.join(rootDir,dir)              #修改为完整路径
    if os.path.isdir(wholedir):                     #判断是否为文件夹（次级路径）
        os.chdir(wholedir)                          #切换到次级路径下
    else:
        continue
    
    targetfilename='minfo1_e1'                      #目标文件名称+后缀
    file=open(targetfilename,'r')                   #打开该文件
    wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt
    file.close                                      #关闭文件
    wholeTxt.reverse()                              #将表格进行逆序排列，大步数在前，小步数在后
    wholeTxt=wholeTxt[0:1001:1000]
    
    for i,line in  enumerate(wholeTxt):             #遍历每一行,
        line=(line[:-1]).split(' ')                 #去除尾部换行号后按照空格切分
        wholeTxt[i]=line

    os.chdir(rootDir)                                               #切回初始路径
    statistical_result=open('data_statistic.txt','a')               #打开或文件
    statistical_result.write(dir+'\n')                              #写入文件名
    statistical_result.write('最新步数：'+str(wholeTxt[0][0]))
    statistical_result.write('  升力系数：'+str(wholeTxt[0][-2])) 
    statistical_result.write('  阻力系数：'+str(wholeTxt[0][-1]))
    statistical_result.write('\n')  
    statistical_result.write('前1000步步数：'+str(wholeTxt[1][0]))
    statistical_result.write('  升力系数：'+str(wholeTxt[1][-2])) 
    statistical_result.write('  阻力系数：'+str(wholeTxt[1][-1]))      
    statistical_result.write('\n')   
    statistical_result.close                                        #关闭文件
    num+=1

print('总共有%d个数据进行了汇总。'%num)
print('已完成数据汇总，请检查目标路径下的data_statistic.txt文件')