#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from math import *
from pygame.locals import *

Width=1000
Hight=0.6*Width
Width=int(Width)
Hight=int(Hight)

pygame.init()
Surface=pygame.display.set_mode((Width,Hight))
pygame.display.set_caption('Function Imagine in CCS')
TitleFro=pygame.font.Font('freesansbold.ttf',20)

White=(255,255,255)
Red=(255,0,0)

Zero=TitleFro.render('0',1,White)
One=TitleFro.render('1',1,White)

UnitLen=50

def f(x):
    try:
        y=(9-(-1-x)**2)**0.5+(4-x**2)**0.5
    except ZeroDivisionError:
        return 'error'
    else:
        return y
    

def plotCCS():
    pygame.draw.line(Surface,White,(20,0.5*Hight),(Width-20,0.5*Hight),3)   #绘制横轴
    pygame.draw.line(Surface,White,(0.5*Width,20),(0.5*Width,Hight-20),3)   #绘制纵轴
    pygame.draw.line(Surface,White,(0.5*Width-UnitLen,0.5*Hight),(0.5*Width-UnitLen,0.5*Hight-8),3)
    pygame.draw.line(Surface,White,(0.5*Width+UnitLen,0.5*Hight),(0.5*Width+UnitLen,0.5*Hight-8),3)   #绘制横轴单位
    pygame.draw.line(Surface,White,(0.5*Width,0.5*Hight-UnitLen),(0.5*Width+8,0.5*Hight-UnitLen),3)
    pygame.draw.line(Surface,White,(0.5*Width,0.5*Hight+UnitLen),(0.5*Width+8,0.5*Hight+UnitLen),3)   #绘制纵轴单位
    pygame.draw.lines(Surface,White,0,[(Width-32,0.5*Hight-12),(Width-20,0.5*Hight),(Width-32,0.5*Hight+12)],4)   #绘制制横箭头 
    pygame.draw.lines(Surface,White,0,[(0.5*Width-12,32),(0.5*Width,20),(0.5*Width+12,32)],4)    #绘制纵轴箭头
    Surface.blit(Zero,(0.5*Width-15,0.5*Hight+5))           #标出原点
    Surface.blit(One,(0.5*Width-14,0.5*Hight-UnitLen-10))   #标出纵轴单位1
    Surface.blit(One,(0.5*Width+UnitLen-5,0.5*Hight+5))     #标出横轴单位1


def calcuDots():
    global dotLsit
    global bigList
    dotLsit=[]
    bigList=[]
    x_max=10
    x_min=-x_max
    x=x_min
    dotNum=1000
    dx=-2*x/dotNum
    while x<=x_max:
        y=f(x)
        x=x+dx
        if type(y)==complex or abs(0.5*Hight-y*UnitLen)>=10**3 or y=='error':
            bigList.append(dotLsit)
            dotLsit=[]
            continue
        dotLsit.append((0.5*Width+(x-dx)*UnitLen,0.5*Hight-y*UnitLen))
    bigList.append(dotLsit)
        

def plotImag():
    for i in bigList:
        if i!=[] and type(i)==list:
            pygame.draw.lines(Surface,Red,0,i,2)


calcuDots()
while 1:
    Surface.fill((0,0,0))
    plotCCS()
    plotImag()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
    pygame.time.Clock().tick(50)

#完成了基本函数绘制功能，但还无法将无意义的点排除在外。同时不知道负数开平方有无影响。下一步添加无意义点的鉴别以及多个函数图像的绘制 v1.00
#优化了对无意义点的算法，但仍然不能绘制分段函数。 下一步想办法能绘制1/x这类分段函数 v1.01
#添加了三角函数  v1.02
#添加了对无意义点的剔除，但仍然不能绘制出震荡点的图像 v1.03