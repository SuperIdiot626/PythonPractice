#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from pygame.locals import *

width,height=800,600
radius=40

center_x=width//2
center_y=height//2
ball_x,ball_y=-width,-height
velocity=[0,0]
wait_shot=0   #等待射击
click_allow=1 #下次按键是否有效？
punched=0     #是否进行碰撞判定？
tracks=[]     #轨迹储存

pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('two dimensional punch')
clock=pygame.time.Clock()

while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            print(tracks)
            exit()
    if event.type == VIDEORESIZE:
            width,height = event.size           #为了使调整窗口大小后相对位置不变
            center_x=width//2
            center_y=height//2
            Surface=pygame.display.set_mode((width,height),RESIZABLE)

    time_pass=clock.tick()/1000
    pressed_mouse=pygame.mouse.get_pressed()  #得到鼠标按键状态

    if click_allow==1 and pressed_mouse[0]==1:   #若允许点击且按下左键
        click_allow=0                            #等鼠标松开后（allow会置1）才能进行下次点击
        mouse_pos=pygame.mouse.get_pos()         #得到鼠标当前位置，并设为球所在位置
        if wait_shot==0:
            tracks=[]                  
            ball_x,ball_y=mouse_pos[0],mouse_pos[1]   #shot为0，将鼠标位置赋给球
            wait_shot=1                               #可以进行射击
        elif wait_shot==1:
            velocity=[mouse_pos[0]-ball_x,mouse_pos[1]-ball_y]  #由两次点击的位置差确定速度
            wait_shot=0                                 #发射了，shot为2时持续计算下一时刻速度
            punched=0                                  #punched为0可以进行撞击判定
    if pressed_mouse[0]==0 and click_allow==0:   #松开鼠标按键，可以进行下次点击
        click_allow=1
    
    if velocity[0]!=0:              #反弹检测
        if ball_x+time_pass*velocity[0]>=width-radius:
            t=(width-radius-ball_x)/velocity[0]
            ball_x=width-radius-(time_pass-t)*velocity[0]
            velocity[0]=-velocity[0]
            tracks.append([width-radius,round(ball_y+velocity[1]*t)])
        elif ball_x+time_pass*velocity[0]<=radius:
            t=(radius-ball_x)/velocity[0]
            ball_x=radius+(time_pass-t)*velocity[0]
            velocity[0]=-velocity[0]
            tracks.append([radius,round(ball_y+velocity[1]*t)])
        if ball_y+time_pass*velocity[1]>=height-radius:
            t=(height-radius-ball_y)/velocity[1]
            ball_y=height-radius-(time_pass-t)*velocity[1]
            velocity[1]=-velocity[1]
            tracks.append([round(ball_x+velocity[0]*t),height-radius])
        elif ball_y+time_pass*velocity[1]<=radius:
            t=(radius-ball_y)/velocity[1]
            ball_y=radius+(time_pass-t)*velocity[1]
            velocity[1]=-velocity[1]
            tracks.append([round(ball_x+velocity[0]*t),radius])

    if wait_shot==0:   #计算下一时刻位置
        ball_x+=time_pass*velocity[0]
        ball_y+=time_pass*velocity[1]
        tracks.append([round(ball_x),round(ball_y)])
        if len(tracks)>=2:
            pygame.draw.aalines(screen,(255,0,0),0,tracks,1)
            tracks.pop()

    delta_x=center_x-ball_x     #两球的x差
    delta_y=center_y-ball_y     #两球的y差
    distance=delta_x**2+delta_y**2  #球心距离用于碰撞判定    

    if distance<=4*radius**2 and punched==0:
        if delta_x>=0:
            degree=math.atan(delta_y/delta_x)-0.5*math.pi   #++,+-
        if delta_x<0:
            degree=math.atan(delta_y/delta_x)+0.5*math.pi   #-+,--
        c=velocity[0]
        velocity[0]=velocity[0]*math.cos(2*degree)+velocity[1]*math.sin(2*degree)
        velocity[1]=c*math.sin(2*degree)-velocity[1]*math.cos(2*degree)
        tracks.append((round(ball_x),round(ball_y)))                  #添加一个路径点
        punched=1   #punched为1则不进行碰撞判定
    else:
        punched=0
    pygame.draw.circle(screen,(255,255,255),(int(ball_x),int(ball_y)),radius)   #画动球
    pygame.draw.circle(screen,(255,255,255),(center_x,center_y),radius)         #画定球
    pygame.display.update()