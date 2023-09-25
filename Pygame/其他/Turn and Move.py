#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,math
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((480, 640), 0, 32)
pygame.display.set_caption('Turn and Move')
background=pygame.image.load('background1.png').convert()
sprite=pygame.image.load('hero.png').convert_alpha()

clock=pygame.time.Clock()
position=(240,320)
direction=[0,0]
degree=0
speed=[200,200]
PI=3.1415926
def plus(vector1,vector2,switch=1):
    if switch ==1:
        return(vector1[0]+vector2[0],vector1[1]+vector2[1])
    elif switch ==-1:
        return(vector1[0]-vector2[0],vector1[1]-vector2[1])
def times(vector,h):
    return (vector[0]*h,vector[1]*h)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        move=[0,0]
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            move[0]=-1
        if pressed_keys[K_LEFT]:
            move[0]=+1
        if pressed_keys[K_UP]:
            move[1]=1
        if pressed_keys[K_DOWN]:
            move[1]=-1
        
    time_pass=clock.tick()/1000
    degree=(degree+ move[0]*speed[0]*time_pass)%360
   
    direction[0]=-math.sin(degree*PI/180)
    direction[1]=-math.cos(degree*PI/180)

    rotated_sprite = pygame.transform.rotate(sprite, degree)
    position=plus(position,times(direction,time_pass*speed[1]*move[1]))
    
    screen.blit(background,(0,0))
    screen.blit(rotated_sprite,plus(position,times(rotated_sprite.get_size(),0.5),-1))
    pygame.display.update()