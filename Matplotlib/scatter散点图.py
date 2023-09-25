#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib                   #用于防止中文出现乱码
font = {
    'family':'SimHei',
    'weight':'bold',
    'size':12
}
matplotlib.rc("font", **font)

import matplotlib.pyplot as plt     #缩写为plt，国际惯例

x_values=[1,2,3,4,5]            #坐标横轴
y_values=[1,4,9,16,25]               #数据来源

u=range(0,1000)
v=[i*i for i in u]

plt.style.use("bmh")

fig,ax=plt.subplots()                           #???

#ax.scatter(2,4)                                    #绘制单个散点
#ax.plot(x_values,y_values,linewidth=3)             #绘制折线，指定横、纵坐标值来源和曲线线宽
#ax.scatter(x_values,y_values,s=500)                #绘制多个散点，并指定点的大小
#ax.scatter(u,v,s=5,c='white')                      #绘制多个散点，并指定点的大小和点的颜色，点的颜色由元组构成，0~1对应RGB0~255
ax.scatter(u,v,s=5,c=v,cmap=plt.cm.jet)  


ax.axis([0,1100,0,1100000])                         #设置两个坐标轴的取值范围     


ax.set_title("平方数",fontsize=24)  #设置图表总标题
ax.set_xlabel("值",fontsize=14)     #设置坐标轴标题
ax.set_ylabel("值^2")

ax.tick_params(axis='both',which='major',labelsize=14)    #设置刻度标记大小


#plt.savefig('examples.jpg',bbox_inches='tight')         #保存图片，第一个参数为保存的名字，第二个是是否切除图片多余的空白区域，可以不要
plt.show()                          #结尾用于显示界面的程序