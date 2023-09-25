#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time

pygame.init()
Surface=pygame.display.set_mode((480,640))
pygame.display.set_caption('Gravity Simulator')
TitleFro=pygame.font.Font('freesansbold.ttf',70)

class Planet(object):
    def __init__(self,surface):
        self.x=240
        self.y=200
        self.v_x=0
        self.v_y=0
        self.a_x=0
        self.a_y=10000
        self.surface=surface
        self.image=pygame.image.load("./eyeball.png").convert()

    def move(self):
        self.x+=self.v_x/50
        self.y+=self.v_y/50

    def accelerate(self):
        self.v_x+=self.a_x/50
        self.v_y+=self.a_y/50

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

ball=Planet(Surface)

while 1:
    Surface.fill((0,0,0))
    ball.accelerate()
    ball.move()
    Surface.blit(ball.image,(ball.x,ball.y))
    ball.punch()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
    pygame.display.update()
    pygame.time.Clock().tick(50)

#完成了基本操作，一个小球在重力最用下坠落。锁定了帧率50。优化了碰撞函数，或许能用在弹射球上。