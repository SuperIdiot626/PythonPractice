#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  
import time
from threading import Thread
window = tk.Tk()

window.title('My Window')
window.geometry('500x300')  # 这里的乘是小写X


test_vari   =tk.IntVar()
test_vari.set('asdasd')
def run_in_thread(fun):
    def wrapper(*args, **kwargs):
        print('1')
        thread = Thread(target=fun, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

@run_in_thread
def looptest():
    
    for i in range(50):
        #print(i)
        t.insert('end', str(i))
        test_vari.set(str(i))
        time.sleep(0.05)

b1 = tk.Button(window, text='loop test', width=10,
               height=2, command=looptest)
b1.pack()


label_test   = tk.Label(window,                              #declare an input box
                textvariable=test_vari,
                font=('Arial', 14),
                width=20,
                height=2,
                anchor='c')
label_test.pack()

 
# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3,width=50)
t.pack()

window.mainloop()                       #使窗口循环，以执行命令