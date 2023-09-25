#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

nodes=[16,17,23,24,100,2000,300000]
node_num=len(nodes)
num=1

def traversedir(ini_dir):
    global num
    os.chdir(ini_dir)
    secondary_dir=os.listdir(ini_dir)
    secondary_dir.sort()
    for i in secondary_dir:
        whole_dir=os.path.join(ini_dir,i)
        if os.path.isdir(whole_dir):
            os.chdir(whole_dir)
            write_infout1f()
            write_mcfd()
            write_npfopts()
            write_pltopts()
            write_job1(num)
            print('file created in  ' + str(whole_dir))
            print('index is  '+str(num)+'  the node num is  ' + str(nodes[(num-1)%node_num])+'\n')
            num = num + 1



def write_infout1f():
    infoutlf=r'''asdasdasdasdasdasdas'''
    file=open('infout1f.inp','w')
    file.write(infoutlf)
    file.close()

def write_mcfd():
    mcfd=r'''asdasdasdasdasdasdas'''
    file=open('mcfd.inp','w')
    file.write(mcfd)
    file.close()

def write_npfopts():
    npfopts=r'''asdasdasdasdasdasdas'''
    file=open('npfopts.inp','w')
    file.write(npfopts)
    file.close()

def write_pltopts():
    pltopts=r'''asdasdasdasdasdasdas'''
    file=open('pltopts.inp','w')
    file.write(pltopts)
    file.close()

def write_job1(num):

    stringPart1=r'''1111111111111111111'''
    stringPart2=r'''22222222222222222222222222222'''
    ChangedP1='asdasdasdasd+         '
    ChangedP2='fghfghfghfghfgh       '
    file=open('job1.cfd','w')
    file.write(stringPart1)
    file.write(ChangedP1+str(num)+'\n')
    file.write(ChangedP2+str(nodes[(num-1)%node_num])+'asdasdasd\n')
    file.write(stringPart2)
    file.close()

target_dir=input('please enter your target dir:')
traversedir(target_dir)
a=input('all done enjoy!')