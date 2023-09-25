import time
import tkinter as tk
from tkinter.ttk import *

def timeFormat(secondTime):
    hour=str(int(secondTime/3600)).rjust(2,'0')
    minute=str(int(secondTime/60)).rjust(2,'0')
    second=str(int(secondTime%60)).rjust(2,'0')
    HMS=(hour+':'+minute+':'+second)
    return HMS

def show():
    global SampleDone
    for i in range(SampleNum-1):
        # 每次更新加1
        progressbarOne['value'] = SampleDone+ 1
        SampleDone+=1
        TimeNow=time.time()
        TimeUsed=TimeNow-TimeStarted
        TimeLeft=TimeUsed/SampleDone*(SampleNum-SampleDone)

        TimeUsed=timeFormat(TimeUsed)
        TimeLeft=timeFormat(TimeLeft)

        Progress.set('进度'+str(SampleDone)+'/'+str(SampleNum))
        Var_TimeUsed.set('已用时间：'+TimeUsed)
        Var_TimeLeft.set('剩余时间：'+TimeLeft)

        
        # 更新画面
        root.update()
        time.sleep(0.000001)

def terminate():
    exit()

def pause():
    exit()


root = tk.Tk()
root.title('计算中')
root.geometry('300x200')





Progress        =tk.IntVar()
Var_TimeUsed    =tk.IntVar()
Var_TimeLeft    =tk.IntVar()

SampleNum=1024
SampleDone=0
TimeStarted=time.time()



#Progress.set(str(SampleDone)+'/'+str(SampleNum))


progressbarOne = Progressbar(root)


progressbarOne['maximum'] = SampleNum
progressbarOne['value'] = 0





labelSambleNum=tk.Label(root,                              #indicate how to use this program
                textvariable=Progress,
                font=('Arial', 15),
                width=20,
                height=2,
                anchor='e')

labelTimeUsed=tk.Label(root,                              #indicate how to use this program
                textvariable=Var_TimeUsed,
                font=('Arial', 15),
                width=50,
                height=2,
                anchor='e')
labelTimeLeft=tk.Label(root,                              #indicate how to use this program
                textvariable=Var_TimeLeft,
                font=('Arial', 15),
                width=50,
                height=2,
                anchor='e')

button_Start    = tk.Button(root,
                text='开始',
                command=show)
button_Pause    = tk.Button(root,
                text='暂停',
                command=pause)
button_Terminate= tk.Button(root,
                text='终止',
                command=terminate)




progressbarOne  .place(width=260,height=25,x=20,y=20)

labelSambleNum  .place(width=200,height=20,x=-60,y=60)

labelTimeUsed   .place(width=200,height=30,x=20,y=90)
labelTimeLeft   .place(width=200,height=30,x=20,y=120)

button_Pause    .place(width=60,height=30,x=40,y=150)
button_Start    .place(width=60,height=30,x=120,y=150)
button_Terminate.place(width=60,height=30,x=200,y=150)




root.mainloop()