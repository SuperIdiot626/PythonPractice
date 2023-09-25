#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小写X



var1=tk.StringVar()                             #声明了一个可用于显示的变量



l = tk.Label(window,
                bg='green',                     #背景色绿色
                fg='yellow',                    #字体色黄色
                font=('Arial',12),
                width=10,
                textvariable=var1)
l.pack()
def print_selection():
    value=lb.get(lb.curselection())             #读取选择的数据
    var1.set(value)                             #将var1设置为读取到的数据
b1=tk.Button(window,                            #定义了一个按钮，按钮返回的函数不能有输入
                text='print selection',
                width=15,
                height=2,
                command=print_selection)
b1.pack()


var2=tk.StringVar()                             #声明另一个可用于显示的变量
var2.set([1,2,3,4])                             #将var2的值设为一个元组，列表也可以

lb=tk.Listbox(window,listvariable=var2)         #创建了一个选择列表，并将var2的值赋给可选择对象
list_items=[11,22,33,44]

for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')                            #在第一的位置插入first
lb.insert(2,'second')                           #在第2的位置插入second
lb.delete(2)                                    #删除了第二个位置上的数据
lb.pack()



window.mainloop()                       #使窗口循环，以执行命令