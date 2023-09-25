#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

h=0.25              #步长
steps=1000          #步数
u=2                 #初始x
v=2                 #初始y
UnitLen=100         #单位长度
Width=1000          #UI宽度
choose=3            #1:显式算法，2:隐式算法，3:辛算法，4:循环播放
Hight=0.6*Width

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

Width=int(Width)
Hight=int(Hight)
t=1
dotList=[]
dotVal=[]
bigList=[[],[],[],[]]


pygame.init()
Surface=pygame.display.set_mode((Width,Hight))
pygame.display.set_caption('GNI experiment Fig 1.2')
TitleFro=pygame.font.Font('freesansbold.ttf',20)
Zero=TitleFro.render('0',1,WHITE)
One=TitleFro.render('1',1,WHITE)


def plotCCS():
    pygame.draw.line(Surface,WHITE,(20,0.5*Hight),(Width-20,0.5*Hight),3)   #绘制横轴
    pygame.draw.line(Surface,WHITE,(0.5*Width,20),(0.5*Width,Hight-20),3)   #绘制纵轴
    pygame.draw.line(Surface,WHITE,(0.5*Width-UnitLen,0.5*Hight),(0.5*Width-UnitLen,0.5*Hight-8),3)
    pygame.draw.line(Surface,WHITE,(0.5*Width+UnitLen,0.5*Hight),(0.5*Width+UnitLen,0.5*Hight-8),3)   #绘制横轴单位
    pygame.draw.line(Surface,WHITE,(0.5*Width,0.5*Hight-UnitLen),(0.5*Width+8,0.5*Hight-UnitLen),3)
    pygame.draw.line(Surface,WHITE,(0.5*Width,0.5*Hight+UnitLen),(0.5*Width+8,0.5*Hight+UnitLen),3)   #绘制纵轴单位
    pygame.draw.lines(Surface,WHITE,0,[(Width-32,0.5*Hight-12),(Width-20,0.5*Hight),(Width-32,0.5*Hight+12)],4)   #绘制制横箭头 
    pygame.draw.lines(Surface,WHITE,0,[(0.5*Width-12,32),(0.5*Width,20),(0.5*Width+12,32)],4)    #绘制纵轴箭头
    Surface.blit(Zero,(0.5*Width-15,0.5*Hight+5))           #标出原点
    Surface.blit(One,(0.5*Width-14,0.5*Hight-UnitLen-10))   #标出纵轴单位1
    Surface.blit(One,(0.5*Width+UnitLen-5,0.5*Hight+5))     #标出横轴单位1


def explicit(u,v):
    dudt=u*(v-2)
    dvdt=v*(1-u)
    x=u+h*dudt
    y=v+h*dvdt
    dotVal.append([x,y])
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))


def implicit(u,v):
    ax=(1+2*h)*h/(1-h)
    bx=1+2*h-(u+v)*h/(1-h)
    cx=-u
    ay=(h-1)*h/(1+2*h)
    by=1-h+(u+v)*h/(1+2*h)
    cy=-v
    x=formula(ax,bx,cx)
    y=formula(ay,by,cy)
    dotVal.append([x[0],y[0]])
    dotList.append((0.5*Width+x[0]*UnitLen,0.5*Hight-y[0]*UnitLen))


def symplectic(u,v):
    x=u*(1-2*h+v*h/(h*u-h+1))
    y=v/(1+h*u-h)
    dotVal.append([x,y])
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))


def formula(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        print('error')
        return 'error'
    else:
        x1=(-b+delta**0.5)/2/a
        x2=(-b-delta**0.5)/2/a
        return(x1,x2)


def switch(choose):
    global f
    global dotList
    if choose!=4:
        if choose==1:
            f=explicit
        elif choose==2:
            f=implicit
        elif choose==3:
            f=symplectic
        f(u,v)
        calcuDots()
    if switch==4:
        n=1
        while n<=3:
            switch(n)
            f(u,v)
            calcuDots()
            bigList.append(dotList)
            print(bigList)
            dotList=[]
            n=n+1


def calcuDots():
    n=0
    while n<steps:
        f(dotVal[-1][0],dotVal[-1][1])
        dotVal.pop(0)
        n+=1
    n=0    
    f(1,1)
    while n<steps:
        f(dotVal[-1][0],dotVal[-1][1])
        n+=1    
    

def plotImag():
    if choose!=4:
        pygame.draw.aalines(Surface,RED,0,dotList,2)
    else:
        for i in bigList:
            pygame.draw.aalines(Surface,RED,0,i,2)

def timer():
    global t
    t+=1
    t%=50
    if t==0:
        return 0
    else:
        return 1


switch(choose)
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
    pygame.time.Clock().tick(40)