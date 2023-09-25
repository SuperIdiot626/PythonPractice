#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time

pygame.init()
Surface=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Gravity Simulator')
TitleFro=pygame.font.Font('freesansbold.ttf',70)

global GravityCons
global MassCenter

MassCenter=2000
GravityCons=10000
Mass_x=500
Mass_y=400


class Planet(object):
    def __init__(self,surface):
        self.x=400
        self.y=400
        self.v_x=-200
        self.v_y=300
        self.a_x=0
        self.a_y=0
        self.mass=100
        self.surface=surface
        self.tracks=[[self.x,self.y]]

    def move(self):
        self.x+=self.v_x/50
        self.y+=self.v_y/50

    def accelerate(self):
        self.v_x+=self.a_x/50
        self.v_y+=self.a_y/50

    def acceleratecompute(self):
        Distance=((self.x-Mass_x)**2+(self.y-Mass_y)**2)**0.5
        self.a_x=GravityCons*MassCenter*(Mass_x-self.x)/Distance**3
        self.a_y=GravityCons*MassCenter*(Mass_y-self.y)/Distance**3

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
        pygame.draw.lines(Surface,(255,255,255),0,self.tracks,1)
    
    def display(self):
        self.track()
        self.acceleratecompute()
        self.accelerate()
        self.move()
        pygame.draw.circle(self.surface,(255,255,255),(int(self.x),int(self.y)),10)

ball=Planet(Surface)


while 1:
    Surface.fill((0,0,0))
    ball.display()
    pygame.draw.circle(Surface,(200,0,0),(500,400),10)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
    pygame.display.update()
    pygame.time.Clock().tick(50)

#重力模拟器v2.00  可以模拟单独的星体绕某一固定质量中心旋转。可以画出相应轨迹。基本实现了想要的功能。下一步进行两颗星体的运动模拟。