#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
import time
from pygame.locals import *
from random import randint

Width=1000
Hight=0.6*Width
Width=int(Width)
Hight=int(Hight)
Originx=int(0.5*Width)
Originy=int(0.5*Hight)

pygame.init()
Surface=pygame.display.set_mode((Width,Hight))
pygame.display.set_caption('Cartesian Coordinate Ssystem Creator')
TitleFro=pygame.font.Font('freesansbold.ttf',20)

UnitLen=55
UnitLen=int(UnitLen)
PI=3.1415926
White=(255,255,255)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)

Zero=TitleFro.render('0',1,White) 
One=TitleFro.render('1',1,White) 

def plot():
    pygame.draw.line(Surface,White,(0.5*Width,0.5*Hight),(Width-20,0.5*Hight),3)   #绘制横轴
    pygame.draw.lines(Surface,White,0,[(Width-32,0.5*Hight-12),(Width-20,0.5*Hight),(Width-32,0.5*Hight+12)],4)   #绘制箭头
    pygame.draw.circle(Surface,White,(Originx,Originy),1*UnitLen,3)  #绘制圆圈1
    pygame.draw.circle(Surface,White,(Originx,Originy),2*UnitLen,3)  #绘制圆圈2
    pygame.draw.circle(Surface,White,(Originx,Originy),3*UnitLen,3)  #绘制圆圈3
    Surface.blit(Zero,(0.5*Width-15,0.5*Hight+5))           #绘制原点
    Surface.blit(One,(0.5*Width+UnitLen,0.5*Hight+8))     #绘制横轴单位1

while 1:
    Surface.fill((0,0,0))
    plot()
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

#完成了基本功能，下一步准备添加改变单位的功能，例如单位长度代表1或10或其他数字等  v1.00