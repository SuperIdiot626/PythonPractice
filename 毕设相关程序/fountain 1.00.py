import pygame
from pygame.locals import *
from sys import exit
from random import randint

w,h=480,640

gravity=100
source=(0.5*w,0.5*h)
droplist=[]

pygame.init()
screen = pygame.display.set_mode((w,h), 0, 32)
clock = pygame.time.Clock()

class drop(object):
    def __init__(self,vx,vy,ax,ay):
        self.x=0.5*w
        self.y=0.5*h
        self.vx=vx
        self.vy=vy
        self.ax=ax
        self.ay=ay
        droplist.append(self)

    def newPosition(self):
        self.x=self.x+self.vx*time_pass
        self.y=self.y+self.vy*time_pass
    
    def newVelocity(self):
        self.vx=self.vx+self.ax*time_pass
        self.vy=self.vy+self.ay*time_pass

    def display(self):
        pygame.draw.line(screen,(255,255,255),(self.x,self.y),(self.x+1,self.y+1))

def on_screen(drop):
        return drop.y < h
        

while True:
    screen.fill((0,0,0))
    time_pass=clock.tick()/1000
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
    
    if len(droplist)<=5000:
        drop(randint(-75,75),randint(-200,-50),0,gravity)

    for i in droplist:
        i.newVelocity()
    for i in droplist:
        i.newPosition()
        i.display()
    
    droplist= list(filter(on_screen,droplist))
    pygame.display.update()