#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time


targetfilename_pre='minfo1_e'                           #for different target file
timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())
filename='data_statistic'+timenow+'.txt'

entry_num=50                                            #the num of minfo1_e files
show_everything=1

show_avera=show_everything                              #set whether calculate the ave_data value
avera_steps=1000                                        #how many steps to cal the ave_data

show_gap =show_everything                               #set whether show a gap step
gap_steps=1000                                          #set the value of gap

show_resi=show_everything

pri_dir=1                                               #directory the case in 
pri_title=0                                             #the meaning of data
isdetail=0                                              #all data will show if set 1

pri_steps=1                                             #steps, this should usually be 1
pri_time=1                                              #time

pri_energy=1                                            #energy flux
pri_mass  =1                                            #mass flux
pri_Fx=1                                                #force at X direction
pri_Fy=1                                                #force at Y direction
pri_Fz=1                                                #force at Z direction
pri_Mx=1                                                #momentum object to axis X
pri_My=1                                                #momentum object to axis Y
pri_Mz=1                                                #momentum object to axis Z
pri_Fx_coe=1                                            #force coefficient at X direction
pri_Fy_coe=1                                            #force coefficient at Y direction
pri_Fz_coe=1                                            #force coefficient at Z direction
pri_Mx_coe=1                                            #momentum coefficient object to axis X
pri_My_coe=1                                            #momentum coefficient object to axis Y
pri_Mz_coe=1                                            #momentum coefficient object to axis Z
pri_LiftCoe=1                                           #lift coefficient
pri_DragCoe=1                                           #drag coefficient
pri_LD_ratio=1                                          #Lift/Drag ratio

num_collected=0                                         #count how many files were collected
num_Nonstandard=0                                       #count how many non_standard files were detected

title=[ '      steps','       time',
        'energy_flux','  mass_flux',
        '    force_x','    force_y','    force_z',
        '   moment_x','   moment_y','   moment_z',
        '    f_coe_x','    f_coe_y','    f_coe_z',
        '    m_coe_x','    m_coe_y','    m_coe_z',
        '   lift_coe','   drag_coe','     LD_coe',]
output=[    pri_steps   ,pri_time,
            pri_energy  ,pri_mass,
            pri_Fx      ,pri_Fy     ,pri_Fz,
            pri_Mx      ,pri_My     ,pri_Mz,
            pri_Fx_coe  ,pri_Fy_coe ,pri_Fz_coe,
            pri_Mx_coe  ,pri_My_coe ,pri_Mz_coe,
            pri_LiftCoe ,pri_DragCoe,pri_LD_ratio,]

def dataWrite(resultfile,data,output_mode,data_exist):
    if pri_steps==1:                                    #以下内容用于使输出更规范
        if output_mode==1:
            front_line=                           "       the  latest  step:"
            resultfile.write(front_line)
        if output_mode==2:
            front_line=str(int(avera_steps)).ljust(8,' ')+"  steps' average:"
            resultfile.write(front_line)
        if output_mode==4:
            front_line=str(int(gap_steps  )).ljust(8,' ')+"aver data's resi:"
            resultfile.write(front_line)
        
        if output_mode==3:
            front_line=str(int(gap_steps  )).ljust(8,' ')+"  steps'  before:"
            resultfile.write(front_line)
        if output_mode==5:
            front_line=str(int(gap_steps  )).ljust(8,' ')+" gap data's resi:"
            resultfile.write(front_line)
    
    if isdetail==0:
        if output_mode in [1,2,3]:
            for index,item in enumerate(output):
                if data_exist[index]==1:                        #if this data exists
                    data_to_be=data.pop(0)                      #pop it out
                    if output[index]==1:                        #if this data needs to be written
                        resultfile.write(' %14.7e'%data_to_be)
            resultfile.write('\n')

        if output_mode in [4,5]:
            for index,item in enumerate(output):
                if data_exist[index]==1:
                    data_to_be=data.pop(0)
                    if output[index]==1:
                        resultfile.write(' %13.3f%%'%(data_to_be*100))
            resultfile.write('\n')
    
    if isdetail==1:
        if output_mode in [1,2,3]:
            for index,item in enumerate(output):
                if data_exist[index]==1:                        #if this data exists
                    data_to_be=data.pop(0)                      #pop it out
                    if output[index]==1:                        #if this data needs to be written
                        resultfile.write(' %14.7e'%data_to_be)
                if data_exist[index]==0:                        #if this data exists
                    if output[index]==1:                        #if this data needs to be written
                        resultfile.write('%15s'%None)
            resultfile.write('\n')

        if output_mode in [4,5]:
            for index,item in enumerate(output):
                if data_exist[index]==1:
                    data_to_be=data.pop(0)
                    if output[index]==1:
                        resultfile.write(' %13.3f%%'%(data_to_be*100))
                if data_exist[index]==0:                        #if this data exists
                    if output[index]==1:                        #if this data needs to be written
                        resultfile.write('%15s'%None)
            resultfile.write('\n')


def datacollect(dir,targetfilename):                                       #function to collect data
    global num_collected
    global num_Nonstandard
    global avera_steps
    try:
        file=open(targetfilename,'r')                       #test if target file exists
    except:
        return 0

    wholeTxt=file.readlines()                               #read all the file
    file.close                                              #close file after read

    keyword=wholeTxt[0].split(' ')[1]
    if   keyword=='energy_flux':
        data_exist=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='mass_flux':
        data_exist=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='x_force':
        data_exist=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='y_force':
        data_exist=[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='z_force':
        data_exist=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='x_moment':
        data_exist=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='y_moment':
        data_exist=[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,]
    elif keyword=='z_moment':
        data_exist=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,]
    elif keyword=='all':
        data_exist=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
    elif keyword=='fluxes':
        data_exist=[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='forces':
        data_exist=[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,]
    elif keyword=='moments':
        data_exist=[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,]
    elif keyword=='forces_moments':
        data_exist=[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,]
    elif keyword=='coefficients':
        data_exist=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,]
    outputNum=sum(data_exist)
    result=[]
    for i in range(outputNum+2):
        result.append(0)
    if pri_LD_ratio==1:
        result.append(0)

    i=1
    while wholeTxt[i][0]=='#':                          #clear all non-data lines
        i=i+1
    wholeTxt.reverse()
    wholeTxt=wholeTxt[0:-i]                             #clear all non-data lines
    while wholeTxt[0]=='\n':                            #in case data detled manually
        wholeTxt.pop(0)
    
    
    
    
    final_row=wholeTxt[0].split(' ')                    #split the line with space and delete all of them
    while '\n' in final_row:                          #if calculation stoped manually it ends with data
        final_row.remove('')
    while '' in final_row:                            #if calculation stoped automaticly it ends with \n
        final_row.remove('')
    for j,data in enumerate(final_row):                 #str to float
        final_row[j]=float(data)
    if pri_LD_ratio==1 and data_exist[-1]==1:           #data_exist[-1]==1, must be coefficient or all
            try:
                final_row.append(final_row[-2]/final_row[-1])
            except ZeroDivisionError:
                final_row.append(0)


    if show_gap:
        try:
            gap_data=wholeTxt[gap_steps]
        except IndexError:
            gap_data=wholeTxt[-1]
            write_log('    gap number exceeds in %s'%dir)
        gap_data=(gap_data[:-1]).split(' ')             #split the line with space and delete all of them                        
        while '' in gap_data:                           
            gap_data.remove('')
        for i,data in enumerate(gap_data):              #str to float
            gap_data[i]=float(data)
        if pri_LD_ratio==1 and data_exist[-1]==1:       #data_exist[-1]==1, must be coefficient or all
            try:
                gap_data.append(gap_data[-2]/gap_data[-1])
            except ZeroDivisionError:
                gap_data.append(0)

        if show_resi and show_gap:
            gap_resi=result[:]                          #initialize the resi data
            for i,data in enumerate(final_row):
                try:
                    gap_resi[i]=abs((gap_data[i]-final_row[i])
                                        /(final_row[i]))
                except ZeroDivisionError:
                    gap_resi[i]=0


    if show_avera:
        if avera_steps>len(wholeTxt):
            print('average number exceeds in %s'%dir)
        wholeTxt=wholeTxt[0:avera_steps]                #only need some last lines
        ave_data=result[:]                              #initial value of ave_data
        for i,line in  enumerate(wholeTxt):
            line=line.split(' ')                        #split the line with space and delete all of them
            while '\n' in line:                         #if calculation stoped manually it ends with data
                line.remove('\n')                       #if calculation stoped automaticly it ends with \n
            while '' in line:
                line.remove('')
            for j,data in enumerate(line):              #add all the data
                line[j]=float(data)
                if show_avera:
                    ave_data[j]+=line[j]

        for i,data in enumerate(ave_data):              #calculate average data
            ave_data[i]=data/len(wholeTxt)

        if pri_LD_ratio==1 and data_exist[-1]==1:       #data_exist[-1]==1, must be coefficient or all
            try:
                ave_data[-1]=(ave_data[-3]/ave_data[-2])
            except ZeroDivisionError:                   #(sigma(An/Bn))/n != sigma(An)/sigma(Bn)
                ave_data[-1]=0                          #but the last one is easier

        if show_resi and show_avera:                    #calculate residual
            ave_resi=result[:]                          #initialize the resi data
            for i,data in enumerate(final_row):
                try:
                    ave_resi[i]=abs((ave_data[i]-final_row[i])
                                        /(final_row[i]))
                except ZeroDivisionError:
                    ave_resi[i]=0

    current_dir=os.getcwd()
    os.chdir(rootDir)
    statistical_result=open(filename,'a')               #open the statistic file and recorC:\Users\WYZ\Desktop\CaoPuyud
    if pri_dir==1:
        statistical_result.write(dir+'%15s'%targetfilename)
    
    
    data_exist=[1,1,]+data_exist+[pri_LD_ratio*data_exist[-1],]


    for index,item in  enumerate(data_exist):
        if isdetail==1:
            statistical_result.write('%15s'%title[index])
        elif pri_title==1:
            if data_exist[index]==1:
                if   output[index]==1:
                    statistical_result.write('%15s'%title[index])
    statistical_result.write('\n')


    dataWrite(    statistical_result, final_row ,1,data_exist)
    if show_avera==1:
        dataWrite(statistical_result, ave_data  ,2,data_exist)
    if show_resi==1 and show_avera==1:
        dataWrite(statistical_result, ave_resi  ,4,data_exist)

    if show_gap==1:
        dataWrite(statistical_result, gap_data  ,3,data_exist)
    if show_resi==1 and show_gap==1:
        dataWrite(statistical_result, gap_resi  ,5,data_exist)
    statistical_result.close
    os.chdir(current_dir)
    num_collected+=1
    print(current_dir+' %12s '%targetfilename+' collected')


def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    os.chdir(ini_dir)                                       #first change into target dir
    for i in range(entry_num):
        targetfilename=str(targetfilename_pre+str(i+1))
        datacollect(ini_dir,targetfilename)                 #check if there is target file in the initial dir
    
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


#v1.99 2022年9月15日18:10:47
#更新内容：
#1.可以针对任意的输出对象进行统计了
#2.可以针对任意个entry文件进行统计了
#3.可以写入输出量的title了
#4.精简了大部分代码
#5.删除了tkinter的UI界面
#toDo：
#暂无

#v2.00 2022年9月15日18:10:47
#更新内容：
#修复了一些在节点上才能发现的bug，
#1.无法穿文件夹识别多个minfo1_e*的bug
#2.平均值无法正常显示升阻比的bug
#3.无法关闭title显示的bug
#增加了一些功能
#1.增加了实时显示被统计对象的功能
#toDo：
#暂无
