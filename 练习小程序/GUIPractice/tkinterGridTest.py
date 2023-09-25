#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name            #初始化


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("马赫数计算_v0.01")                            #窗口名
        #self.init_window_name.geometry('320x160+10+10')                            #290x160为窗口大小，此项会受系统放大倍率影响，中间为小写x，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('500x500+100+100')
        #self.init_window_name["bg"] = "pink"                                        #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",1)                             #透明度，值越小透明程度越高
        
        
        #标签
        self.init_data_label = Label(self.init_window_name, text="请输入目标路径")
        self.init_data_label.grid(row=0, column=0)

        self.pbefore_label = Label(self.init_window_name, text="0,0")
        self.pbefore_label.grid(row=0, column=0, rowspan=2, columnspan=2)                                #row和column分别为第几行第几列
        self.pbefore_label = Text(self.init_window_name, width=20, height=1)    #波前压强录入框，width和height是输入框占几个字符的高度、宽度,录入框本身会自动居中显示
        self.pbefore_label.grid(row=1, column=1, rowspan=1, columnspan=1)
        
        self.pafter_label = Label(self.init_window_name, text="2,0")
        self.pafter_label.grid(row=2, column=0, rowspan=2, columnspan=2)
        self.pafter_label = Text(self.init_window_name, width=20, height=1)     #波后压强录入框
        self.pafter_label.grid(row=2, column=1, rowspan=1, columnspan=1)
        
        b = Button(self.init_window_name, text="hit me", command=DISABLED)
        



    #功能函数
    def calculate(self):
        src = self.pbefore_label.get(1.0,END).strip().replace("\n","").encode()
        print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()