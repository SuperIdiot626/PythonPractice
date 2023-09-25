#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time
width,height=480,640
pygame.init()
Surface=pygame.display.set_mode((width,height))
pygame.display.set_caption('Gravity Simulator')
TitleFro=pygame.font.Font('freesansbold.ttf',70)
clock=pygame.time.Clock()       #用于计时

class Planet(object):
    def __init__(self,surface):
        self.x=240
        self.y=200
        self.v_x=0
        self.v_y=0
        self.vh_x=0
        self.vh_y=0
        self.a_x=0
        self.a_y=5000
        self.radius=20
        self.surface=surface
        

    def move(self):
        #self.x+=self.v_x/50
        #self.y+=self.v_y/50
        self.x+=self.v_x*time_pass
        self.y+=self.v_y*time_pass
        

    def accelerate(self):
        #self.v_x+=self.a_x/50
        #self.v_y+=self.a_y/50
        self.v_x+=self.a_x*time_pass
        self.v_y+=self.a_y*time_pass

    def punch(self):
        if self.x<0:
            self.x=0
            self.v_x=-self.v_x
        if self.x>450:
            self.x=450
            self.v_x=-self.v_x
        if self.y<0:
            self.y=0
            self.vh_y=-self.vh_y
        if self.y>610:
            self.y=610
            self.vh_y=-self.vh_y

    def punch1(self):                               #边界碰撞检测   升级版
        delta_x=self.v_x*time_pass
        delta_y=self.v_y*time_pass
        if self.x+delta_x<self.radius:        #若下一时刻粒子超出 左 边界
            self.x=self.radius
            self.v_x=-self.v_x
        if self.x+delta_x>width-self.radius:  #若下一时刻粒子超出 右 边界
            self.x=width
            self.v_x=-self.v_x

        if self.y+delta_y<self.radius:        #若下一时刻粒子超出 上 边界
            self.y=self.radius              
            self.v_y=-self.v_y

        if self.y+delta_y>height-self.radius: #若下一时刻粒子超出 下 边界
            self.y=height
            self.v_y=-self.v_y

    def punch2(self):                               #边界碰撞检测   升级版2.0
        delta_x=self.v_x*time_pass
        delta_y=self.v_y*time_pass
        '''if self.x+delta_x<self.radius:        #若下一时刻粒子超出 左 边界
            self.x=2*self.radius-self.x-delta_x 
            self.v_x=-self.v_x
        if self.x+delta_x>width-self.radius:  #若下一时刻粒子超出 右 边界
            self.x=2*width-2*self.radius-self.x-delta_x 
            self.v_x=-self.v_x

        if self.y+delta_y<self.radius:        #若下一时刻粒子超出 上 边界
            self.y=2*self.radius-self.y-delta_y                
            self.v_y=-self.v_y'''

        if self.y+delta_y>height-self.radius: #若下一时刻粒子超出 下 边界
            self.y=2*height-2*self.radius-self.y-delta_y 
            self.v_y=-self.v_y

    def punch3(self):                               #边界碰撞检测   升级版3.0
        delta_y=self.v_y*time_pass+0.5*self.a_y**2
        

        if self.y+delta_y>height-self.radius: #若下一时刻粒子超出 下 边界
            t=(-self.v_y+(self.v_y**2-2*self.a_y*(self.x-height))**0.5)/self.a_y
            self.y=height-(self.v_y+self.v_y*t)*(time_pass-t)-0.5*self.a_y*(time_pass-t)**2
            self.v_y=-self.v_y-2*self.a_y+self.a_y*time_pass


    def frog_jump_start1(self):

        vh_x = self.v_x + self.a_x * time_pass/2    #计算蛙跳中间速度 
        vh_y = self.v_y + self.a_y * time_pass/2

        self.v_x += self.a_x * time_pass            #计算速度
        self.v_y += self.a_y * time_pass

        self.x += vh_x * time_pass                  #计算位移
        self.y += vh_y * time_pass

    def frog_jump_start2(self):

        vh_x = self.v_x + self.a_x * time_pass/2    #计算蛙跳中间速度
        vh_y = self.v_y + self.a_y * time_pass/2

        self.v_x += self.a_x * time_pass            #计算速度
        self.v_y += self.a_y * time_pass

        self.x += vh_x * time_pass                  #计算位移
        self.y += vh_y * time_pass

    def frog_jump_start(self):

        vh_x = self.v_x + self.a_x * 0.001/2    #计算蛙跳中间速度
        vh_y = self.v_y + self.a_y * 0.001/2

        self.v_x += self.a_x * 0.001           #计算速度
        self.v_y += self.a_y * 0.001

        self.x += vh_x * 0.001                  #计算位移
        self.y += vh_y * 0.001

    def frog_jump_step(self):
        self.vh_x += self.a_x * time_pass
        self.vh_y += self.a_y * time_pass

        self.v_x = self.vh_x + self.a_x * time_pass/2
        self.v_y = self.vh_y + self.a_y * time_pass/2

        self.x += self.vh_x * time_pass
        self.y += self.vh_y * time_pass



ball=Planet(Surface)
start=1
max_height=640
while 1:
    time_pass=clock.tick()/1000
    Surface.fill((0,0,0))
    
    
    ball.punch()
    #ball.accelerate()
    #ball.move()
    if start==1:
        #ball.frog_jump_start()
        ball.vh_y=ball.v_y-0.5*time_pass
        start=0
    else:
        ball.frog_jump_step()
    pygame.draw.circle(Surface,(255,0,0),(240,200),ball.radius)
    pygame.draw.circle(Surface,(255,255,255),(int(ball.x),int(ball.y)),ball.radius)
    
    if max_height>ball.y:
        max_height=ball.y
        print(max_height)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
    pygame.display.update()
    #pygame.time.Clock().tick(50)

#完成了基本操作，一个小球在重力最用下坠落。锁定了帧率50。优化了碰撞函数，或许能用在弹射球上。