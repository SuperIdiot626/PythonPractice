#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

h=0.1              #步长
steps=100         #步数
u=5                 #初始x
v=5                 #初始y
UnitLen=40          #单位长度
Width=1000          #UI宽度
switch=1            #1:显式算法，2:隐式算法，3:中点算法，4:辛算法
Hight=0.6*Width

WHITE=(255,255,255)
RED=(255,0,0)

Width=int(Width)
Hight=int(Hight)
dotList=[]
dotPosi=[]

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


def f(u,v):
    dudt=u*(v-2)
    dvdt=v*(1-u)
    u=u+h*dudt
    v=v+h*dvdt
    dotPosi.append([u,v])
    dotList.append((0.5*Width+u*UnitLen,0.5*Hight-v*UnitLen))
    

def calcuDots():
    n=0
    while n<steps:
        f(dotPosi[-1][0],dotPosi[-1][1])
        dotPosi.pop(0)
        n+=1
    

def plotImag():
    pygame.draw.aalines(Surface,RED,0,dotList,2)


f(u,v)
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