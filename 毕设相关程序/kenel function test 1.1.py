#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *
from vectorcalculate import *

#以下为调试用参数  
draw_tem=0                                          #是否绘制温度分布图  1为是 0为否
kenel_function_choose=1                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel 
width,height=760,600                                #窗口大小  应设为40的倍数  鉴于网格宽度为40像素
circle_radius_multi=2.5                             #绘制圆形半径与网格宽度的比率  应设置为大于2.5
grid_width=40                                       #网格宽度
smooth_length=grid_width*circle_radius_multi        #光滑长度

pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('Kenel Function Test')
clock=pygame.time.Clock()

#在屏幕上生成网格，且为每个点设置随机温度
pos_list=[]
tem_list=[]
x,y=0,280                   #若要一般有粒子一般没有，y值应小心设置
n=0
while y<=height:           #绘制网点
    while x<=width:
        pos_list.append( (x,y) )
        tem_list.append(n)
        n+=1
        x+=grid_width
    y+=grid_width
    x=0


def kenel_function(X,X1,h):                 #核函数，待测试
    q=magenititude(minus(X,X1))/h

    alpha_D1 = 5/3.1415/2.55#/h**2            #此处参数因根据实际情况进行调试
    alpha_D2 = 15/7/3.1415*12.5#/h**2
    alpha_D3 = 15/7/3.1415*9#/h**2

    if kenel_function_choose==0:            # 1
        if q>1:
            return '0'
        else:
            return 1   

    if kenel_function_choose==1:            # Lucy’s Quartic Kernel
        if q>1:
            return '0'
        else:
            return  alpha_D1*(1+3*q-q**3-3*q**4)

    if kenel_function_choose==2:            # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:
            return alpha_D2*(2/3-q**2+q**3/2)
        elif q<=2:
            return alpha_D2*(2-q)**3/6
        else:
            return '0'

    if kenel_function_choose==3:            # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:
            return alpha_D3*(2/3-q**2+q**3/2)/2*3
        elif q<=2:
            return alpha_D3*(2-q)**3/4
        else:
            return '0'
 

def delta_kenel(X,X1,h):                    #结果为向量
    q=magenititude(minus(X,X1))/h

    alpha_D1 = 5/3.1415/2.55#/h**2            #此处参数因根据实际情况进行调试
    alpha_D2 = 15/7/3.1415*12.5#/h**2
    alpha_D3 = 15/7/3.1415*9#/h**2

    if kenel_function_choose==0:            # 1
        if q>1:
            return '0'
        else:
            return (0,0)  

    if kenel_function_choose==1:            # Lucy’s Quartic Kernel
        if q>1:
            return '0'
        else:
            a=(3-3*q**2-12*q**3)/q 
            vector=minus(X,X1)
            return  times(vector,alpha_D1*a)






def nearest_dot_tem(mouse_pos):                                 #找到距离鼠标最近点的温度
    mouse_pos=pygame.mouse.get_pos()
    mouse_grid_potential_1=(mouse_pos[0]//grid_width*grid_width,mouse_pos[1]//grid_width*grid_width)        #左上
    mouse_grid_potential_2=(mouse_grid_potential_1[0]+grid_width,mouse_grid_potential_1[1])                 #右上
    mouse_grid_potential_3=(mouse_grid_potential_1[0],mouse_grid_potential_1[1]+grid_width)                 #左下
    mouse_grid_potential_4=(mouse_grid_potential_1[0]+grid_width,mouse_grid_potential_1[1]+grid_width)      #右下
    mouse_grid_poslist=[mouse_grid_potential_1,mouse_grid_potential_2,mouse_grid_potential_3,mouse_grid_potential_4]#形成列表
    distance_list=[]

    for i in mouse_grid_poslist:                                #计算鼠标位置与最近四个点的距离
        distance_list.append(magenititude_simple(minus(mouse_pos,i)))
    i=distance_list.index(min(distance_list))                   #找出最近的点位
    mouse_grid_pos=mouse_grid_poslist[i]
    try:                                                        #将周围格子的id添加入列表
        tem_show=tem_list[pos_list.index(mouse_grid_pos)] 
    except ValueError:
        pass
    else:
        tem_show=tem_list[pos_list.index(mouse_grid_pos)]           #显示该点温度
        tem_show=pygame.font.Font('freesansbold.ttf',20).render(str(tem_show),1,(200,200,200))
        screen.blit(tem_show,mouse_grid_pos)


def calculate_tem(mouse_pos):
    num_within_domain=0                     #最终影响域圆内粒子数量
    final_tem=0                             #最终温度
    dots_pos_within_domain=[]               #影响域方框内粒子坐标

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]          #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]         #影响域方框右下角坐标
    left_top=times(  plus(  quotient(  left_top,(grid_width,grid_width)  ),(1,1)  )  ,  grid_width  )           #取其左上的点
    right_bot=times(quotient(right_bot,(grid_width,grid_width)),grid_width)                                     #取其右下的点
                  
    y=int(left_top[1])
    while y<=right_bot[1]:              #找出影响域方框内的点
        x=int(left_top[0]) 
        while x<=right_bot[0]:            
            try :                
                pos_list.index((x,y))   #如果(x,y)在pos_list中
            except ValueError:
                x+=grid_width                    
                continue
            else:
                dots_pos_within_domain.append( (x,y) )       
                x+=grid_width
        y+=grid_width

    for i in dots_pos_within_domain:
        if i in pos_list:
            pygame.draw.circle(screen,(255,0,0),i,5)            #红色标出 影响域方框 内粒子
            kenel_function_result = kenel_function(mouse_pos,i,smooth_length)
            if kenel_function_result=='0':                      #用于判定粒子是否处于影响域圆   
                continue
            num_within_domain+=1   
            pygame.draw.circle(screen,(0,255,0),i,10)           #绿色标出 影响域圆 内粒子
            final_tem += tem_list[pos_list.index(i)] * kenel_function_result
    final_tem/=num_within_domain
    #print(final_tem,mouse_pos)                                  #程序批量调试时请注释此行
    return int(final_tem)


def calculate_gradient(mouse_pos):
    num_within_domain=0                     #最终影响域圆内粒子数量
    gradient=[0,0]                          #最终温度
    dots_pos_within_domain=[]               #影响域方框内粒子坐标

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]          #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]         #影响域方框右下角坐标
    left_top=times(  plus(  quotient(  left_top,(grid_width,grid_width)  ),(1,1)  )  ,  grid_width  )           #取其左上的点
    right_bot=times(quotient(right_bot,(grid_width,grid_width)),grid_width)                                     #取其右下的点
                  
    y=int(left_top[1])
    while y<=right_bot[1]:              #找出影响域方框内的点
        x=int(left_top[0]) 
        while x<=right_bot[0]:            
            try :                
                pos_list.index((x,y))   #如果(x,y)在pos_list中
            except ValueError:
                x+=grid_width                    
                continue
            else:
                dots_pos_within_domain.append( (x,y) )       
                x+=grid_width
        y+=grid_width

    for i in dots_pos_within_domain:
        if i in pos_list:
            pygame.draw.circle(screen,(255,0,0),i,5)            #红色标出 影响域方框 内粒子
            delta_kenel_result = delta_kenel(mouse_pos,i,smooth_length)
            if delta_kenel_result=='0':                         #用于判定粒子是否处于影响域圆   
                continue
            num_within_domain+=1   
            pygame.draw.circle(screen,(0,255,0),i,10)           #绿色标出 影响域圆 内粒子
            gradient=plus(gradient,delta_kenel_result)
    #print(gradient,mouse_pos)                                   #程序批量调试时请注释此行
    pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,normalize(gradient,50)),5)      #划线
    return gradient


def draw_tem_profile():     #绘制温度分布图

    clock=pygame.time.Clock()
    x,y=width-grid_width,height-grid_width
    max_tem=0
    while y<height:           #计算右下角格的最高温度作为参考，并输出
        while x<width:
            n=calculate_tem((x,y))
            if max_tem<=n:
                max_tem=n
            x+=1
        y+=1
        x=width-grid_width
    max_tem+=1

    x,y=0,0
    n=0
    tem_color=pygame.Surface((width,height),depth=24)
    while y<height:           #计算每个坐标的温度，然后绘制为背景
        while x<width:
            n=calculate_tem((x,y))
            n=int(n/(max_tem)*255)
            if n<128:
                r=0
                g=2*n
                b=255-n*2   
            else:
                r=2*n-255
                g=511-2*n
                b=0
            x+=1
            tem_color.set_at((x,y), (r, g, b))
        print('已完成%%%d'%(100*y/height))
        y+=1
        x=0
    tem_profile_name=str(kenel_function_choose)+'+'+str(max_tem)+'+'+str(circle_radius_multi)+".png"
    pygame.image.save(tem_color,tem_profile_name)       #核函数序号+alphaD+最高温度+坐标+间距乘数
    time_pass=clock.tick()/1000
    print('最高温度为%.2f'%max_tem)
    print('共用时%.2f'%time_pass)


if draw_tem==1:
    draw_tem_profile()
'''
while kenel_function_choose<=3:
    while circle_radius_multi<=5:
        draw_tem_profile()
        circle_radius_multi+=0.5
        print(circle_radius_multi,kenel_function_choose)
    circle_radius_multi=2.5
    kenel_function_choose+=1
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
        calculate_gradient(mouse_pos)

    nearest_dot_tem(mouse_pos)

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))
    screen.blit(mouse_pos_show,(0,0))                               #显示当前鼠标位置

    pygame.draw.circle(screen,(255,255,255),mouse_pos,int(smooth_length),1)        # smooth_length 的网格间距画圆

    for i in pos_list:  #绘出网格点
        pygame.draw.circle(screen,(255,255,255),i,2)
    
    pygame.display.update()

#验证了光滑函数求偏导的可行性，第一核函数完全可行，下一步验证不规则粒子分布情况下是否仍然成立