#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *

#相关初始化
width,height=300,400    #窗口大小
way_to_create=1         #球体产生方法  1为单击生成正六边形块
r=3
ball_create=0
#click_allow=1          #下次按键是否有效？
particlepos=[]
bottom_particlepos=[]
particlelist=[]
pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('粒子块下落')
clock=pygame.time.Clock()

#向量运算函数
def magenititude(vector):                       #(01)求模长
    return (vector[0]**2+vector[1]**2)**0.5
def times(vector,h):                            #(03)相乘
    return [vector[0]*h,vector[1]*h]
def plus(vector1,vector2):                      #(05)向量相加
    return [vector1[0]+vector2[0],vector1[1]+vector2[1]]
def minus(vector1,vector2):                     #(06)向量相减
    return [vector1[0]-vector2[0],vector1[1]-vector2[1]]
def dot_product(vector1,vector2):               #(07)向量点乘
    return (vector1[0]*vector2[0]+vector1[1]*vector2[1])
def angle_180(vector1,vector2,radian=0):        #(09)求夹角0-180
    mag_a=magenititude(vector1)
    mag_b=magenititude(vector2)
    if mag_a*mag_b==0:
        return 'Error! zero vector detected'
    else:
        degree=dot_product(vector1,vector2)/mag_a/mag_b
        degree=math.acos(degree)
        if radian==0:
            degree=degree/math.pi*180
        return degree
def angle_to_horizontal(vector,radian=0):       #(10)求与向量(1,0)的夹角，0-360  radian=1输出弧度制
    if vector[0]==0 and vector[1]==0:
        return 'Error! zero vector detected'
    else:
        a=angle_180(vector,(1,0))
        b=angle_180(vector,(0,1))
        if (a<=90 and b<=90) or (a>90 and b<=90):
            degree=a
        elif (a>90 and b>90) or (a<=90 and b>90):
            degree=360-a
        if radian==1:
            degree=degree/180*math.pi
        return degree
def rotate_CCS(vector,degree,radian=0):         #(13)旋转坐标系 
    if radian==0:
        degree=degree/180*math.pi
    a=+vector[0]*math.cos(degree)+vector[1]*math.sin(degree)
    b=-vector[0]*math.sin(degree)+vector[1]*math.cos(degree)
    return [a,b]


#定义粒子类（坐标，速度，半径，颜色）
class particles(object):
    def __init__(self,pos,vel,radius,color):
        self.pos=pos
        self.vel=vel
        self.color=color
        self.radius=radius
        self.id=len(particlelist)+1
        self.acce=[0,2000]
        self.tracks=[]
        particlelist.append(self)

    #位移、速度、加速度函数
    def positioncompute(self):                              #位移计算函数
        self.pos=plus(times(self.vel,time_pass),self.pos)
    def velocitycompute(self):                              #速度计算函数
        self.vel=plus(times(self.acce,time_pass),self.vel)
    def acceleratecompute(self):                            #速度耗散？
        self.acce=plus(times(self.vel,0),[0,1000])
    
    def knock(self):                                        #边界碰撞检测，触壁则修正圆心位置，速度暂时取反
        if self.pos[0]+self.vel[0]*time_pass>=width-self.radius:
            self.pos[0]=width-self.radius                   #修正小球圆心位置
            self.vel[0]=-self.vel[0]                         #触壁速度取反
        elif self.pos[0]+self.vel[0]*time_pass<=self.radius:
            self.pos[0]=self.radius         
            self.vel[0]=-self.vel[0]
        elif self.pos[1]>=height-self.radius:  
            self.pos[1]=height-self.radius   
            self.vel[1]=-self.vel[1]
        elif self.pos[1]+self.vel[1]*time_pass<=self.radius:
            self.pos[1]=self.radius               
            self.vel[1]=-self.vel[1]

        for i in particlelist[self.id::]:   #与其他球体的碰撞检测
            if i==self:
                continue
            distance_vec=minus(self.pos,i.pos)
            distance=magenititude(distance_vec)
            if distance<=self.radius+i.radius:
                self.vel[1]=-self.vel[1]   
                i.vel[1]=-i.vel[1]
                distance_vec[1]=-distance_vec[1]                    #将差向量纵坐标取反，从而转化为普通右手系
                degree=float(angle_to_horizontal(distance_vec))     #得到与水平横轴正方向夹角，角度值
                new_self_vel=rotate_CCS(self.vel,degree)
                new_i_vel=rotate_CCS(i.vel,degree)
                new_self_vel[0],new_i_vel[0]=new_i_vel[0],new_self_vel[0]    #连心线方向速度交换，另一方向速度不变
                self.vel=rotate_CCS(new_self_vel,0-degree)
                i.vel=rotate_CCS(new_i_vel,0-degree)
                self.vel[1]=-self.vel[1]
                i.vel[1]=-i.vel[1]   #将两球速度、距离向量转化为左手系

    def display(self):
        self.knock()
        self.acceleratecompute()
        self.velocitycompute()
        self.positioncompute()
        pygame.draw.circle(screen,self.color,list(map(round,self.pos)),self.radius)

#生成粒子块
while True:                                               #持续循环
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    

    time_pass=clock.tick()/1000
    pressed_mouse=pygame.mouse.get_pressed()                #鼠标状态

    if  pressed_mouse[1]==1:                                #中键清空所有球
        particlelist=[]

    elif  pressed_mouse[0]==1 and ball_create==0:                              
        startpoint=list(pygame.mouse.get_pos())    
        pygame.draw.circle(screen,(0,0,255),startpoint,r)   #显示将要生成的粒子位置
        ball_create=1

    elif  pressed_mouse[0]==0 and ball_create==1:           #生成运动实体
        particles(startpoint,[0,0],r,(0,0,255))
        ball_create=0

    for i in particlelist:
        i.display()

    pygame.display.update()                                            #更新页面
