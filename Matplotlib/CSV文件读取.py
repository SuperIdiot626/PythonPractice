#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
from datetime import datetime                           #自带时间日期处理库


plt.rcParams['font.sans-serif'] = ['KaiTi']             #指定默认字体
plt.rcParams['axes.unicode_minus'] = False              #解决保存图像是负号'-'显示为方块的问题


filename='death_valley_2018_simple.csv'

with open(filename) as f:
    reader=csv.reader(f)                                #返回一个了与文件相关的阅读器对象
    header_row=next(reader)                             #第一次进行next返回文件第一行
    for index,data in enumerate(header_row):
        print(index,data)

    dates,highs,lows=[],[],[]
    for row in reader:
        date=datetime.strptime(row[2],'%Y-%m-%d')       #时间数据的特殊处理方式，输入
        try:                                            #处理了没有数据的错误情况
            high=int(row[4])
            low=int(row[5])
        except ValueError:
            print(date.strftime(
                    'Missing data for %Y-%m-%d'))       #时间数据的特殊处理方式，输出
            continue
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)



#plt.style.use('seaborn')                               #该样式无法显示中文
fig,ax=plt.subplots()
ax.plot(dates,highs,c=(0.5,0,0),linewidth=1,alpha=0.5)  #绘制曲线
ax.plot(dates,lows,c=(0,0,0.5),linewidth=1)             #
ax.fill_between(dates,lows,highs,
    facecolor=(0,0.5,0),alpha=0.5)                      #在两个值之间涂色,alpha值代表透明度，1不透明，0透明，可在多个语句中使用
ax.set_title("temperature of 2018",fontsize=24)         #设置图表总标题
ax.set_xlabel("Date",fontsize=14)                       #设置坐标轴标题
ax.set_ylabel("temperature",fontsize=14)                #设置纵轴标题
fig.autofmt_xdate()                                     #用来绘制倾斜的标签
ax.tick_params(axis='both',which='major',labelsize=10)  #设置刻度标记大小
plt.show()