#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

import os

wirte_mcfd_inp=1            # 需要写入哪些文件就将其值设为1，否则设为零
wirte_job1_cfd=1
wirte_infout_inp=1
wirte_tecout_inp=1

def main():
    states_location,dire=reference_input()
    states=states_readin(states_location)
    for i in range(len(states)):
        dirname=states[i][0]
        state=states[i][1:]
        if i==0:
            if wirte_mcfd_inp  ==1: 
                Pt_mcfdinp_1,Pt_mcfdinp_2=template_mcfdinp_read(dire,dirname)
            if wirte_job1_cfd  ==1: 
                Pt_job1cfd_1,Pt_job1cfd_2=template_job1cfd_read(dire,dirname)
            if wirte_infout_inp==1: 
                Pt_infout_1 ,Pt_infout_2 =template_infout_read (dire,dirname)

        secondary_dir=os.path.join(dire,states[i][0])
        try:
            os.chdir(secondary_dir)
        except  FileNotFoundError:
            total=wirte_mcfd_inp+wirte_job1_cfd+wirte_infout_inp+wirte_tecout_inp
            print(total*i,' files created in corresponding dir')
            break

        if wirte_mcfd_inp  ==1:
            write_mcfd_inp_func(Pt_mcfdinp_1,Pt_mcfdinp_2,state[0:5])
        if wirte_job1_cfd  ==1:
            wirte_job1_cfd_func(Pt_job1cfd_1,Pt_job1cfd_2,states[i][0])
        if wirte_infout_inp  ==1:
            wirte_infout_inp_func(Pt_infout_1 ,Pt_infout_2,state[5])
        if wirte_tecout_inp==1:
            wirte_tecout_inp_func()
        
        print('file written in '+dirname)

def filewriteParts(file,part):
    for i in part:
        file.write(i)

def reference_input():
    states_location=input('please enter the location of your states.txt file:')
    dire_location=input('please enter the location of your calculation files:')
    states_location+='\\states.txt'
    return states_location,dire_location

def states_readin(states_location):
    txtfile=open(states_location,'r')
    text=txtfile.readlines()
    text=text[1:]
    for i in range(len(text)):
        text[i]=text[i].split()
    return text

def template_mcfdinp_read(dire,dirname):
    try:
        file=open(dire+'\\'+dirname+'\\mcfd.inp','r')
    except FileNotFoundError:
        print('mcfd.inp template file not Found!')
        exit()
    text=file.readlines()
    file.close()
    for i in text:
        if i[0:7]=='seq.# 2':
            index=text.index(i)
    stringPart1=(text[:index+1])
    stringPart2=(text[index+2:])
    return stringPart1,stringPart2

def template_job1cfd_read(dire,dirname):
    try:
        file=open(dire+'\\'+dirname+'\\job1.cfd','r')
    except FileNotFoundError:
        print('job1.cfd template file not Found!')
        exit()
    text=file.readlines()
    file.close()
    stringPart1=(text[:1])
    stringPart2=(text[3:])
    return stringPart1,stringPart2

def template_infout_read (dire,dirname):
    try:
        file=open(dire+'\\'+dirname+'\\infout.inp','r')
    except FileNotFoundError:
        print('infout.inp template file not Found!')
        exit()
    text=file.readlines()
    file.close()
    stringPart1=(text[:-5])
    stringPart2=(text[-6:])
    return stringPart1,stringPart2

def write_mcfd_inp_func  (Part1,Part2,states):
    file=open('mcfd.inp','w')
    filewriteParts(file,Part1)
    file.write('values ')
    for j in states:
        file.write(j+' ')
    file.write('\n')
    filewriteParts(file,Part2)
    file.close()
    print('mcfd.inp ',end='')

def wirte_job1_cfd_func  (Part1,Part2,name):
    file=open('job1.cfd','w')
    filewriteParts(file,Part1)
    file.write('#PBS -N '+name+'\n')
    filewriteParts(file,Part2)
    file.close()
    print('job1.cfd ',end='')

def wirte_infout_inp_func(Part1,Part2,AOA):
    file=open('infout.inp','w')
    filewriteParts(file,Part1 )
    file.write('AOA ')
    file.write(AOA+'\n')
    filewriteParts(file,Part2 )
    file.close()
    print('infout.inp ',end='')

def wirte_tecout_inp_func():
    file=open('tecout.inp','w')
    file.write('1\n1\n')
    file.close()
    print('tecout.inp ',end='')  

main()

#与states.txt文件配合使用
#可以自动读入文件夹名称以及来流数据
#可以将第一个文件夹下的mcfd.inp、job1.cfd、infout.inp文件进行复制
#然后在剩余文件夹下进行粘贴，并修改其中的某些数据
#修改的数据对应关系如下：
#mcfd.inp:      读取states.txt文件中的来流参数，修改对应温度压力以及三向速度
#job1.cfd:      读取将job的名称设置为与文件夹名称相同
#infout.inp:    读取states.txt文件夹中最后一列的攻角
#注意，其余任何未提到的数据都不会进行修改