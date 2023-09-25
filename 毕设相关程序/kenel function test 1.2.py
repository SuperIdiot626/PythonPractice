#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random import randint
from pygame.locals import *
from vectorcalculate import *

#以下为调试用参数  
draw_tem=0                                          #是否绘制温度分布图  1为是 0为否
kenel_function_choose=2                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel 
width,height=800,600                                #窗口大小  应设为40的倍数  鉴于网格宽度为40像素
circle_radius_multi=2                               #绘制圆形半径与网格宽度的比率  应设置为大于2.5
grid_width=50                                       #网格宽度
gap=5                                               #图像分辨率

def f(x):                                           #图像生成函数
    y=200*math.cos(x/400*3.14159)
    return y


grid_list=[]                                        #用于储存网格左上顶点坐标       元素为 列表 坐标 
ball_list=[]                                        #用于储存所有粒子              元素为 粒子
balls_in_grid_list=[]                               #用于储存各个格子中的粒子       元素为 列表，列表内为粒子id
dots_within_domain=[]                               #用于储存处于影响域内的粒子     元素为 数字，粒子id
smooth_length=grid_width*circle_radius_multi        #光滑长度


pygame.init()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('Kenel Function Test')


class balls(object):
    def __init__(self,pos,tem,color=(255,255,255)):
        self.pos=pos                                #位置   需即时更新
        self.radius=0                               #半径          
        self.tem=tem                                #暂时无用
        self.id=len(ball_list)                      #以ball_list的长度作为id    不需更新
        self.in_grid=[self.pos[0]-self.pos[0]%grid_width,self.pos[1]-self.pos[1]%grid_width]
        ball_list.append(self)
        balls_in_grid_list[grid_list.index(self.in_grid)].append(self.id)       #使其所在的格子中记录自己的id  


def generate_dots_pit():                            #根据函数绘制各种图形
    x,n=0,0                                         #以屏幕最左侧中点为原点
    while x<=width:                                 #x到最右侧截止
        top=height/2-f(x)+f(x)%gap                  #由于pygame坐标系反了，这里函数值要做减法
        y=height
        while y>=0 and y>=top and y<=height:
            balls((x,y),n)
            n+=1
            y-=gap
        x+=gap


def kenel_function(X,X1,h):                         #核函数，待测试
    q=magenititude(minus(X,X1))/h

    alpha_D1 = 5/3.1415/2.55#/h**2                  #此处参数因根据实际情况进行调试
    alpha_D2 = 15/7/3.1415*12.5#/h**2               #部分数据红皮书与学姐论文不相符，需自行调试
    alpha_D3 = 15/7/3.1415*9#/h**2

    if kenel_function_choose==0:                    # 1
        if q>1:
            return '0'
        else:
            return 1   

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:
            return '0'
        else:
            return  alpha_D1*(1+3*q-q**3-3*q**4)

    if kenel_function_choose==2:                    # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:
            return alpha_D2*(2/3-q**2+q**3/2)
        elif q<=2:
            return alpha_D2*(2-q)**3/6
        else:
            return '0'

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:
            return alpha_D3*(2/3-q**2+q**3/2)*3/2
        elif q<=2:
            return alpha_D3*(2-q)**3/4
        else:
            return '0'
 

def delta_kenel(X,X1,h):                            #结果为向量
    q=magenititude(minus(X,X1))/h

    alpha_D1 = 5/3.1415/2.55#/h**2                  #此处参数因根据实际情况进行调试
    alpha_D2 = 15/7/3.1415*12.5#/h**2
    alpha_D3 = 15/7/3.1415*9#/h**2

    if kenel_function_choose==0:                    # 1
        if q>1:
            return '0'
        else:
            return (0,0)  

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:
            return '0'
        else:
            a=(3-3*q**2-12*q**3)/q 
            return  times(minus(X,X1),alpha_D1*a)

    if kenel_function_choose==2:                    # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:            
            return times(minus(X,X1),alpha_D1*(-2+3/2*q))
        elif q<=2:
            return times(minus(X,X1),alpha_D2*(-(2-q)**2)/2/q )
        else:
            return '0'

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:
            return times(minus(X,X1),alpha_D3*(-2+3/2*q)*3/2)
        elif q<=2:
            return times(minus(X,X1),alpha_D3*(-(2-q)**2)/q*3/4)
        else:
            return '0'
 

def calculate_tem(mouse_pos):
    num_within_domain=0                             #最终影响域圆内粒子数量
    final_tem=0                                     #最终温度
    dots_within_domain=[]                           #影响域大方框内粒子id

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]            #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]           #影响域方框右下角坐标
    left_top=times( quotient(left_top,(grid_width,grid_width) ),grid_width)     #取左上角的左上的格子顶点
    right_bot=times(quotient(right_bot,(grid_width,grid_width)),grid_width)     #取右下角的左上的格子顶点
                  
    y=left_top[1]
    while y<=right_bot[1]:                          #找出影响域方框内的点
        x=left_top[0]
        while x<=right_bot[0]:            
            try :                
                a=grid_list.index([x,y])            #如果(x,y)在pos_list中
            except ValueError:
                x+=grid_width                    
                continue
            else:
                dots_within_domain+=balls_in_grid_list[a]                       #将粒子id添加入内
                x+=grid_width
        y+=grid_width

    for i in dots_within_domain:
        pygame.draw.circle(screen,(255,0,0),ball_list[i].pos,5)                 #红色标出 影响域方框 内粒子
        kenel_function_result = kenel_function(mouse_pos,ball_list[i].pos,smooth_length)
        if kenel_function_result=='0':                                          #用于判定粒子是否处于影响域圆   
            continue
        num_within_domain+=1 
        pygame.draw.circle(screen,(0,255,0),ball_list[i].pos,10)                #绿色标出 影响域圆 内粒子
        final_tem += ball_list[i].tem * kenel_function_result
    final_tem/=num_within_domain
    print(final_tem,mouse_pos)                                                  #程序批量调试时请注释此行
    return int(final_tem)


def calculate_gradient(mouse_pos):
    num_within_domain=0                             #最终影响域圆内粒子数量
    gradient=[0,0]                                  #最终梯度
    dots_within_domain=[]                           #影响域方框内粒子坐标

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]            #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]           #影响域方框右下角坐标
    left_top=times( quotient(left_top,(grid_width,grid_width) ),grid_width)     #取左上角的左上的格子顶点
    right_bot=times(quotient(right_bot,(grid_width,grid_width)),grid_width)     #取右下角的左上的格子顶点
                  
    y=left_top[1]
    while y<=right_bot[1]:                          #找出影响域方框内的点
        x=left_top[0]
        while x<=right_bot[0]:            
            try :                
                a=grid_list.index([x,y])            #如果(x,y)在pos_list中
            except ValueError:
                x+=grid_width                    
                continue
            else:
                dots_within_domain+=balls_in_grid_list[a]                       #将粒子id添加入内
                x+=grid_width
        y+=grid_width

    for i in dots_within_domain:
        pygame.draw.circle(screen,(255,0,0),ball_list[i].pos,5)                 #红色标出 影响域方框 内粒子
        delta_kenel_result = delta_kenel(mouse_pos,ball_list[i].pos,smooth_length)
        if delta_kenel_result=='0':                                             #用于判定粒子是否处于影响域圆   
            continue
        num_within_domain+=1   
        pygame.draw.circle(screen,(0,255,0),ball_list[i].pos,10)                #绿色标出 影响域圆 内粒子
        gradient=plus(gradient,delta_kenel_result)
    print(gradient,mouse_pos)                                                   #程序批量调试时请注释此行
    try:
        pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,normalize(gradient,100)),5)      #划线
    except ZeroDivisionError:
        pass
    return gradient


def nearest_dot_tem(mouse_pos):                     #找到距离鼠标最近点的温度
    mouse_pos=pygame.mouse.get_pos()
    mouse_in_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]
    try:
        a=grid_list.index(mouse_in_grid)
    except ValueError:
        pass
    else:
        distance=100
        show_id=0
        for i in balls_in_grid_list[a]:             #找出这一格内距离鼠标最近的点
            n=magenititude(minus(ball_list[i].pos,mouse_pos))
            if distance>n:
                distance=n
                show_id=i
        tem_show=ball_list[show_id].tem             #显示该点温度
        tem_show=pygame.font.Font('freesansbold.ttf',20).render(str(tem_show),1,(200,200,200))
        screen.blit(tem_show,ball_list[show_id].pos)


def generate_grids():                               #网格生成函数   
    x,y=0,0
    while y<height+grid_width:                      #生成网格并记录左上角顶点坐标
        while x<width+grid_width:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=grid_width
        y+=grid_width
        x=0
generate_grids()

def draw_tem_profile():                             #绘制温度分布图
    clock=pygame.time.Clock()

    x,y=width-grid_width,height-grid_width
    max_tem=0
    while y<height:                                 #计算右下角格的最高温度作为参考，并输出
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
    while y<height:                                 #计算每个坐标的温度，然后绘制为背景
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
    pygame.image.save(tem_color,tem_profile_name)   #核函数序号+alphaD+最高温度+坐标+间距乘数
    time_pass=clock.tick()/1000
    print('最高温度为%.2f'%max_tem)
    print('共用时%.2f'%time_pass)

generate_dots_pit()
while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    for i in ball_list:                             #绘出网格点
        pygame.draw.circle(screen,(255,255,255),(int(i.pos[0]),int(i.pos[1])),2)
        
    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    
    if pressed_mouse[0]==1: 
        #calculate_tem(mouse_pos)
        calculate_gradient(mouse_pos)
    
    '''
    nearest_dot_tem(mouse_pos)
    '''
    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))
    screen.blit(mouse_pos_show,(0,0))                                           #显示当前鼠标位置

    pygame.draw.circle(screen,(255,255,255),mouse_pos,int(smooth_length),1)     # smooth_length 的网格间距画圆

    
    
    pygame.display.update()


#验证了光滑函数求偏导的可行性，第一核函数完全可行，下一步验证不规则粒子分布情况下是否仍然成立
#第一个核函数一直怀疑其准确性，日后都应使用2，3核函数
#由于程序模拟并未考虑与实际长度单位进行联系，所以h，h**2等运算需要自己处理数值
#v1.2  添加了求垂直于液面的向量的函数，目前运行良好，下一步添加判定其到底位于液面还是液内的函数，在下一步添加表面张力，设法合并两个函数