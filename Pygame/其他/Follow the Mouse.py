#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()
screen = pygame.display.set_mode((480, 640), 0, 32)
pygame.display.set_caption('Follow the Mouse')
background=pygame.image.load('background1.png').convert()
sprite=pygame.image.load('hero.png').convert_alpha()

clock=pygame.time.Clock()
position=(240,320)
velocity=(0,0)

def plus(vector1,vector2,switch=1):
    if switch ==1:
        return(vector1[0]+vector2[0],vector1[1]+vector2[1])
    elif switch ==-1:
        return(vector1[0]-vector2[0],vector1[1]-vector2[1])
def magenititude(vector):
    return (vector[0]**2+vector[1]**2)**0.5
def times(vector,h):
    return (vector[0]*h,vector[1]*h)
def normalize(vector):
    s=magenititude(vector)
    return (vector[0]/s,vector[1]/s)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    mouse_pos = pygame.mouse.get_pos()
    direction = times(normalize(plus(mouse_pos,position,-1)),0.5)
    velocity = plus(velocity,direction,+1)

    time_pass=clock.tick()/1000
    position=plus(position,times(velocity,time_pass))

    screen.blit(background,(0,0))
    screen.blit(sprite,plus(position,times(sprite.get_size(),0.5),-1))
    pygame.display.update()