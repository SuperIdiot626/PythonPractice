#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
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
UnitLen=40
dotList=[]
dotVal=[]
h=0.1 #步长
steps=100000  #迭代次数

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


def symplectic(x0,y0):
    x=x0*(1-2*h+y0*h/(h*x0-h+1))
    y=y0/(1+h*x0-h)
    dotVal.append([x,y])
    dotList.append((0.5*Width+x*UnitLen,0.5*Hight-y*UnitLen))


def calcuDots():
    n=0
    while n<steps:
        symplectic(dotVal[-1][0],dotVal[-1][1])
        dotVal.pop(0)
        n+=1
    

def plotImag():
    pygame.draw.aalines(Surface,Red,0,dotList,2)


symplectic(6,2)
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