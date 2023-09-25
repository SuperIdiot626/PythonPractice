#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter.filedialog import *
from threading          import Thread
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
import os,time
#from typing_extensions import IntVar 

def timeFormat(secondTime):
    hour=str(int(secondTime/3600)).rjust(2,'0')
    minute=str(int(secondTime/60)).rjust(2,'0')
    second=str(int(secondTime%60)).rjust(2,'0')
    HMS=(hour+':'+minute+':'+second)
    return HMS

def show():
    TimeStarted=TimeNow=time.time()
    progressbarOne.start()
    Var_ButtonText.set('分析中，请稍候...')
    for i in range(50000):
        TimeNow=time.time()
        TimeUsed=TimeNow-TimeStarted
        TimeUsed=timeFormat(TimeUsed)
        Var_TimeUsed.set('已用时间：'+TimeUsed)
        window.update()
    progressbarOne.stop()
    Var_ButtonText.set('分析完成')
    text_daili.insert('end', dailimoxingCA+'\n')
    text_daili.insert('end', dailimoxingCN+'\n')
    text_daili.insert('end', dailimoxingCm+'\n')
    text_daili.insert('end', dailimoxingCL+'\n')
    text_daili.insert('end', dailimoxingCD+'\n')
    text_Residual.insert('end', residuaCA+'\n')
    text_Residual.insert('end', residuaCN+'\n')
    text_Residual.insert('end', residuaCm+'\n')
    text_Residual.insert('end', residuaCL+'\n')
    text_Residual.insert('end', residuaCD+'\n')
    text_Residual.insert('end', residuaK+'\n')
    text_Residual.insert('end', residuaPpoin+'\n')


def quit():
    exit()

window = tk.Tk()

Var_TimeUsed        =tk.StringVar()
Var_ButtonText      =tk.StringVar()


Var_ButtonText.set('开始分析')

window.title('结果分析')
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



dailimoxingCA='CA=0.0829-0.0136*θlNl-0.00007667*NuNl+0.0197*θl+0.0016*Nu+0.0033*Nl'
dailimoxingCN='CN=0.1079-0.0017*θlNl-0.00095269*NuNl+0.00067366*θu+0.034*θl-0.0031*Nu+0.00003117*Nl+0.0037*n'
dailimoxingCm='Cm=0.3827-0.0092*θlNl-0.00031*NuNl+0.0012*θu+0.1140*θl-0.0085*Nu+0.000027010*Nl+0.0120*n'
dailimoxingCL='CL=0.4971-0.0397*θlNl-0.000069734*NuNl+0.0033*Nu*n+0.0130*Nun+0.0557*θl-0.00085264*Nu-0.0069Nl-0.0199*n'
dailimoxingCD='CD=0.1719-0.0208*θlNl+0.000048577*NuNl+0.0299*θl+0.0020*Nu+0.0042*Ni-0.0041*n'

residuaCA='对于CA，θl、Nu、Nl对其有显著影响，θu、n对其影响较小；θl、Nl交互作用明显，Nu、Nl交互作用明显'
residuaCN='对于CN，θu、θl、Nu、Nl、n对其有显著影响，无参数对其影响较小；θl、Nl交互作用明显，Nu、Nl交互作用明显'
residuaCm='对于Cm，θu、θl、Nu、Nl、n对其有显著影响，无参数对其影响较小；θl、Nl交互作用明显，Nu、Nl交互作用明显'
residuaCL='对于CL，θl、Nu、Nl、n对其有显著影响，θu对其影响较小；θl、Nl交互作用明显，Nu、Nl交互作用明显，Nu、n交互作用明显，Nl、n交互作用明显'
residuaCD='对于CD，θl、Nu、Nl、n对其有显著影响，θu对其影响较小；θl、Nu交互作用明显，Nu、Nl交互作用明显'

residuaK='对于K，θu、θl、Nu、Nl对其有显著影响，n对其影响较小；θl、Nl交互作用明显，Nu、Nl交互作用明显，Nu、n交互作用明显，Nl、n交互作用明显'
residuaPpoin='对于压心，θl、Nu、Nl对其有显著影响，θu，n对其影响较小；θu、Nu交互作用明显，Nu、Nl交互作用明显，Nl、n交互作用明显'


progressbarOne =Progressbar(window,
                length=200, 
                mode='indeterminate', 
                orient=tkinter.HORIZONTAL)

button = tk.Button(window,
                textvariable=Var_ButtonText,
                font=('Arial', 20),
                width=20,
                height=3,
                command=show)

label_TimeUsed  =tk.Label(window,
                textvariable=Var_TimeUsed,
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

label_dailiModel=tk.Label(window,
                text='代理模型结果:',
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

text_daili    = tk.Text(window,
                font=('Arial', 13),
                height=25,
                width=80)           #set the max rows of log and max width

label_ResidualModel=tk.Label(window,
                text='多因素方差分析:',
                font=('Arial', 20),
                width=12,
                height=2,
                anchor='w')

text_Residual    = tk.Text(window,
                font=('Arial', 13),
                height=25,
                width=80)

button_save     = tk.Button(window,
                text="保存",
                font=('Arial', 18),
                width=20,
                height=2,
                command=None)

button_exit     = tk.Button(window,
                text="退出",
                font=('Arial', 18),
                width=20,
                height=2,
                command=quit)
progressbarOne      .place(width=800,height=30,x=50,y=20)
button              .place(width=250,height=50,x=50,y=60)
label_TimeUsed      .place(width=250,height=25,x=50,y=150)
label_dailiModel    .place(width=800,height=30,x=50,y=200)
text_daili          .place(width=800,height=180,x=50,y=250)
label_ResidualModel .place(width=800,height=30,x=50,y=450)
text_Residual       .place(width=800,height=250,x=50,y=500)
button_save         .place(width=250,height=50,x=100,y=780)
button_exit         .place(width=250,height=50,x=550,y=780)

window.mainloop()                       #使窗口循环，以执行命令