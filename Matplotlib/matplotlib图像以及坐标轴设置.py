#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt     #缩写为plt，国际惯例
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


input_values=[1,2,3,4,5]            #坐标横轴
squares=[1,4,9,16,25]               #数据来源
squares01=range(1,6)

plt.style.use("bmh")

fig,ax=plt.subplots()                           #???
ax.plot(input_values,squares,linewidth=3)           #绘制第一条曲线，设定横坐标、纵坐标和曲线线宽
ax.plot(input_values,squares01)                  #绘制第二条曲线

ax.set_title("平方数",fontsize=24)      #设置图表总标题
ax.set_xlabel("值",fontsize=14)         #设置坐标轴标题
ax.set_ylabel("值^2")

ax.tick_params(axis='both',labelsize=14)    #设置刻度标记大小

plt.show()                          #结尾用于显示界面的程序