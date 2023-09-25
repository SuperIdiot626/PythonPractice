#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

import os

wirte_mcfd_inp=1            # 需要写入哪些文件就将其值设为1，否则设为零
wirte_job1_cfd=1
wirte_infout_inp=1
wirte_tecout_inp=1

def main():
    templateread=0
    nums=0
    states_location,dire=reference_input()
    states=states_readin(states_location)
    for i in range(len(states)):
        dirname=states[i][0]
        state=states[i][1:]
        secondary_dir=os.path.join(dire,states[i][0])
        try:
            os.chdir(secondary_dir)
        except  FileNotFoundError:
            print(secondary_dir+' not Found')
            continue

        if templateread==0:
            if wirte_mcfd_inp  ==1: 
                Pt_mcfdinp=template_read('mcfd.inp')
            if wirte_job1_cfd  ==1: 
                Pt_job1cfd=template_read('job1.cfd')
            if wirte_infout_inp==1: 
                Pt_infout1f=template_read('infout1f.inp')
            
            templateread=1

        if wirte_mcfd_inp  ==1:
            write_mcfd_inp_func(Pt_mcfdinp,state[0:5])
        if wirte_job1_cfd  ==1:
            wirte_job1_cfd_func(Pt_job1cfd,dirname)
        if wirte_infout_inp==1:
            wirte_infout_inp_func(Pt_infout1f,state)
        if wirte_tecout_inp==1:
            wirte_tecout_inp_func()
        nums+=1
        print('file written in '+dirname)
    total=wirte_mcfd_inp+wirte_job1_cfd+wirte_infout_inp+wirte_tecout_inp
    print(total*nums,' files created in corresponding dir')

def filewriteParts(file,part):
    for i in part:
        file.write(i)

def reference_input():
    states_location=input('please enter the location of your states.txt file:')
    dire_location=input('please enter the location of your calculation files:')
    states_location+='/states.txt'
    return states_location,dire_location

def states_readin(states_location):
    txtfile=open(states_location,'r')
    text=txtfile.readlines()
    text=text[1:]
    for i in range(len(text)):
        text[i]=text[i].split()
    return text

def template_read(name):
    try:
        file=open(name,'r')
    except FileNotFoundError:
        print(name+' template file not Found!')
        exit()
    text=file.readlines()
    file.close()
    return text

def write_mcfd_inp_func(text,states ):
    for i in text:
        if i[-22:-1]=='primitive_variables_2':
            index=text.index(i)
            break
    file=open('mcfd.inp','w')
    filewriteParts(file,text[:index+1])
    file.write('values ')
    for j in states:
        file.write(j+' ')
    file.write('\n')
    filewriteParts(file,text[index+2:])
    file.close()
    print('mcfd.inp ',end='')

def wirte_job1_cfd_func(text,dirname):
    file=open('job1.cfd','w')
    filewriteParts(file,text[:2])
    file.write('#PBS -N '+dirname+'\n')
    filewriteParts(file,text[3:])
    file.close()
    print('job1.cfd ',end='')

def wirte_infout_inp_func(text,states):
    pref=float(states[0])
    tref=float(states[1])
    vx  =float(states[2])**2
    vy  =float(states[3])**2
    vz  =float(states[4])**2

    air_constant=287.1848
    rref=pref/tref/air_constant
    uref=(vx+vy+vz)**0.5

    file=open('infout1f.inp','w')
    filewriteParts(file,text[:-13] )
    file.write('pref %e\n'%pref)
    file.write('rref %e\n'%rref)
    file.write('uref %e\n'%uref)

    filewriteParts(file,text[-10:-4] )
    file.write('alpha '+states[-1]+'\n')
    filewriteParts(file,text[-3:] )
    file.close()
    print('infout1f.inp ',end='')

def wirte_tecout_inp_func():
    file=open('tecout.inp','w')
    file.write('1\n1\n')
    file.close()
    print('tecout.inp ',end='')  

main()

#说明
#与states.txt文件配合使用
#可以自动读入文件夹名称以及来流数据
#可以将第一个文件夹下的mcfd.inp、job1.cfd、infout.inp文件进行复制
#然后在剩余文件夹下进行粘贴，并修改其中的某些数据
#修改的数据对应关系如下：
#mcfd.inp:      读取states.txt文件中的来流参数，修改对应温度压力以及三向速度
#job1.cfd:      读取将job的名称设置为与文件夹名称相同
#infout.inp:    读取states.txt的内容，并自动修改参考压力、密度、速度以及攻角。
#               其中密度速度均为计算得到，计算所用气体常数为287.1848
#注意，其余任何未提到的数据都不会进行修改

#1.00
#更新内容
#1.按照实际运行情况修改了部分代码，使之可以在linux上运行
#2.完成了目前所有功能
#toDo：
#增加自动填写参考量的功能

#v1.10
#更新内容：
#1.按照需求增加了infout1f.inp文件的自动填写参考压力密度速度的功能。
#2.精简了代码。
#3.修改了说明
#toDo：
#尝试增加湍流初始化的功能

#v1.11
#更新内容：
#1.在内部机上测试了1.10版本软件，修改了细节：
#       ①在写入来流数据时，从读取前几个字符改为后几个
#       ②优化了部分代码结构，提升了可读性（删除了一些空格）
#2.修改了一些个bug：
#       ①在写job1.cfd时写入的是压力数据
#       ②在写入mcfd文件时名称错误。
#toDo：
#尝试增加湍流初始化的功能