#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import time

pygame.init()
Surface=pygame.display.set_mode((480,640))
pygame.display.set_caption('Moonie')
TitleFro=pygame.font.Font('freesansbold.ttf',70)
TitleFro1=pygame.font.Font('freesansbold.ttf',30)
GameTitle1=TitleFro.render('Moonie!',True,(0,0,200))
GameTitle2=TitleFro.render('Moonie!',True,(255,255,255))
Start=TitleFro.render('START!',True,(200,0,0))


n=0
while 1:
    Surface.blit(GameTitle1,(100,100))
    pygame.display.update()
    time.sleep(0.08)
    Surface.blit(GameTitle2,(100,100))
    pygame.display.update()
    time.sleep(0.08)
    n+=1
    if n>5:
        Surface.blit(Start,(110,200))
        pygame.display.update()
    if n==12:
        break
    for event in pygame.event.get(): 
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

class Ball(object):
    def __init__(self,surface):
        self.v_x=0
        self.v_y=0
        self.x=240
        self.y=320
        self.a_x=0
        self.a_y=0
        self.surface=surface
        self.image=pygame.image.load("./eyeball.png").convert()

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

    def move(self):
        self.x+=self.v_x
        self.y+=self.v_y

    def accelerate(self):
        if abs(self.v_y)<0.1:
            self.v_y=0
        if abs(self.v_x)<0.1:
            self.v_x=0
        if self.v_x<=20:
            self.v_x+=self.a_x
        if self.v_y<=20:
            self.v_y+=self.a_y

    def display(self):
        Surface.blit(self.image,(self.x,self.y))
        self.move()
        self.accelerate()
        self.punch()

ball=Ball(Surface)
while 1:
    Surface.fill((0,0,0))
    ball.display()
    
    
    v_abs='velocity:'+str((ball.v_x**2+ball.v_y**2)**0.5)[0:5]
    v_abs_str=TitleFro1.render(v_abs,True,(255,255,255))
    Surface.blit(v_abs_str,(0,0))

    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
            if event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    ball.a_x=-0.5
                elif event.key==K_d or event.key==K_RIGHT:
                    ball.a_x=+0.5
                elif event.key==K_w or event.key==K_UP:
                    ball.a_y=-0.5
                elif event.key==K_s or event.key==K_DOWN:
                    ball.a_y=+0.5 
                elif event.key==K_SPACE:
                    ball.v_y*=0.7
                    ball.v_x*=0.7
            elif event.type==KEYUP:
                ball.a_y=0
                ball.a_x=0
    pygame.display.update()
    pygame.time.Clock().tick(30)

#完成从零到一，改进方向：①球替换成圆形②添加速度显示器、时间显示器③添加敌人④添加开始菜单选择  v1.00
#替换了素材图片，添加了速度显示器，改善了刹车功能；下一步：添加第二个球，添加开始菜单选择    v1.10
#优化了punch函数，将球类运动、加速、显示函数进行了整合，使主函数更简洁了。但仍存在某些情况下无法加速的问题。 v1.11