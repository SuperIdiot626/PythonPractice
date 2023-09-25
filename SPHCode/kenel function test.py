#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *
from vectorcalculate import *

width,height=760,600                                #窗口大小
circle_radius_multi=1.2                             #绘制圆形半径与网格宽度的比率  应设置为大于2.5
grid_width=40                                       #网格宽度
smooth_length=grid_width*circle_radius_multi        #光滑长度

pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('Kenel Function Test')
clock=pygame.time.Clock()

#在屏幕上生成网格，且为每个点设置随机温度
pos_list=[]
tem_list=[]
x,y=0,0
n=0
while y<=height:           #绘制网点
    while x<=width:
        pos_list.append( (x,y) )
        tem_list.append(n)
        n+=1
        x+=grid_width
    y+=grid_width
    x=0


def kenel_function(X,X1,h):   #核函数，待测试
    q=magenititude(minus(X,X1))/h
    if q>1:
        return '0'
    else:
        return 1#(1+3*q-q**3-3*q**4)


def nearest_dot_tem(mouse_pos):                                 #找到距离鼠标最近点的温度
    mouse_pos=pygame.mouse.get_pos()
    mouse_grid_potential_1=(mouse_pos[0]//grid_width*grid_width,mouse_pos[1]//grid_width*grid_width)      #左上
    mouse_grid_potential_2=(mouse_grid_potential_1[0]+grid_width,mouse_grid_potential_1[1])             #右上
    mouse_grid_potential_3=(mouse_grid_potential_1[0],mouse_grid_potential_1[1]+grid_width)             #左下
    mouse_grid_potential_4=(mouse_grid_potential_1[0]+grid_width,mouse_grid_potential_1[1]+grid_width)  #右下
    mouse_grid_poslist=[mouse_grid_potential_1,mouse_grid_potential_2,mouse_grid_potential_3,mouse_grid_potential_4]#形成列表
    distance_list=[]

    for i in mouse_grid_poslist:                                #计算鼠标位置与最近四个点的距离
        distance_list.append(magenititude_simple(minus(mouse_pos,i)))
    i=distance_list.index(min(distance_list))                   #找出最近的点位
    mouse_grid_pos=mouse_grid_poslist[i]
    
    tem_show=tem_list[pos_list.index(mouse_grid_pos)]           #显示该点温度
    tem_show=pygame.font.Font('freesansbold.ttf',20).render(str(tem_show),1,(200,200,200))
    screen.blit(tem_show,mouse_grid_pos)


def calculate_tem(mouse_pos):
    num_within_domain=0                     #最终影响域圆内粒子数量
    final_tem=0                             #最终温度
    dots_pos_within_domain=[]               #影响域方框内粒子坐标

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]          #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]         #影响域方框右下角坐标
    left_top=times(  plus(  quotient(  left_top,(grid_width,grid_width)  ),(1,1)  )  ,  grid_width  )           #取其右下的点
    right_bot=times(quotient(right_bot,(grid_width,grid_width)),grid_width)                                     #取其左上的点
                   
    y=int(left_top[1])
    while y<=right_bot[1]:              #找出影响域方框内的点
        x=int(left_top[0]) 
        while x<=right_bot[0]:
            dots_pos_within_domain.append( (x,y) )
            x+=grid_width
        y+=grid_width


    for i in dots_pos_within_domain:
        
        pygame.draw.circle(screen,(255,0,0),i,5)            #红色标出 影响域方框 内粒子
        kenel_function_result = kenel_function(mouse_pos,i,smooth_length)

        if kenel_function_result=='0':                      #用于判定粒子是否处于影响域圆   
            continue
        num_within_domain+=1   
        pygame.draw.circle(screen,(0,255,0),i,10)           #绿色标出 影响域圆 内粒子

    
        final_tem += tem_list[pos_list.index(i)] * kenel_function_result

    final_tem/=num_within_domain 
    print(final_tem)

    return int(final_tem)


'''
x,y=2,2
n=0
color_table=pygame.Surface((width,height),depth=24)
while y<height-20:           #计算每个坐标的温度，然后绘制为背景
    while x<width-20:
        n=calculate_tem((x,y))
        n=int(n/(550)*256-1)
        if n<128:
            r=0
            g=2*n
            b=255-n*2   
        else:
            r=2*n-255
            g=511-2*n
            b=0
        x+=1
        color_table.set_at((x,y), (r, g, b))
    y+=1
    x=10
pygame.image.save(color_table, "kenel function=(1+3*q-q**3-3*q**4).png")
'''


while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    
    pressed_mouse=pygame.mouse.get_pressed()  #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()          #得到鼠标位置
    if pressed_mouse[0]==1: 
        calculate_tem(mouse_pos)

    nearest_dot_tem(mouse_pos)

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))
    screen.blit(mouse_pos_show,(0,0))                               #显示当前鼠标位置

    pygame.draw.circle(screen,(255,255,255),mouse_pos,int(smooth_length),1)        # smooth_length 的网格间距画圆

    for i in pos_list:  #绘出网格点
        pygame.draw.circle(screen,(255,255,255),i,2)
   
    #screen.blit(color_table,(0,0))
    pygame.display.update()
