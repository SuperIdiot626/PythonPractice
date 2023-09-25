#!/usr/bin/env python3

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_w,screen_h=1000,640
screen = pygame.display.set_mode((screen_w,screen_h),RESIZABLE,32)

color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor=0
def color_inter():
    r1,g1,b1=color1
    r2,g2,b2=color2
    r=r1-factor*(r1-r2)
    g=g1-factor*(g1-g2)
    b=b1-factor*(b1-b2)
    return r,g,b

while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        if event.type == VIDEORESIZE:
            screen_w,screen_h = event.size           #为了使调整窗口大小后相对位置不变
            Surface=pygame.display.set_mode((screen_w,screen_h),RESIZABLE)
    if pygame.mouse.get_pressed()[0]:
        factor=pygame.mouse.get_pos()[0]/screen_w
        pygame.display.set_caption("Color Palette - "+str(factor))
    color=color_inter()
    screen.fill(color)
    pygame.draw.circle(screen,(255,255,255),(int(factor*screen_w),int(screen_h/2)),20)
    pygame.display.update()