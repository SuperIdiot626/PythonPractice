#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先导入
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
l=tk.Label(window,width=20,text='empty')
l.pack()

def print_selection():
    v1=var1.get()
    v2=var2.get()
    v3=var3.get()
    if v1+v2+v3==0:
        l.config(text='zero')
    elif v1+v2+v3==1:
        l.config(text='one')
    elif v1+v2+v3==2:
        l.config(text='two')
    elif v1+v2+v3==3:
        l.config(text='three')
    # if var1+var1+var3==0:
    #     l.config(text='zero')
    # elif var1+var1+var3==1:
    #     l.config(text='one')
    # elif var1+var1+var3==2:
    #     l.config(text='two')
    # elif var1+var1+var3==3:
    #     l.config(text='three')

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

# var1=0
# var2=0
# var3=0

c1 = tk.Checkbutton(window, text='Python',  variable=var1, onvalue=1, offvalue=0, command=print_selection)    # 传值原理类似于radiobutton部件
c2 = tk.Checkbutton(window, text='C++',     variable=var2, onvalue=1, offvalue=0, command=print_selection)
c3 = tk.Checkbutton(window, text='java',    variable=var3, onvalue=1, offvalue=0, command=print_selection)

c1.pack()
c2.pack()
c3.pack()

window.mainloop()