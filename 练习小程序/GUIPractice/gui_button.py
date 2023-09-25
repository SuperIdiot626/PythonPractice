#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小写X

var = tk.StringVar() 
l = tk.Label (window, 
                textvariable=var,       #此处设置了文本变量，如此设置才可以进行修改
                bg='green',             #背景颜色，可不设置
                font=('Arial', 12),     #文本框的字体与大小
                width=30,               #文本框的宽度，单位为字符
                height=3)               #文本框的高度，单位为字符
l.pack()                                # Label内容content区域放置位置，自动调节尺寸


on_hit= False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, 
                text="hit me",          #按钮所显示的文本，如果使用text与变量，就会出现乱码，反之则显示为空
                #bg='green', 
                font=('Arial', 12), 
                width=10, 
                height=2, 
                command=hit_me)         #按下按钮式调用的函数

b.pack()

window.mainloop()                       #使窗口循环，以执行命令