#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *
from vectorcalculate import *

x,y=0,0
width,height=800,600            #界面的长宽
smooth_length=50                #光滑长度
grid_list=[]                    #用于储存网格左上顶点坐标
ball_list=[]                    #用于储存所有粒子
balls_in_grid_list=[]           #用于储存各个格子中的粒子


pygame.init()
clock=pygame.time.Clock()       #用于计时
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('New Try of SPH')



class balls(object):
    def __init__(self,pos,tem,color):
        self.pos=pos                        
        self.tem=tem
        self.color=color
        self.id=len(ball_list)                      #以ball_list的长度作为id
        self.in_grid=( self.pos[0]//smooth_length*smooth_length , self.pos[1]//smooth_length*smooth_length)
        self.near_grids=[]                          #储存临近格子的id
        self.near_dots=[]                           #储存临近粒子的id
        ball_list.append(self)
        balls_in_grid_list[grid_list.index(self.in_grid)].append(self.id)       #使其所在的格子中记录自己的id   

    def find_near_grids(self):                      #找到其所在格周围的格子
        self.near_grids=[]                          #每次调用次函数需将本来的数据清空
        x=-1
        y=-1
        while y<=1:
            while x<=1:                             #利用异常处理了边界格子
                try:
                    n=grid_list.index((self.in_grid[0]+x*smooth_length,self.in_grid[1]+y*smooth_length))
                except ValueError:
                    x+=1
                    continue
                else:
                    x+=1
                    self.near_grids.append( n )   
            x=-1
            y+=1
    
    def find_near_dots(self):                       #找到周围的其他粒子
        self.near_dots=[]                           #每次调用此函数需清空原始数据
        for i in self.near_grids:
            self.near_dots+=balls_in_grid_list[i]   #直接使用list加法得出结果

    def renew(self):                                #更新自己数据
        self.find_near_grids()                          
        self.find_near_dots()


def create_balls(n):                                #n为生成球的数量
    time_pass=clock.tick()/1000
    print('自程序开始以来用时为：%.4f'%time_pass)
    m=0
    while m<n: 
        random_pos=[randint(0,width-1),randint(0,height-1)]
        random_tem=randint(0,100)
        random_color=(randint(0,255),randint(0,255),randint(0,255))
        balls(random_pos,random_tem,random_color)
        m+=1
    
    for i in ball_list:                             #生成小球后立刻进行更新
        i.renew()
    time_pass=clock.tick()/1000
    print('生成%d个小球用时：%.4f'%(n,time_pass))


while y<height:                                     #生成网格并记录左上角顶点坐标
    while x<width:
        grid_list.append((x,y))                     #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
        balls_in_grid_list.append([])               #为每个格子生成一个空列表用于记录其所含有的粒子
        x+=smooth_length
    y+=smooth_length
    x=0


create_balls(5000)

x=0                                                 #测试用
key_press_allow=1                                   #测试用
while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()
    if key_press_allow==1:
        if pressed_keys[257]:                       #按小键盘1 使 小球id+1
            x+=1
        if pressed_keys[258]:                       #按小键盘2 使 小球id+10
            x+=10
        if pressed_keys[259]:                       #按小键盘3 使 小球id+100
            x+=100
        key_press_allow=0
        x%=len(ball_list)
    if  (not pressed_keys[257]) and (not pressed_keys[258]) and (not pressed_keys[259]):
        key_press_allow=1


    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    show_grid=( mouse_pos[0]//smooth_length*smooth_length , mouse_pos[1]//smooth_length*smooth_length)      #寻找鼠标所在的格子
    pygame.draw.rect(screen,(255,255,255), (show_grid,(smooth_length,smooth_length)), 1)                    #画出鼠标所在的格子

    if pressed_mouse[0]==1:
        for i in ball_list[x].near_grids:
            pygame.draw.rect(screen,(255,0,0), (grid_list[i],(smooth_length,smooth_length)), 2)             #红色显示附近格子
        for i in ball_list[x].near_dots:
            pygame.draw.circle(screen,(255,255,255),ball_list[i].pos,6,2)                                   #白色圈出附近粒子

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))               #显示鼠标位置
    screen.blit(mouse_pos_show,(0,0)) 


    x_show=pygame.font.Font('freesansbold.ttf',30).render(str(x),1,(200,0,0))                               #显示当前查看粒子的id
    screen.blit(x_show,(0,30)) 

    pygame.draw.circle(screen,(255,255,255),ball_list[x].pos,15,1)                                          #显示目前选中粒子的位置

    for i in balls_in_grid_list[grid_list.index(show_grid)]:
        pygame.draw.circle(screen,(255,255,255),ball_list[i].pos,5,1)

    for i in ball_list:
        pygame.draw.circle(screen,i.color,i.pos,2,1)
    pygame.display.update()



#改进：关于查找相邻格子的：可以事先计算出每一行m个格子，然后利用格子ID，±1和±m并±1，但会遇到边界格子无法处理的问题
