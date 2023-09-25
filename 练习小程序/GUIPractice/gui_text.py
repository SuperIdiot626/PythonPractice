#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小写X


e1 = tk.Entry(window, 
                show=None,               # 显示成密文形式，以*代替，此项可随意更改，但起作用的只有一个字符，可以中文
                font=('Arial', 14))

def insert_point(): # 在鼠标焦点处插入输入内容
    var = e1.get()                              #可以读取e1中输入的文字
    t.insert('insert', var)
def insert_end():   # 在文本框内容最后接着插入输入内容
    var = e1.get()
    print(type(var))
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()
 
# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3)
t.pack()


e1.pack()


window.mainloop()                       #使窗口循环，以执行命令