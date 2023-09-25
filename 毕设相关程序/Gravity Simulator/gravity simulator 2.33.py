#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
import time
from pygame.locals import *
from random import randint

massiveFollow=0                 #是否锁定视角
tracksShow=True                 #是否显示轨迹
blankBorder=100                 #星球生成范围
FPS=50                          #帧率
GRAVITYCONS=2000                #重力常数
DENSITY=5                       #星球密度
Width=1000                      #UI宽度
Hight=0.5625*Width

PI=3.1415926                    #圆周率
WHITE=(255,255,255)
GREEN=(0,255,0)

PlanetList=[]
clearTrack=0
Width=int(Width)
Hight=int(Hight)

pygame.init()
Surface=pygame.display.set_mode((Width,Hight),RESIZABLE)
pygame.display.set_caption('Gravity Simulator')


class Planet(object):
    def __init__(self,x=400,y=400,v_x=-100,v_y=0,color=WHITE,mass=200,id=1,surface=Surface):
        self.x=x
        self.y=y
        self.v_x=v_x
        self.v_y=v_y
        self.mass=mass
        self.color=color
        self.a_x=0
        self.a_y=0
        self.radius=(self.mass/PI/DENSITY)**0.5
        self.surface=surface
        self.tracks=[[self.x,self.y]]
        PlanetList.append(self)
        self.id=id
        self.str_id=pygame.font.Font('freesansbold.ttf',15).render(str(id),1,WHITE)

    def move(self):
        self.x+=self.v_x/FPS
        self.y+=self.v_y/FPS

    def accelerate(self):
        self.v_x+=self.a_x/FPS
        self.v_y+=self.a_y/FPS

    def acceleratecompute(self):
        self.a_x=0
        self.a_y=0
        for i in PlanetList:
            if len(PlanetList)==1:
                break
            distance=((self.x-i.x)**2+(self.y-i.y)**2)**0.5
            if i==self:
                continue
            self.a_x=self.a_x+GRAVITYCONS*i.mass*(i.x-self.x)/distance**3
            self.a_y=self.a_y+GRAVITYCONS*i.mass*(i.y-self.y)/distance**3
    
    def punch(self):
        for i in PlanetList:
            if i==self:
                continue
            distance=((self.x-i.x)**2+(self.y-i.y)**2)**0.5
            if distance<=(self.radius+i.radius):
                if self.mass<i.mass:
                    self.color=i.color
                    self.id=i.id
                    self.tracks=i.tracks
                self.x=(self.mass*self.x+i.mass*i.x)/(self.mass+i.mass)
                self.y=(self.mass*self.y+i.mass*i.y)/(self.mass+i.mass)
                self.v_x=(self.mass*self.v_x+i.mass*i.v_x)/(self.mass+i.mass)
                self.v_y=(self.mass*self.v_y+i.mass*i.v_y)/(self.mass+i.mass)
                self.mass=self.mass+i.mass
                self.radius=(self.mass/PI/DENSITY)**0.5
                PlanetList.remove(i)

    def track(self):
        if tracksShow==True:
            self.tracks.append((self.x,self.y))
            if len(self.tracks)>=500:
                self.tracks.pop(0)
            pygame.draw.aalines(Surface,self.color,0,self.tracks,1)
    
    def display(self):
        self.accelerate()
        self.move()
        self.track()
        pygame.draw.circle(self.surface,self.color,(int(self.x),int(self.y)),int(self.radius))
        Surface.blit(self.str_id,(self.x,self.y))


def generateplanets(x):
    n=1
    while n<=x:
        RandomColor=(randint(0,255),randint(0,255),randint(0,255))
        randomX=randint(blankBorder,Width-blankBorder)
        randomY=randint(blankBorder,Hight-blankBorder)
        randomV_X=randint(-200,200)
        randomV_Y=randint(-200,200)
        randomMass=randint(0,100)
        ball=Planet(randomX,randomY,randomV_X,randomV_Y,RandomColor,randomMass,n)
        n=n+1


def centerlize(n):
    if n:
        global massivePlanet
        global clearTrack
        a=massivePlanet
        for i in PlanetList:
            if i.mass>=massivePlanet.mass:
                if i.mass!=massivePlanet.mass and massivePlanet.id!=i.id:
                    clearTrack=1
                massivePlanet=i
        if a!=massivePlanet:
            for i in PlanetList:
                i.v_x=i.v_x+massivePlanet.v_x
                i.v_y=i.v_y+massivePlanet.v_y
        for i in PlanetList:
                i.x=i.x-massivePlanet.x+0.5*Width
                i.y=i.y-massivePlanet.y+0.5*Hight
                #i.v_x=i.v_x+massivePlanet.v_x
                #i.v_y=i.v_y+massivePlanet.v_y

#ball2=Planet(0.5*Width,0.5*Hight,100,0,(255,255,255),1000)
#ball3=Planet(0.5*Width,0.5*Hight+100,100,0,(255,255,255),20)
generateplanets(100)
massivePlanet=PlanetList[0]
while 1:
    center_x=0.5*Width
    center_y=0.5*Hight
    Surface.fill((0,0,0))
    centerlize(massiveFollow)
    if clearTrack==1:
        for i in PlanetList:
            i.tracks=[[i.x,i.y]]
        clearTrack=0
    for i in PlanetList:
        i.punch()
    for i in PlanetList:
        i.acceleratecompute()
    for i in PlanetList:
        i.display()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            Width, Hight = event.size
            if massiveFollow:
                for i in PlanetList:
                    if i!=massivePlanet:
                        i.x=i.x+0.5*Width-center_x
                        i.y=i.y+0.5*Hight-center_y
                clearTrack=1
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                tracksShow=not tracksShow
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    starNum=pygame.font.Font('freesansbold.ttf',50).render(str(len(PlanetList)),1,GREEN)
    Surface.blit(starNum,(0,0))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#重力模拟器v2.00  可以模拟单独的星体绕某一固定质量中心旋转。可以画出相应轨迹。基本实现了想要的功能。下一步进行两颗星体的运动模拟。
#可模拟任意数量、位置、速度和质量的行星运动，只需要添加相应定义即可。接下来应该考虑将其与现实数据挂钩，计算其时间、距离、质量上的数据换算。
#添加了计数器、序号显示、改善了撞击后星球颜色的变化规律。还添加了生硬的视角锁定。  v2.21
#可以在主视角改变时将轨迹删掉，按照此思路改善视角锁定
#改变视角后会将原轨道清空，避免了复杂折线出现的情况。同时可以方便的的决定是否要锁定视角。 v2.30
#对代码格式进行了一些规范化处理，具体规则见python笔记。 v2.31
#添加了空格控制轨迹显示的功能 v3.32
#解决了改变窗口大小时，星体相对位置错乱的bug   v3.33

#切换视角时，应该将其他星球加上视角中心星球的速度