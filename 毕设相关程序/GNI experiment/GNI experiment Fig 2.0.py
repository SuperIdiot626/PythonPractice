#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

h=0.025             #步长
steps=1000          #步数
u=2                 #初始x
v=2                 #初始y
UnitLen=50          #单位长度
Width=1000          #UI宽度
choose=3            #1:显式算法，2:隐式算法，3:辛算法，4:循环播放
Hight=0.6*Width

WHITE=(255,255,255) #白色
RED=(255,0,0)       #红色
BLUE=(0,0,255)      #蓝色
GREEN=(0,255,0)     #绿色
BLACK=(0,0,0)       #黑色

BLACK=(255,255,255) #白色
WHITE=(0,0,0)       #黑色
RED=(0,0,255)       #红色

Width=int(Width)
Hight=int(Hight)
n=1                 #计数用
t=1
dotList=[]
dotVal=[]
dotList_list=[[],[],[],[]]
dot_pre=[0,0]


pygame.init()
Surface=pygame.display.set_mode((Width,Hight))
pygame.display.set_caption('GNI experiment Fig 1.2')
TitleFro=pygame.font.Font('freesansbold.ttf',20)
Zero=TitleFro.render('0',1,WHITE)
One=TitleFro.render('1',1,WHITE)


def plotCCS():                  #绘制坐标轴            
    pygame.draw.line(Surface,WHITE,(20,0.5*Hight),(Width-20,0.5*Hight),3)                                       #绘制横轴
    pygame.draw.line(Surface,WHITE,(0.5*Width,20),(0.5*Width,Hight-20),3)                                       #绘制纵轴
    pygame.draw.line(Surface,WHITE,(0.5*Width-UnitLen,0.5*Hight),(0.5*Width-UnitLen,0.5*Hight-8),3)
    pygame.draw.line(Surface,WHITE,(0.5*Width+UnitLen,0.5*Hight),(0.5*Width+UnitLen,0.5*Hight-8),3)             #绘制横轴单位
    pygame.draw.line(Surface,WHITE,(0.5*Width,0.5*Hight-UnitLen),(0.5*Width+8,0.5*Hight-UnitLen),3)
    pygame.draw.line(Surface,WHITE,(0.5*Width,0.5*Hight+UnitLen),(0.5*Width+8,0.5*Hight+UnitLen),3)             #绘制纵轴单位
    pygame.draw.lines(Surface,WHITE,0,[(Width-32,0.5*Hight-12),(Width-20,0.5*Hight),(Width-32,0.5*Hight+12)],4) #绘制制横箭头 
    pygame.draw.lines(Surface,WHITE,0,[(0.5*Width-12,32),(0.5*Width,20),(0.5*Width+12,32)],4)                   #绘制纵轴箭头
    Surface.blit(Zero,(0.5*Width-15,0.5*Hight+5))                                                               #标出原点
    Surface.blit(One,(0.5*Width-14,0.5*Hight-UnitLen-10))                                                       #标出纵轴单位1
    Surface.blit(One,(0.5*Width+UnitLen-5,0.5*Hight+5))                                                         #标出横轴单位1


def explicit(old_x,old_y):      #显式算法
    global dot_pre
    u=-old_y
    v=old_x
    x=old_x+h*u
    y=old_y+h*v
    dot_pre=[x,y]
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))
def implicit(old_x,old_y):      #隐式算法
    global dot_pre
    x=(old_x-h*old_y)/(1+h**2)
    y=(old_y+h*old_x)/(1+h**2)
    dot_pre=[x,y]
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))   
def symplectic(old_x,old_y):    #辛算法
    global dot_pre
    x=old_x-h**2*old_x-h*old_y
    y=old_y+h*old_x
    dot_pre=[x,y]
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))


def switch(choose):             #切换算法
    global f
    global dotList
    global dot_pre
    if choose!=4:
        if choose==1:
            f=explicit
        elif choose==2:
            f=implicit
        elif choose==3:
            f=symplectic
        f(u,v)
        calcuDots()

def calcuDots():                #点计算
    n=0
    while n<steps:
        f(dot_pre[0],dot_pre[1])
        n+=1

def plotImag():
    pygame.draw.circle(Surface,(RED),(int(0.5*Width+u*UnitLen),int(0.5*Hight-v*UnitLen)),5)
    #pygame.draw.aalines(Surface,RED,0,dotList,1)
    pygame.draw.lines(Surface,RED,0,dotList,2)
   
def video_maker():              #绘制动态图专用
    global n
    n=n+1
    if n >= len(dotList):
        n=n%len(dotList)+2
    a=dotList[:n]
    pygame.draw.lines(Surface,RED,0,a,2)
    pygame.draw.circle(Surface,(RED),(int(a[-1][0]),int(a[-1][1])),5)

        
switch(choose)
while 1:
    Surface.fill(BLACK)
    plotCCS()
    video_maker()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    pygame.time.Clock().tick(100)
    pygame.display.update()
    