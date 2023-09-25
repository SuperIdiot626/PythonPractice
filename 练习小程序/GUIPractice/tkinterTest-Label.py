#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()            #简历window

window.title('wtf!!!')      #给窗口取名

window.geometry('300x300')  #设置窗口尺寸，中间乘号为小写x

l = tk.Label(window,        #在该对象上进行绘制
                text='say hi to the One',
                bg='green',
                font=('Arial',12),
                width=30,
                height=2)

l.pack()

windows = tk.Tk()            #简历window

windows.title('wtf!!!')      #给窗口取名

windows.geometry('200x200')  #设置窗口尺寸，中间乘号为小写x

ls = tk.Label(windows,        #在该对象上进行绘制
                text='say hi to the Two',
                bg='blue',
                font=('Arial',15),
                width=20,
                height=5)

ls.pack()
window.mainloop()
windows.mainloop()