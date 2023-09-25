#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *
from vectorcalculate import *

width,height=800,600
radius=40

center_x=width//2
center_y=height//2
ball_x,ball_y=-width,-height
wait_shot=0   #等待射击
click_allow=1 #下次按键是否有效？
punched=0     #是否进行碰撞判定？
tracks=[]     #轨迹储存
balllist=[]
newballpos=[0,0]
newballvel=[0,0]
newballradius=0


pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('多球碰撞1')
clock=pygame.time.Clock()

class balls(object):
    def __init__(self,pos,vel,color):
        self.pos=pos
        self.vel=vel
        self.color=color#

        self.id=len(balllist)+1
        self.radius=randint(0,20)
        #self.radius=radius
        self.acce=[0,0]
        self.tracks=[]
        balllist.append(self)

    def positioncompute(self):
        self.pos=plus(times(self.vel,time_pass),self.pos)

    def velocitycompute(self):
        self.vel=plus(times(self.acce,time_pass),self.vel)

    def acceleratecompute(self):
        self.acce=[0,0]
    
    def punch(self):   #简易边界碰撞检测
        if (self.pos[0]+self.vel[0]*time_pass>=width-radius) or (self.pos[0]+self.vel[0]*time_pass<=radius):
            self.vel[0]=-self.vel[0]
        if (self.pos[1]+self.vel[1]*time_pass>=height-radius) or (self.pos[1]+self.vel[1]*time_pass<=radius):
            self.vel[1]=-self.vel[1]

        for i in balllist[self.id::]:   #与其他球体的碰撞检测
            if i==self:
                continue
            distance_vec=minus(self.pos,i.pos)
            distance=magenititude(distance_vec)
            if distance<=self.radius+i.radius:

                self.vel[1]=-self.vel[1]   
                i.vel[1]=-i.vel[1]
                distance_vec[1]=-distance_vec[1]  #将两球速度、距离向量转化为右手系

                degree=float(angle_to_horizontal(distance_vec))
                new_self_vel=rotate_CCS(self.vel,degree)
                new_i_vel=rotate_CCS(i.vel,degree)
                new_self_vel[0],new_i_vel[0]=new_i_vel[0],new_self_vel[0]    #连心线方向速度交换，另一方向速度不变
                self.vel=rotate_CCS(new_self_vel,0-degree)
                i.vel=rotate_CCS(new_i_vel,0-degree)

                self.vel[1]=-self.vel[1]
                i.vel[1]=-i.vel[1]   #将两球速度、距离向量转化为左手系

    def display(self):
        self.positioncompute()
        self.velocitycompute()
        self.punch()
        pygame.draw.circle(screen,self.color,list(map(round,self.pos)),self.radius)


while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    if event.type == VIDEORESIZE:
            width,height = event.size           #为了使调整窗口大小后相对位置不变
            Surface=pygame.display.set_mode((width,height),RESIZABLE)

    time_pass=clock.tick()/1000
    pressed_mouse=pygame.mouse.get_pressed()  #得到鼠标按键状态

    if click_allow==1 and pressed_mouse[2]==1:  #右键清空所有球
        click_allow=0
        balllist=[]

    if click_allow==1 and pressed_mouse[0]==1:   #若允许点击且按下左键
        click_allow=0                            #等鼠标松开后（allow会置1）才能进行下次点击
        mouse_pos=pygame.mouse.get_pos()         #得到鼠标当前位置，并设为球所在位置
        if wait_shot==0:          #shot为0，将鼠标位置赋给球
            newballpos=mouse_pos                #新球位置
            newballcolor=(randint(0,255),randint(0,255),randint(0,255))  #新球颜色
            wait_shot=1                               #可以进行射击
        elif wait_shot==1:
            newballvel=minus(mouse_pos,newballpos)  #由两次点击的位置差确定速度  新球速度
            ball=balls(newballpos,newballvel,newballcolor)  #产生新球
            wait_shot=0                                 #发射了，shot为2时持续计算下一时刻速度

    if click_allow==0 and pressed_mouse[0]==1:     #随时间增加半径  待完成
        newballradius+=time_pass*4

    if pressed_mouse[0]==0 and click_allow==0:   #松开鼠标按键，可以进行下次点击
        click_allow=1
        newballradius=0

    if wait_shot==1:
        pygame.draw.circle(screen,newballcolor,newballpos,round(newballradius))  #画出球的位置

    for i in balllist:
        i.display()

    pygame.display.update()

    #左键生成球