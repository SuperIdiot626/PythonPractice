#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先导入
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 

var1 = tk.StringVar()  

var2 = tk.StringVar()  



l = tk.Label(window,
                #bg='green',                     #背景色绿色
                #fg='yellow',                    #字体色黄色
                font=('Arial',12),
                width=30,
                text='empty')
l.pack()

def print_selection():
    l.config(text='You have selected '+var1.get())

r1=tk.Radiobutton(window,
                    text='Option A1',
                    variable=var1,                  #用于区分单选按钮所在的组
                    value="A",
                    command=print_selection)
r2=tk.Radiobutton(window,
                    text='Option B1',
                    variable=var1,
                    value="B",
                    command=print_selection)

r3=tk.Radiobutton(window,
                    text='Option A2',
                    variable=var2,
                    value="C",
                    command=print_selection)

r4=tk.Radiobutton(window,
                    text='Option B2',
                    variable=var2,
                    value="D",
                    command=print_selection,)
r1.select()

r3.select()

r1.pack()
r2.pack()
r3.pack()
r4.pack()


window.mainloop()