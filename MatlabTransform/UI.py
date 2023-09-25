#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.filedialog import *
from threading          import Thread
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
import os,time
#from typing_extensions import IntVar 



timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())



show_avera=0                                            #set whether calculate the average value
avera_steps=500                                         #how many steps to cal the average

show_gap=0                                              #set whether show a gap step
gap_steps=1000                                          #set the value of gap

pri_dir=0
pri_steps=0                                             #steps, this should usually be 1
pri_time=0                                              #time
pri_Fx=0                                                #force at X direction
pri_Fy=0                                                #force at Y direction
pri_Fz=0                                                #force at Z direction
pri_Mx=0                                                #momentum object to axis X
pri_My=0                                                #momentum object to axis Y
pri_Mz=0                                                #momentum object to axis Z
pri_LiftCoe=0                                           #lift coefficient
pri_DragCoe=0                                           #drag coefficient
pri_LD_ratio=0                                          #Lift/Drag ratio

num_collected=0                                         #count how many files were collected
num_Nonstandard=0                                       #count how many non_standard files were detected
window = tk.Tk()

var_pri_avera   =tk.IntVar()
var_pri_gap     =tk.IntVar()
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
dir_input       =tk.StringVar()
dir_output      =tk.StringVar()



var_dir_input=os.getcwd()
var_dir_input=os.path.join(var_dir_input,'Input.txt')
dir_input.set(var_dir_input)                            #default dir is current dir

var_dir_output=os.getcwd()
dir_output.set(var_dir_output) 



window.title('工程估算')
window.geometry('900x850')


#添加菜单
menu1=tk.Menu(window)

menu1_2=tk.Menu(menu1,tearoff=False)
menu1  .add_cascade(label='文件',menu=menu1_2)
menu1_2.add_command(label='保存')
menu1_2.add_command(label='另存为')
menu1_2.add_command(label='导入')
menu1_2.add_command(label='退出')

menu2_2=tk.Menu(menu1,tearoff=False)
menu1  .add_cascade(label='设置',menu=menu2_2)
menu2_2.add_command(label='输出设置')
menu2_2.add_command(label='代理模型')
menu2_2.add_command(label='单位设置')
menu2_2.add_command(label='恢复默认设置')

menu3_2=tk.Menu(menu1,tearoff=False)
menu1  .add_cascade(label='帮助',menu=menu3_2)
menu3_2.add_command(label='说明文档')
menu3_2.add_command(label='反馈')

window.config(menu=menu1)







# tk.Label(window,text='来流条件:',font=('Arial', 14)).grid(row=0,column=0)
# val=tk.StringVar()






label_geometry  =tk.Label(window,
                text='    几何条件:',
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

label_dotsx= tk.Label(window,                              #indicate how to use this program
                text='纵向离散数:',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')
scale_dotx = tk.Scale(window,
                from_=50,
                to=500,
                orient=tk.HORIZONTAL,
                command=None)
label_lenx = tk.Label(window,                              #indicate how to use this program
                text='纵向长度:',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')

label_dotsy= tk.Label(window,                              #indicate how to use this program
                text='横向离散数:',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')
scale_doty = tk.Scale(window,
                from_=50,
                to=1000,
                orient=tk.HORIZONTAL,
                command=None)
label_leny = tk.Label(window,                              #indicate how to use this program
                text='横向长度:',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')

label_ConeN= tk.Label(window,                              #indicate how to use this program
                text='锥数(1~5):',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')


label_inflow     =tk.Label(window,
                text='    来流条件:',
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

label_in_mod=tk.Label(window,                              #indicate how to use this program
                text='输入模式',
                font=('Arial', 14),
                width=12,
                height=2,
                anchor='e')

combobox1    =Combobox(window,
                textvariable='',
                font=('Arial', 10),
                width=15,
                height=2)
combobox1["values"]=("三速度分量","速度攻角偏航角")      #下拉列表
combobox1.current(0)                                       #设置默认值


label_P    = tk.Label(window,                              #indicate how to use this program
                text='P(Pa):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_T    = tk.Label(window,                              #indicate how to use this program
                text='T(K):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_rho  = tk.Label(window,                              #indicate how to use this program
                text='rho(kg/m^3):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')

label_V    = tk.Label(window,                              #indicate how to use this program
                text='V(m/s):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_alpha= tk.Label(window,                              #indicate how to use this program
                text='alpha(°):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_beta = tk.Label(window,                              #indicate how to use this program
                text=' beta(°):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')

label_Vx   = tk.Label(window,                              #indicate how to use this program
                text='Vx(m/s):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_Vy   = tk.Label(window,                              #indicate how to use this program
                text='Vy(m/s):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_Vz   = tk.Label(window,                              #indicate how to use this program
                text='Vz(m/s):',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')


label_file =tk.Label(window,
                text='  输入输出路径:',
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

label_input= tk.Label(window,                              #indicate how to use this program
                text='读取输入参数',
                font=('Arial', 15),
                width=20,
                height=2,
                anchor='e')

label_CDin = tk.Button(window,
                        text='读取输入文件',
                        width=15,
                        height=1,
                        font=('Arial', 12),
                        command=None)

label_dirIn   = tk.Label(window,                              #declare an input box
                        textvariable=dir_input,
                        font=('Arial', 15),
                        width=30,
                        height=2,
                        anchor='center')


label_output= tk.Label(window,                              #indicate how to use this program
                text='计算输出路径',
                font=('Arial', 15),
                width=20,
                height=2,
                anchor='e')

button_CDout= tk.Button(window,
                        text='切换输出路径',
                        width=15,
                        height=1,
                        font=('Arial', 12),
                        command=None)

label_dirOut   = tk.Label(window,                              #declare an input box
                        textvariable=dir_output,
                        font=('Arial', 15),
                        width=30,
                        height=2,
                        anchor='center')





button_Calcu= tk.Button(window,
                        text='计算',
                        width=15,
                        height=1,
                        font=('Arial', 18),
                        command=None,
                        anchor='ce')

button_Analys= tk.Button(window,
                        text='分析',
                        width=15,
                        height=1,
                        font=('Arial', 18),
                        command=None,
                        anchor='ce')


entry_dotsx = tk.Entry(window,font=('Arial', 14),width=10)
entry_dotsy = tk.Entry(window,font=('Arial', 14),width=10)
entry_lenx  = tk.Entry(window,font=('Arial', 14),width=10)
entry_leny  = tk.Entry(window,font=('Arial', 14),width=10)
entry_ConeN = tk.Entry(window,font=('Arial', 14),width=10)

entry_P     = tk.Entry(window,font=('Arial', 10),width=10)
entry_T     = tk.Entry(window,font=('Arial', 10),width=10)
entry_rho   = tk.Entry(window,font=('Arial', 10),width=10)

entry_V     = tk.Entry(window,font=('Arial', 10),width=10)
entry_alpha = tk.Entry(window,font=('Arial', 10),width=10)
entry_beta  = tk.Entry(window,font=('Arial', 10),width=10)

entry_Vx    = tk.Entry(window,font=('Arial', 10),width=10)
entry_Vy    = tk.Entry(window,font=('Arial', 10),width=10)
entry_Vz    = tk.Entry(window,font=('Arial', 10),width=10)

label_geometry  .grid(row=1,column=0,columnspan=1)
label_dotsx     .grid(row=2,column=0,columnspan=1)
scale_dotx      .grid(row=2,column=1,columnspan=1)
entry_dotsx     .grid(row=2,column=2,columnspan=1)
label_lenx      .grid(row=2,column=3,columnspan=1)
entry_lenx      .grid(row=2,column=4,columnspan=1)

label_dotsy     .grid(row=3,column=0,columnspan=1)
scale_doty      .grid(row=3,column=1,columnspan=1)
entry_dotsy     .grid(row=3,column=2,columnspan=1)
label_leny      .grid(row=3,column=3,columnspan=1)
entry_leny      .grid(row=3,column=4,columnspan=1)


label_ConeN     .grid(row=4,column=0)
entry_ConeN     .grid(row=4,column=1)




label_inflow.grid(row=5,column=0,columnspan=2,sticky='EW')
label_in_mod.grid(row=6,column=0)
combobox1   .grid(row=6,column=1)

label_P     .grid(row=7,column=0)
entry_P     .grid(row=7,column=1)

label_T     .grid(row=7,column=2)
entry_T     .grid(row=7,column=3)

label_rho   .grid(row=7,column=4)
entry_rho   .grid(row=7,column=5)

label_V     .grid(row=8,column=0)
entry_V     .grid(row=8,column=1)

label_alpha .grid(row=8,column=2)
entry_alpha .grid(row=8,column=3)

label_beta  .grid(row=8,column=4)
entry_beta  .grid(row=8,column=5)

label_Vx    .grid(row=9,column=0)
entry_Vx    .grid(row=9,column=1)

label_Vy    .grid(row=9,column=2)
entry_Vy    .grid(row=9,column=3)

label_Vz    .grid(row=9,column=4)
entry_Vz    .grid(row=9,column=5)




label_file  .grid(row=11,column=0)
label_input .grid(row=12,column=0)
label_dirIn .grid(row=13,column=0,columnspan=2)
label_CDin  .grid(row=13,column=3)

label_output .grid(row=14,column=0)
label_dirOut .grid(row=15,column=0,columnspan=2)
button_CDout .grid(row=15,column=3)


button_Calcu .grid(row=17,column=0,columnspan=2)
button_Analys.grid(row=18,column=0,columnspan=2)


window.mainloop()                       #使窗口循环，以执行命令