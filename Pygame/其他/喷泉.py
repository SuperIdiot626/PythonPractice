import pygame
from math import sin,cos
from pygame.locals import QUIT,KEYDOWN
from sys import exit
from random import uniform

w,h=800,640     #UI参数
gravity=150     #重力加速度
v_initial=300    #初始速度
beginangle=60   #起始角度
branchnumber=7  #喷泉条数

branchgap=(180-beginangle*2)/(branchnumber+1)
source=(0.5*w,0.8*h)
droplist=[]
n=1

pygame.init()
screen = pygame.display.set_mode((w,h), 0, 32)
clock = pygame.time.Clock()

class drop(object):
    def __init__(self,vx,vy,ax,ay):
        self.x=source[0]
        self.y=source[1]
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
        pygame.draw.circle(screen,(255,255,255),(int(self.x),int(self.y)),2)

def on_screen(drop):
        return drop.y < h
        
def generate_drop():
    global n
    n=n%branchnumber+1
    middleangle=n*branchgap+beginangle
    randomangle=uniform(middleangle-3,middleangle+3)
    vx=-v_initial*cos(randomangle/180*3.1415)
    vy=-v_initial*sin(randomangle/180*3.1415)
    drop(vx,vy,0,gravity)


while True:
    screen.fill((0,0,0))
    time_pass=clock.tick()/1000
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
    generate_drop()
    generate_drop()
    generate_drop()
    generate_drop()
    generate_drop()
    for i in droplist:
        i.newVelocity()
        i.newPosition()
        i.display()
    
    droplist= list(filter(on_screen,droplist))
    pygame.display.update()