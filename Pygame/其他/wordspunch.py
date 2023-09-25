#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,time
from random import randint
from pygame.locals import *

width=480
height=640

pygame.init()
Surface=pygame.display.set_mode((width,height))
pygame.display.set_caption('CharacterPunch')
TitleFro=pygame.font.SysFont('默陌信笺手写体',50)
words=TitleFro.render('死吧！！',True,(255,0,0))
word_w=words.get_width()/2
word_h=words.get_height()/2
FPS=100
x=randint(0,width-word_w*2)
y=randint(0,height-word_h*2)
vx=randint(20,50)
vy=randint(20,50)


def punch():
    global vx,vy
    if x<0 or x+word_w*2>width:
        vx=-vx
    if y<0 or y+word_h*2>height:
        vy=-vy


while 1:
    punch()
    x=x+vx/FPS
    y=y+vy/FPS
    Surface.fill((0,0,0))
    Surface.blit(words,(x,y))
    
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 

    pygame.display.update()
    pygame.time.Clock().tick(FPS)