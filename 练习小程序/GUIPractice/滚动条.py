#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  
from tkinter.ttk import *
import time
window = tk.Tk()

window.title('ssss')

window.geometry('200x300')

pro=Progressbar(window,mode='indeterminate',value=0,max=100,length=200)
pro.pack(pady=10)
Button(window,text='start',command=pro.start(40),width=7).pack()

window.mainloop()