#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter.filedialog import *
    #from threading          import Thread
    from tkinter.ttk import *
    import tkinter as tk
    import tkinter.messagebox

except:
    GuiMod=False
else:
    GuiMod=True

#GuiMod=False

import os,time
#from typing_extensions import IntVar 


targetfilename='minfo1_e1'                              #for different target file
timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())
filename='data_statistic'+timenow+'.txt'

show_everything=0

show_avera=show_everything                             	#set whether calculate the ave_data value
avera_steps=5000                                        #how many steps to cal the ave_data

show_gap =show_everything                               #set whether show a gap step
gap_steps=5000                                          #set the value of gap

show_resi=show_everything

pri_dir=1
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

if GuiMod==True:
    window = tk.Tk()

    var_pri_avera   =tk.IntVar()
    var_pri_gap     =tk.IntVar()
    var_pri_resi    =tk.IntVar()
    var_pri_time    =tk.IntVar()
    var_pri_dir     =tk.IntVar()
    var_pri_steps   =tk.IntVar()
    var_pri_time    =tk.IntVar()
    var_pri_Fx      =tk.IntVar()
    var_pri_Fy      =tk.IntVar()
    var_pri_Fz      =tk.IntVar()
    var_pri_Mx      =tk.IntVar()
    var_pri_My      =tk.IntVar()
    var_pri_Mz      =tk.IntVar()
    var_pri_LiftCoe =tk.IntVar()
    var_pri_DragCoe =tk.IntVar()
    var_pri_LD_ratio=tk.IntVar()

    dir_state       =tk.StringVar()
    dir_current     =tk.StringVar()
    dir_state.set('    Please click the button below to change dir : ')
    rootDir=os.getcwd()
    dir_current.set(rootDir)                                #default dir is current dir




def dataWrite(resultfile,data,output_mode):
    if pri_steps==1:                                    #以下内容用于使输出更规范
        if output_mode==1:
            front_line=                           "       the  latest  step:"
            resultfile.write(front_line+str(int(data[0])).rjust(9,' '))
        if output_mode==2:
            front_line=str(int(avera_steps)).ljust(8,' ')+"  steps' average:"
            resultfile.write(front_line+str(int(data[0])).rjust(9,' '))
        if output_mode==4:
            front_line=str(int(gap_steps  )).ljust(8,' ')+"aver data's resi:"
            resultfile.write(front_line+str(int(data[0])).rjust(9,' '))
        
        if output_mode==3:
            front_line=str(int(gap_steps  )).ljust(8,' ')+"  steps'  before:"
            resultfile.write(front_line+str(int(data[0])).rjust(9,' '))
        if output_mode==5:
            front_line=str(int(gap_steps  )).ljust(8,' ')+" gap data's resi:"
            resultfile.write(front_line+str(int(data[0])).rjust(9,' '))
        
    if output_mode in [1,2,3]:
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
                resultfile.write('  L/D= %14.7e'%(data[8]/data[9]))
            except ZeroDivisionError:
                write_log('divided by zero in %s'%dir)
                resultfile.write('  divided by zero')
        resultfile.write('\n')
    if output_mode in [4,5]:
        if pri_time==1:
            resultfile.write(' %13.3f%%'%(data[1]*100))
        if pri_Fx==1:
            resultfile.write(' %13.3f%%'%(data[2]*100))
        if pri_Fy==1:
            resultfile.write(' %13.3f%%'%(data[3]*100))
        if pri_Fz==1:
            resultfile.write(' %13.3f%%'%(data[4]*100))
        if pri_Mx==1:
            resultfile.write(' %13.3f%%'%(data[5]*100))
        if pri_My==1:
            resultfile.write(' %13.3f%%'%(data[6]*100))
        if pri_Mz==1:
            resultfile.write(' %13.3f%%'%(data[7]*100))
        if pri_LiftCoe==1:
            resultfile.write(' %13.3f%%'%(data[8]*100))
        if pri_DragCoe==1:
            resultfile.write(' %13.3f%%'%(data[9]*100))
        if pri_LD_ratio==1:
            resultfile.write(' %13.3f%%'%(data[10]*100))
        resultfile.write('\n')

def datacollect(dir):                                       #function to collect data
    global num_collected
    global num_Nonstandard
    global avera_steps
    try:
        file=open(targetfilename,'r')                       #test if target file exists
    except:
        return 0
    print(dir)
    wholeTxt=file.readlines()                               #read all the file
    file.close                                              #close file after read

    if wholeTxt[0].split(' ')[1]=="coefficients":           #check if file is output by "coefficients" 
        wholeTxt.reverse()
        wholeTxt=wholeTxt[0:-12]                            #the first 12 rows are fixed

        final_row=wholeTxt[0].split(' ')                    #split the line with space and delete all of them                             
        while '\n' in final_row:                            #if calculation stoped manually it ends with data
            final_row.remove('')                            #if calculation stoped automaticly it ends with \n
        while '' in final_row:
            final_row.remove('')
        for j,data in enumerate(final_row):                 #add all the data
            final_row[j]=float(data)

        if show_gap:
            try:
                gap_data=wholeTxt[gap_steps]
            except IndexError:
                gap_data=wholeTxt[-1]
                write_log('gap number exceeds in %s'%dir)
            gap_data=(gap_data[:-1]).split(' ')             #split the line with space and delete all of them                        
            while '' in gap_data:                           
                gap_data.remove('')
            for i,data in enumerate(gap_data):              #str to float
                gap_data[i]=float(data)

            if show_resi:
                gap_resi=[0,0,0,0,0,0,0,0,0,0,0]
                for i,data in enumerate(final_row):
                    if i==0:
                        continue
                    try:
                        gap_resi[i]=abs((gap_data[i]-final_row[i])
                                         /(final_row[i])
                                        )
                    except ZeroDivisionError:
                        gap_resi[i]=0
                if gap_data[-1]==0:
                    gap_LD =0
                else:
                    gap_LD = gap_data[-2]/ gap_data[-1]
                if final_row[-1]==0:
                    data_LD =0
                else:
                    data_LD=final_row[-2]/final_row[-1]
                if (gap_LD ==0) and (data_LD ==0):
                    gap_resi[10]=0
                else:
                    gap_resi[10]=abs((gap_LD-data_LD)
                                      /(data_LD)
                                    )


        if show_avera:
            wholeTxt=wholeTxt[0:avera_steps]                #only need some last lines
            ave_data=[0,0,0,0,0,0,0,0,0,0]                  #initial value of ave_data
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
                wholeTxt[i]=line                            #set the data
            for i,data in enumerate(ave_data):              #calculate average data
                ave_data[i]=data/len(wholeTxt)

            if show_resi:                                   #calculate residual
                ave_resi=[0,0,0,0,0,0,0,0,0,0,0]            #longer than usual
                for i,data in enumerate(final_row):
                    if i==0:
                        continue
                    try:
                        ave_resi[i]=abs((ave_data[i]-final_row[i])
                                         /(final_row[i])
                                        )
                    except ZeroDivisionError:
                        ave_resi[i]=0
                if ave_data[-1]==0:                         #in case of divided by zero
                    ave_LD =0
                else:
                    ave_LD = ave_data[-2]/ ave_data[-1]
                if final_row[-1]==0:
                    data_LD =0
                else:
                    data_LD=final_row[-2]/final_row[-1]
                if (ave_LD ==0) and (data_LD ==0):
                    ave_resi[10]=0
                else:
                    ave_resi[10]=abs((ave_LD-data_LD)
                                      /(data_LD)
                                    )

        os.chdir(rootDir)
        statistical_result=open(filename,'a')               #open the statistic file and recorC:\Users\WYZ\Desktop\CaoPuyud
        if pri_dir==1:
            statistical_result.write(dir+'\n')

        dataWrite(    statistical_result, final_row ,1)
        if show_avera==1:
            dataWrite(statistical_result, ave_data  ,2)
        if show_resi==1:
            dataWrite(statistical_result, ave_resi  ,4)
        if show_gap==1:

            dataWrite(statistical_result, gap_data  ,3)
        if show_resi==1:
            dataWrite(statistical_result, gap_resi  ,5)
        statistical_result.close
        num_collected+=1
        if GuiMod==True:
            write_log("%s collected"%dir)                    #show which dirs were collected
    else:
        num_Nonstandard+=1
        if GuiMod==True:
            write_log('Non_standard file decteced in %s'%dir)

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

def print_selection():
    global show_avera
    global avera_steps
    global show_gap
    global gap_steps

    global pri_dir
    global pri_steps
    global pri_time
    global pri_Fx
    global pri_Fy
    global pri_Fz
    global pri_Mx
    global pri_My
    global pri_Mz
    global pri_LiftCoe
    global pri_DragCoe
    global pri_LD_ratio
    avera_steps =(ave_entry.get())
    gap_steps   =(gap_entry.get())
    if avera_steps!='':
        avera_steps =int(avera_steps)
    else:
        avera_steps=1
    if  gap_steps!='':
         gap_steps =int(gap_steps)
    else:
         gap_steps=0
    show_avera  =var_pri_avera.get()
    show_gap    =var_pri_gap.get()
    pri_dir     =var_pri_dir.get()
    pri_steps   =var_pri_steps.get()
    pri_time    =var_pri_time.get()  
    pri_Fx      =var_pri_Fx.get()
    pri_Fy      =var_pri_Fy.get()
    pri_Fz      =var_pri_Fz.get()
    pri_Mx      =var_pri_Mx.get()
    pri_My      =var_pri_My.get()
    pri_Mz      =var_pri_Mz.get()
    pri_LiftCoe =var_pri_LiftCoe.get()
    pri_DragCoe =var_pri_DragCoe.get()
    pri_LD_ratio=var_pri_LD_ratio.get()

def collect():                                              #collect the data when press the button
    global num_collected
    pro.start(40)
    print_selection()
    try:
        os.chdir(rootDir)
    except OSError:
        tkinter.messagebox.showerror(title='Error',          #if error, inject an tip window
            message='Invalid path!')
    else:
        traversedir(rootDir)                                #if success, inject an "all done" window
        x=str(num_collected) 
        tkinter.messagebox.showinfo(title='Message',
            message=x+' file(s) collected,please check root dir.')
        write_log('All done, '+str(num_collected)+' file(s) collected',1)
        num_collected=0
        pro.stop()

def clear():                                                #collect the data when press the button
    try:
        os.chdir(rootDir)
    except OSError:
        tkinter.messagebox.showerror(title='Error',         #if error, inject an tip window
            message='Invalid path!')
    else:
        confirm=(tkinter.messagebox.askyesno(title='Warning', 
            message='Delet existing Datafile?'))            #confirm current operation
        if confirm==True:                                   
            try:
                os.remove(filename) 
            except FileNotFoundError:                       #if file not Found, which means deleted
                tkinter.messagebox.showerror(title='Error!',
                    message='Delete Failed.')
            else:
                tkinter.messagebox.showinfo(title='Message',
                    message='Delete success.')
                write_log("File deleted",1)

def select_dir():
    global rootDir
    rootDir=askdirectory(title='Please select target directory')
    dir_state.set('    Please check your target dir : ')
    dir_current.set(rootDir)

def write_log(text,write_time=0):
    if GuiMod==True:
        if write_time==1:
            timetxt=time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())
            text_log.insert('end', timetxt)

        text_log.insert('end', text+'\n')
    else:
        print(text)


if __name__=='__main__':

    if GuiMod==True:
        window.title('Data Collector')
        window.geometry('1100x510')

        label_dir   = tk.Label(window,                              #declare an input box
                        textvariable=dir_current,
                        font=('Arial', 14),
                        width=45,
                        height=2,
                        anchor='c')

        label_log   = tk.Label(window,                              #declare an input box
                        text="Operation Log:",
                        font=('Arial', 12),
                        width=40,
                        height=1,
                        anchor='w')

        label_hint  = tk.Label(window,                              #indicate how to use this program
                        textvariable=dir_state,
                        font=('Arial', 12),
                        width=45,
                        height=2,
                        anchor='w')

        label_ave   = tk.Label(window,                              #indicate how to use this program
                        text='ave steps:',
                        font=('Arial', 12),
                        width=12,
                        height=2,
                        anchor='e')

        label_gap   = tk.Label(window,                              #indicate how to use this program
                        text='gap steps:',
                        font=('Arial', 12),
                        width=12,
                        height=2,
                        anchor='e')

        label_output= tk.Label(window,                              #indicate how to use this program
                        text='    Please select the data you want to output: ',
                        font=('Arial', 12),
                        width=45,
                        height=2,
                        anchor='w')

        button_start= tk.Button(window,
                        text='Start !',
                        width=10,
                        height=1,
                        font=('Arial', 12),
                        command=collect)

        button_clear= tk.Button(window,
                        text='Del file',
                        width=10,
                        height=1,
                        font=('Arial', 12),
                        command=clear)

        button_cd   = tk.Button(window,
                        text='Click to Change dir',
                        width=15,
                        height=1,
                        font=('Arial', 12),
                        command=select_dir)

        text_log    = tk.Text(window, height=30,width=80)           #set the max rows of log and max width

        ave_entry= tk.Entry(window,font=('Arial', 14),width=10)
        gap_entry= tk.Entry(window,font=('Arial', 14),width=10)
        ctrl_aver= tk.Checkbutton(window,text='ave step' ,variable=var_pri_avera,    onvalue=1, offvalue=0,)
        ctrl_gap = tk.Checkbutton(window,text='gap step',variable=var_pri_gap,      onvalue=1, offvalue=0,)
        ctrl_resi= tk.Checkbutton(window,text='residual',variable=var_pri_resi,     onvalue=1, offvalue=0,)
        ctrl_dir = tk.Checkbutton(window,text='dir     ',variable=var_pri_dir,      onvalue=1, offvalue=0,)
        ctrl_step= tk.Checkbutton(window,text='step   ' ,variable=var_pri_steps,    onvalue=1, offvalue=0,)
        ctrl_time= tk.Checkbutton(window,text='time'    ,variable=var_pri_time,     onvalue=1, offvalue=0,)
        ctrl_Fx  = tk.Checkbutton(window,text='Fx      ',variable=var_pri_Fx,       onvalue=1, offvalue=0,)
        ctrl_Fy  = tk.Checkbutton(window,text='Fy     ' ,variable=var_pri_Fy,       onvalue=1, offvalue=0,)
        ctrl_Fz  = tk.Checkbutton(window,text='Fz'      ,variable=var_pri_Fz,       onvalue=1, offvalue=0,)
        ctrl_Mx  = tk.Checkbutton(window,text='Mx     ' ,variable=var_pri_Mx,       onvalue=1, offvalue=0,)
        ctrl_My  = tk.Checkbutton(window,text='My     ' ,variable=var_pri_My,       onvalue=1, offvalue=0,)
        ctrl_Mz  = tk.Checkbutton(window,text='Mz'      ,variable=var_pri_Mz,       onvalue=1, offvalue=0,)
        ctrl_LC  = tk.Checkbutton(window,text='LiftCoe' ,variable=var_pri_LiftCoe,  onvalue=1, offvalue=0,)
        ctrl_DC  = tk.Checkbutton(window,text='DragCoe' ,variable=var_pri_DragCoe,  onvalue=1, offvalue=0,)
        ctrl_LDR = tk.Checkbutton(window,text='L-G Coe' ,variable=var_pri_LD_ratio, onvalue=1, offvalue=0,)

        pro=Progressbar(window,mode='indeterminate',value=0,max=100,length=500)

        label_hint  .grid(row=0,column=0,columnspan=3,sticky='W')
        label_dir   .grid(row=1,column=0,columnspan=3,sticky='W')
        button_cd   .grid(row=2,column=1,columnspan=2)
        label_output.grid(row=3,column=0,columnspan=3,sticky='W')

        ctrl_aver.grid(row=4,column=0,columnspan=1)
        label_ave.grid(row=4,column=1,columnspan=1,sticky='E')
        ave_entry.grid(row=4,column=2,columnspan=1,sticky='W')

        ctrl_gap .grid(row=5,column=0,columnspan=1)
        label_gap.grid(row=5,column=1,columnspan=1,sticky='E')
        gap_entry.grid(row=5,column=2,columnspan=1,sticky='W')

        ctrl_resi.grid(row=6,column=0,columnspan=1)

        ctrl_dir .grid(row=7,column=0,columnspan=1,sticky='E')
        ctrl_step.grid(row=7,column=1,columnspan=1)
        ctrl_time.grid(row=7,column=2,columnspan=1,sticky='W')

        ctrl_Fx  .grid(row=8,column=0,columnspan=1,sticky='E')
        ctrl_Fy  .grid(row=8,column=1,columnspan=1)
        ctrl_Fz  .grid(row=8,column=2,columnspan=1,sticky='W')

        ctrl_Mx  .grid(row=9,column=0,columnspan=1,sticky='E')
        ctrl_My  .grid(row=9,column=1,columnspan=1)
        ctrl_Mz  .grid(row=9,column=2,columnspan=1,sticky='W')

        ctrl_LC  .grid(row=10,column=0,columnspan=1,sticky='E')
        ctrl_DC  .grid(row=10,column=1,columnspan=1)
        ctrl_LDR .grid(row=10,column=2,columnspan=1,sticky='W')

        button_clear.grid(row=11,column=0,rowspan=2,columnspan=1,sticky='E')
        button_start.grid(row=11,column=2,rowspan=2,columnspan=1,sticky='W')

        #pro      .grid(row=0,column=4,rowspan=1,columnspan=1,sticky='W')
        label_log.grid(row=1,column=4,rowspan=1,columnspan=1,sticky='W')
        text_log .grid(row=2,column=4,rowspan=10,columnspan=1,sticky='W')

        ctrl_aver.select()                      #default sets
        ctrl_gap .select()
        ctrl_resi.select()

        ctrl_dir .select()
        ctrl_step.select()
        ctrl_time.select()

        ctrl_Fx  .select()
        ctrl_Fy  .select()
        ctrl_Fz  .select()

        ctrl_Mx  .select()
        ctrl_My  .select()
        ctrl_Mz  .select()

        ctrl_LC  .select()
        ctrl_DC  .select()
        ctrl_LDR .select()
        
        ave_entry.insert(0,'1000')
        gap_entry.insert(0,'1000')
        write_log('',1)

        window.mainloop()                       #使窗口循环，以执行命令
    else:
        rootDir=input("please enter target dir:")
        #rootDir="D:\Code\Python\练习小程序\数据" 
        traversedir(rootDir)
        print('%d file(s) were collected'%num_collected)
        print('%d non_standard file(s) detected'%num_Nonstandard)
        print('all done! please check file data_statistic.txt at origial dic')

#v1.01  通过文件夹选择菜单避免了路径无法复制粘贴的问题  2021年8月20日10:43:22
#v1.02  优化了界面视觉效果  2021年8月21日20:02:51
#v1.03  增加了操作历史，进一步优化了视觉效果，解决了一些bug 2021年8月23日18:39:30
#v1.04  防止末行不为空的bug，可以根据情况选择是否启用gui了
#v1.05  增加了残差输出，优化了输出格式

#添加残差检测功能   done
#添加运行时间功能
#问题：①log不能实时更新