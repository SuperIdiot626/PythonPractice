import time
import tkinter as tk
from tkinter.ttk import *


def show():
    global SampleDone
    SampleDone=0
    for i in range(100):
        # 每次更新加1
        progressbarOne['value'] = i + 1
        SampleDone+=1
        TimeNow=time.time()
        TimeUsed=TimeNow-TimeStarted


        TimeLeft=TimeUsed/SampleDone*(SampleNum-SampleDone)
        TimeUsed=time.strftime("%H:%M:%S")
        TimeLeft=time.strftime("%H:%M:%S")
        Progress.set(str(SampleDone)+'/'+str(SampleNum))
        Var_TimeUsed.set(TimeUsed)
        Var_TimeLeft.set()

        
        # 更新画面
        root.update()
        time.sleep(1)
    exit()
root = tk.Tk()
root.geometry('200x150')





Progress        =tk.IntVar()
Var_TimeUsed    =tk.IntVar()
Var_TimeLeft    =tk.IntVar()

SampleNum=100
SampleDone=1
TimeStarted=time.time()



Progress.set(str(SampleDone)+'/'+str(SampleNum))


progressbarOne = tk.ttk.Progressbar(root)
progressbarOne.pack(pady=20)
# 进度值最大值
progressbarOne['maximum'] = 100
# 进度值初始值
progressbarOne['value'] = 0

button = tk.Button(root, text='Running', command=show)
button.pack(pady=5)


labelSambleNum=tk.Label(root,                              #indicate how to use this program
                textvariable=Progress,
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')
labelSambleNum.pack(pady=10,padx=10)

labelTimeUsed=tk.Label(root,                              #indicate how to use this program
                textvariable='1024',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')
labelTimeUsed.pack(pady=10,padx=10)
labelTimeLeft=tk.Label(root,                              #indicate how to use this program
                textvariable='1024',
                font=('Arial', 15),
                width=12,
                height=2,
                anchor='e')
labelTimeLeft.pack(pady=10,padx=10)


root.mainloop()