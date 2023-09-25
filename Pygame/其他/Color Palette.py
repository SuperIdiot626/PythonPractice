#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

screen_w,screen_h=1000,640
height=screen_h//6

pygame.init()
screen = pygame.display.set_mode((screen_w,screen_h),RESIZABLE,32)
pygame.display.set_caption('Color Palette')
def color_scales():
    red_scale=pygame.surface.Surface((screen_w,height))
    green_scale=pygame.surface.Surface((screen_w,height))
    blue_scale=pygame.surface.Surface((screen_w,height))
    for i in range(screen_w):
        x=int(i/screen_w*255)
        red=(x,0,0)
        green=(0,x,0)
        blue=(0,0,x)
        line_rect=Rect(i,0,1,height)
        pygame.draw.rect(red_scale,red,line_rect)
        pygame.draw.rect(green_scale,green,line_rect)
        pygame.draw.rect(blue_scale,blue,line_rect)
    return red_scale,green_scale,blue_scale

red_scale,green_scale,blue_scale=color_scales()
color=[0,0,0]
while 1:
    screen.fill(color)
    screen.blit(red_scale,(0,0))
    screen.blit(green_scale,(0,height))
    screen.blit(blue_scale,(0,height*2))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        if event.type == VIDEORESIZE:
            screen_w,screen_h = event.size           #为了使调整窗口大小后相对位置不变
            Surface=pygame.display.set_mode((screen_w,screen_h),RESIZABLE)
            height=screen_h//6
            red_scale,green_scale,blue_scale=color_scales()
    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for i in range(3):
            if y>=i*height and y < (i+1)*height:
                color[i]=int(x/screen_w*255)
        pygame.display.set_caption("Color Palette - "+str(tuple(color)))
    for i in range(3):
        pygame.draw.circle(screen,(255,255,255),(int(color[i]*screen_w/255),int((i+0.5)*height)),20)
    pygame.display.update()