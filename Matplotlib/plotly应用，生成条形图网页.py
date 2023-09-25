#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
from plotly.graph_objs import Bar,Layout
from plotly import offline


class Die:
    def __init__(self,number_sides=6):
        self.number_sides=number_sides

    def roll(self):
        return randint(1,self.number_sides)

die_01=Die(6)
die_02=Die(6)



results=[]                                      #记录结果
for roll_num in range(120000):                  #扔色子次数
    result=die_01.roll()+die_02.roll()
    results.append(result)


frequencies=[]
max_result=die_01.number_sides+die_02.number_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

x_values=list(range(2,max_result+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={'title':'结果','dtick':1}        #dtcik设置x轴显示间隔
y_axis_config={'title':'结果的频率'}

my_layout = Layout(title='掷一个D6 1200次的结果',
    xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='D6_D6.html')