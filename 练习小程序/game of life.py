#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
#from vectorcalculate    import *



width=1600
height=800
cell_side_length=5



cell_coordinate_list=[]
cell_list=[]
width_dots=width//cell_side_length
height_dots=height//cell_side_length




pygame.init()
screen=pygame.display.set_mode((width,height))
#screen=pygame.display.set_mode((width,height),FULLSCREEN)
pygame.display.set_caption('Game of Life v1.00')

class cell(object):
    def __init__(self,pos):
        self.pos=pos                                #坐标   不需要更新
        self.around_cells=[]                        #周围细胞储存
        self.state_now=randint(0,1)                 #当前时刻死活状态   需即时更新
        self.state_next=0                           #下一时刻死活状态   需即时更新
        self.around_cells_id=[]                     #周围细胞id储存
        self.around_cells=[]                        #周围细胞储存
        self.id=len(cell_list)                      #本细胞id

    def around_cells_compute(self):                 #计算并储存周围细胞坐标
        for i in range(-1,2):
            for j in range(-1,2):
                if i==j and i==0:
                    continue
                if self.pos[0]+i<0 or self.pos[1]+j<0 or self.pos[0]+i>width_dots or self.pos[1]+j>height_dots:
                    continue
                self.around_cells.append(cell_coordinate_list[self.pos[0]+i][self.pos[1]+j])
                self.around_cells_id.append(cell_coordinate_list[self.pos[0]+i][self.pos[1]+j].id)

    def state_next_cal(self):                       #判断下时刻生死状态
        life_point=0
        for i in self.around_cells:
            life_point+=i.state_now
        if life_point<=1 or life_point>=4:          #生命值小于2或大于3，则死
            self.state_next=0
        elif life_point==2:                         #生命值为2，则状态不变
            self.state_next=self.state_next
        else:                                       #生命值为其他状态，则生
            self.state_next=1

    def renew(self):
        self.state_now=self.state_next



def create_cells():                                 #生成细胞
    global cell_coordinate_list
    i=0
    while i <=width_dots:
        j=0
        cell_coordinate_list.append([])
        while j<=height_dots:
            new_cell=cell([i,j])
            cell_coordinate_list[i].append(new_cell)
            cell_list.append(new_cell)
            j+=1
        i+=1


def another_state():
    for i in cell_list:
        i.state_now=randint(0,1)

create_cells()
for i in cell_list:
    i.around_cells_compute()

a=0

while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    if pressed_mouse[0]==1:                         #点击鼠标左键，进行check动作
        another_state()

    a+=1
    for i in cell_list:
        i.state_next_cal()
    for i in cell_list:
        i.renew()


    for i in cell_list:
        if i.state_now==1:
            color=(255,255,255)
        else:
            color=(0,0,0)
        cell_side_length=int(cell_side_length)
        square_coordinate=(i.pos[0]*cell_side_length,i.pos[1]*cell_side_length)
        square_side=(cell_side_length,cell_side_length)
        pygame.draw.rect(screen,color, (square_coordinate,square_side),2)
    pygame.time.wait(100)
    
    pygame.display.update()