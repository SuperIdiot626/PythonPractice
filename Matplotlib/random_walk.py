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

from random import choice

class RandmWalk:
    def __init__(self,num_points=5000):
        self.num_points=num_points

        self.x_value=[0]
        self.y_value=[0]

    def fill_walk(self):
        while len(self.x_value)<self.num_points:
            
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            if x_step==0 and y_step==0:
                continue
            
            x=self.x_value[-1]+x_step
            y=self.y_value[-1]+y_step

            self.x_value.append(x)
            self.y_value.append(y)



while True:
    rw=RandmWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(16,9),dpi=100)                                         #指定生成图标的尺寸，单位英寸，之后为每英寸的像素数量



    point_numbers=range(rw.num_points)
    #ax.scatter(rw.x_value,rw.y_value,c=point_numbers,
    #    cmap=plt.cm.Blues,s=5,edgecolors='none')                                        #edgecolors作用为设置点的边线颜色，none为无边线
    ax.plot(rw.x_value,rw.y_value,linewidth=1)
    ax.scatter(0,0,c='green',s=50,edgecolors='blue')                                    #着重绘制起点和终点
    ax.scatter(rw.x_value[-1],rw.y_value[-1],c='red',s=50,edgecolors='none') 
   
    ax.get_xaxis().set_visible(False)                                                   #设置坐标轴不可见
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running=input('Another walk?(y/n):')
    if keep_running=='n':
        break
