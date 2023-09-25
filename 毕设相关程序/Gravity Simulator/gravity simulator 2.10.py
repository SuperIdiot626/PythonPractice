#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time

pygame.init()
Surface=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Gravity Simulator')
TitleFro=pygame.font.Font('freesansbold.ttf',70)

GravityCons=10000

White=(255,255,255)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)


PlanetList=[]

class Planet(object):
    def __init__(self,x=400,y=400,v_x=-100,v_y=0,color=White,surface=Surface):
        self.x=x
        self.y=y
        self.v_x=v_x
        self.v_y=v_y
        self.a_x=0
        self.a_y=0
        self.mass=1000
        self.surface=surface
        self.tracks=[[self.x,self.y]]
        self.color=color
        PlanetList.append(self)        #???

    def move(self):
        self.x+=self.v_x/50
        self.y+=self.v_y/50

    def accelerate(self):
        self.v_x+=self.a_x/50
        self.v_y+=self.a_y/50

    def acceleratecompute(self):
        for i in PlanetList:
            Distance=((self.x-i.x)**2+(self.y-i.y)**2)**0.5
            if Distance==0:
                continue
            self.a_x=GravityCons*i.mass*(i.x-self.x)/Distance**3
            self.a_y=GravityCons*i.mass*(i.y-self.y)/Distance**3

    def punch(self):
        if self.x<0:
            self.x=0
            self.v_x=-self.v_x
        if self.x>450:
            self.x=450
            self.v_x=-self.v_x
        if self.y<0:
            self.y=0
            self.v_y=-self.v_y
        if self.y>610:
            self.y=610
            self.v_y=-self.v_y

    def track(self):
        self.tracks.append((self.x,self.y))
        pygame.draw.lines(Surface,self.color,0,self.tracks,1)
    
    def display(self):
        self.track()
        self.acceleratecompute()
        self.accelerate()
        self.move()
        pygame.draw.circle(self.surface,self.color,(int(self.x),int(self.y)),10)

#ball1=Planet(500,200,60,0,Red)                #不成功的三体运动数据
#ball2=Planet(500-100*3**0.5,500,-30,-30*3**0.5,Blue)
#ball3=Planet(500+100*3**0.5,500,-30,30*3**0.5,Green)

ball1=Planet(500,300,-200,10,Red)
ball2=Planet(500,500,200,-10,Blue)
#ball3=Planet(500+100*3**0.5,500,-30,30*3**0.5,Green)

while 1:
    Surface.fill((0,0,0))
    for i in PlanetList:
        i.display()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
    pygame.display.update()
    pygame.time.Clock().tick(50)

#重力模拟器v2.00  可以模拟单独的星体绕某一固定质量中心旋转。可以画出相应轨迹。基本实现了想要的功能。下一步进行两颗星体的运动模拟。
#可模拟任意数量、位置、速度和质量的行星运动，只需要添加相应定义即可。接下来应该考虑将其与现实数据挂钩，计算其时间、距离、质量上的数据换算。下一步设置随机位置与速度。 v2.10  