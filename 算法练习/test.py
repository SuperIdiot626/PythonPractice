#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.filedialog import *
from threading          import Thread
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
import os,time
#from typing_extensions import IntVar 


targetfilename='minfo1_e1'                              #for different target file
timenow=time.strftime((" %Y-%m-%d %H.%M.%S"),time.localtime())
filename='data_statistic'+timenow+'.txt'


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

dir_state       =tk.StringVar()
dir_current     =tk.StringVar()
dir_state.set('    Please click the button below to change dir : ')
rootDir=os.getcwd()
dir_current.set(rootDir)                            #default dir is current dir



window.title('Data Collector')
window.geometry('1100x510')


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





label_inflow     =tk.Label(window,
                text='来流条件:',
                font=('Arial', 14),
                width=12,
                height=2,
                anchor='e')

combobox1    =Combobox(window,
                textvariable='',
                font=('Arial', 14),
                width=12,
                height=2)
combobox1["values"]=("三速度分量","速度，攻角，偏航角")       #下拉列表
combobox1.current(0)                                        #设置默认值






label_dotsx= tk.Label(window,                              #indicate how to use this program
                text='纵向离散数:',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')

label_dotsy= tk.Label(window,                              #indicate how to use this program
                text='纵向离散数:',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')

label_in_mod=tk.Label(window,                              #indicate how to use this program
                text='输入模式',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')

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

label_alpha= tk.Label(window,                              #indicate how to use this program
                text='alpha:',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')
label_beta = tk.Label(window,                              #indicate how to use this program
                text=' beta:',
                font=('Arial', 12),
                width=12,
                height=2,
                anchor='e')








entry_dotsx = tk.Entry(window,font=('Arial', 14),width=10)
entry_dotsy = tk.Entry(window,font=('Arial', 14),width=10)

entry_P     = tk.Entry(window,font=('Arial', 14),width=10)
entry_T     = tk.Entry(window,font=('Arial', 14),width=10)
entry_rho   = tk.Entry(window,font=('Arial', 14),width=10)

entry_V     = tk.Entry(window,font=('Arial', 14),width=10)
entry_alpha = tk.Entry(window,font=('Arial', 14),width=10)
entry_beta  = tk.Entry(window,font=('Arial', 14),width=10)

entry_Vx    = tk.Entry(window,font=('Arial', 14),width=10)
entry_Vy    = tk.Entry(window,font=('Arial', 14),width=10)
entry_Vz    = tk.Entry(window,font=('Arial', 14),width=10)






label_dotsx .grid(row=1,column=0,columnspan=1,sticky='W')
entry_dotsx .grid(row=1,column=3,columnspan=1,sticky='W')

label_dotsy .grid(row=2,column=0,columnspan=1,sticky='W')
entry_dotsy .grid(row=2,column=3,columnspan=1,sticky='W')

label_inflow.grid(row=4,column=0,columnspan=2,sticky='W')

label_in_mod.grid(row=5,column=0)
combobox1   .grid(row=5,column=1)



label_P     .grid(row=6,column=0)
entry_P     .grid(row=6,column=1)

label_T     .grid(row=6,column=2)
entry_T     .grid(row=6,column=3)

label_rho   .grid(row=6,column=4)
entry_rho   .grid(row=6,column=5)

label_V     .grid(row=7,column=0)
entry_V     .grid(row=7,column=1)

label_alpha .grid(row=7,column=2)
entry_alpha .grid(row=7,column=3)

label_beta  .grid(row=7,column=4)
entry_beta  .grid(row=7,column=5)

label_Vx    .grid(row=8,column=0)
entry_Vx    .grid(row=8,column=1)

label_Vy    .grid(row=8,column=2)
entry_Vy    .grid(row=8,column=3)

label_Vz    .grid(row=8,column=4)
entry_Vz    .grid(row=8,column=5)


window.mainloop()                       #使窗口循环，以执行命令
