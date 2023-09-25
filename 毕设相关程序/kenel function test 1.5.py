#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math,time
from random import randint
from pygame.locals import *
from vectorcalculate import *

#以下为调试用参数  
draw_tem=0                                          #是否绘制温度分布图  1为是 0为否
kenel_function_choose=3                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel 
width,height=800,600                                #窗口大小  应设为40的倍数  鉴于网格宽度为40像素
circle_radius_multi=2.5                             #绘制圆形半径与网格宽度的比率  应设置为大于2.5
grid_width=20                                       #网格宽度
gap=5                                               #图像分辨率
draw_screen=1                                       #绘制图像专用
alpha_D1 = 5/3.1415/2.55#/h**2                      #此处参数因根据实际情况进行调试 这三个值需要根据光滑长度进行调整
alpha_D2 = 15/7/3.1415*5.6#/h**2                    #部分数据红皮书与学姐论文不相符，需自行调试
alpha_D3 = alpha_D2*3/2

def f(x):                                           #图像生成函数
    y=250*math.cos(x/200*3.14159)
    return y


grid_list=[]                                        #用于储存网格左上顶点坐标       元素为 列表 坐标 
ball_list=[]                                        #用于储存所有粒子              元素为 粒子
balls_in_grid_list=[]                               #用于储存各个格子中的粒子       元素为 列表，列表内为粒子id
dots_within_domain=[]                               #用于储存处于影响域内的粒子     元素为 数字，粒子id
smooth_length=grid_width*circle_radius_multi        #光滑长度


pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('Kenel Function Test')


class balls(object):
    def __init__(self,pos,tem,color=(255,255,255)):
        self.pos=pos                                #位置   需即时更新
        self.radius=2                               #半径          
        self.tem=1                                  #暂时无用
        self.id=len(ball_list)                      #以ball_list的长度作为id    不需更新
        self.in_grid=[self.pos[0]-self.pos[0]%grid_width,self.pos[1]-self.pos[1]%grid_width]
        ball_list.append(self)
        balls_in_grid_list[grid_list.index(self.in_grid)].append(self.id)       #使其所在的格子中记录自己的id  


def generate_grids():                               #网格生成函数   
    x,y=0,0
    while y<height+grid_width:                      #生成网格并记录左上角顶点坐标
        while x<width+grid_width:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=grid_width
        y+=grid_width
        x=0
def generate_dots():                                #根据函数绘制各种图形
    time_pass=clock.tick()/1000  
    x,n=0,0                                         #以屏幕最左侧中点为原点
    while x<=width:                                 #x到最右侧截止
        top=height/2-f(x)+f(x)%gap                  #由于pygame坐标系反了，这里函数值要做减法
        y=height
        while y>=0 and y>=top and y<=height:
            balls((x,y),n)
            n+=1
            y-=gap
        x+=gap
    time_pass=clock.tick()/1000  
    print('生成粒子%5d个，共用时%.4f秒'%(len(ball_list),time_pass))


def norma_kenel(X,X1,h):                            #核函数，待测试
    q=magenititude(minus(X,X1))/h

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
 
def nabla_kenel(X,X1,h):                            #结果为向量
    q=magenititude(minus(X,X1))/h

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
 
def lapla_kenel(X,X1,h):                            #二次偏导
    q=magenititude(minus(X,X1))/h

    if kenel_function_choose==0:                    # 1
        if q>1:
            return '0'
        else:
            return 0  

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:                                    
            return '0'
        else:
            return (3/q-9*q-48*q**2)*alpha_D1

    if kenel_function_choose==2:                    # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:  
            return (9/2*q-4)*alpha_D2
        elif q<=2:
            return (-3/2*q-2/q+4)*alpha_D2
        else:
            return '0'

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:  
            return (9/2*q-4)*alpha_D3
        elif q<=2:
            return (-3/2*q-2/q+4)*alpha_D3
        else:
            return '0'


def calculate_kenel(mouse_pos):
    num_within_domain=0                             #影响域圆内粒子数量
    dots_within_domain=[]                           #影响域方框内粒子id
    dots_within_domain_circle=[]                    #影响域圆内粒子id

    final_tem=0                                     #温度
    gradient=[0,0]                                  #梯度
    curvature=0                                     #曲率
    Csi=0

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
        pygame.draw.circle(screen,(255,0,0),ball_list[i].pos,3)                 #红色标出 影响域方框 内粒子
        norma_kenel_result = norma_kenel(mouse_pos,ball_list[i].pos,smooth_length)
        if norma_kenel_result=='0' or ball_list[i].pos==mouse_pos:              #用于判定粒子是否处于影响域圆   
            continue
        else:
            pygame.draw.circle(screen,(0,255,0),ball_list[i].pos,5)             #绿色标出 影响域圆 内粒子
            dots_within_domain_circle.append(i)                                 #记录影响域圆内的粒子id
            Csi+=norma_kenel_result

    num_within_domain = len(dots_within_domain_circle)                          #计算影响圆内粒子数量       
    if num_within_domain  != 0:
        Csi/=num_within_domain
        Csi-=1
    else:
        return [0,0],0,0                                                        #若影响域内粒子数量为零，则提前跳出函数

        
    for i in dots_within_domain_circle:                                         #仅对存在于影响域内的粒子进行计算
        norma_kenel_result = norma_kenel(mouse_pos,ball_list[i].pos,smooth_length)
        nabla_kenel_result = nabla_kenel(mouse_pos,ball_list[i].pos,smooth_length)

        vector=minus(mouse_pos,ball_list[i].pos)                                #这两行是用于计算曲率
        curvature += 2 * Csi* dot_product(vector,nabla_kenel_result)/magenititude_simple(vector)  
        final_tem += ball_list[i].tem * norma_kenel_result                      #温度叠加
        gradient=plus(gradient,nabla_kenel_result)                              #梯度叠加

    gradient=divide(gradient,num_within_domain)
    final_tem/=num_within_domain
    curvature/=num_within_domain
    #pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,gradient),5) #划线,直接画出梯度
    #pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,normalize(times( gradient,-curvature ),100) ),5)     #划线
    pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,times(gradient,-curvature)),5)
    return gradient,final_tem,curvature


def nearest_dot_tem(mouse_pos):                     #找到距离鼠标最近点的温度
    mouse_pos=pygame.mouse.get_pos()
    mouse_in_grid=[mouse_pos[0]-mouse_pos[0]%grid_width,mouse_pos[1]-mouse_pos[1]%grid_width]
    try:
        a=grid_list.index(mouse_in_grid)
    except ValueError:
        pass
    else:
        distance=1000000
        show_id=0
        for i in balls_in_grid_list[a]:             #找出这一格内距离鼠标最近的点
            n=magenititude(minus(ball_list[i].pos,mouse_pos))
            if distance>n:
                distance=n
                show_id=i
        tem_show=ball_list[show_id].tem             #显示该点温度
        tem_show=pygame.font.Font('freesansbold.ttf',20).render(str(tem_show),1,(0,200,200))
        screen.blit(tem_show,ball_list[show_id].pos)


def shift_color(m):
    if m<128:
        r=0
        g=2*m
        b=255-m*2   
    else:
        r=2*m-255
        g=511-2*m
        b=0
    color=(r, g, b)
    return color
def draw_tem_profile():                             #绘制温度分布图
    m,n,x,y=0,0,0,0                                 #n为当前点的值,m为实际最大值
    limit_change=0
    max=1.56
    min=-2.12
    delta=max-min
    tem_color=pygame.Surface((width,height),24)     #创建一张图片，用于填色
    clock=pygame.time.Clock()
    if draw_screen==1:
        while y<height:                             #计算每个坐标的温度，然后绘制为背景
            while x<width:
                #n=calculate_kenel((x,y))[0]            #温度
                #n=magenititude(calculate_kenel((x,y))[1])
                n=calculate_kenel((x,y))[2]
                m=int((n-min)/delta*255)
                color=shift_color(m)
                try:
                    tem_color.set_at((x,y), color)  #利用错误重新定义上下限
                except TypeError:
                    if n<min:                           #下限直接取整
                        min=n
                    if n>max:                           #上限取整后加一
                        max=n
                    delta=max-min                       #上下限改变后重新计算两者差值
                    limit_change=1
                    continue 
                x+=1
            print('已完成%d%%'%(100*y/height))
            y+=1
            x=0
    elif draw_screen==2:
        for i in ball_list:
            #n=calculate_kenel(i.pos)[0]            #温度
            #n=magenititude(calculate_kenel(i.pos)[1])
            n=calculate_kenel(i.pos)[2]

            m=int((n-min)/delta*255)
            color=shift_color(m)
            try:
                tem_color.set_at(i.pos, (color))  #利用错误重新定义上下限
            except TypeError:
                if n<min:                           #下限直接取整
                    min=n
                if n>max:                           #上限取整后加一
                    max=n
                delta=max-min                       #上下限改变后重新计算两者差值
                limit_change=1
                continue 

            if i.id%100==0:
                print('已完成%.2f%%'%(100*i.id/len(ball_list)))
    
    localtime = (time.strftime("%m-%d %H..%M", time.localtime()))
    if limit_change==1:
        profile_name=str(localtime)+'  ('+str(min)+'~'+str(max)+')  '+'上下限不准确'+".png"
    else:
        profile_name=str(localtime)+'  ('+str(min)+'~'+str(max)+')  '+'上下限准确'+".png"
    pygame.image.save(tem_color,profile_name)       #时间+上下限范围+是否改动了上下限
    time_pass=clock.tick()/1000
    print('上下限范围为 %d~%d '%(min,max))
    print('共用时%.2fs'%time_pass)
    exit()


generate_grids()
generate_dots()
#draw_tem_profile()
while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    for i in ball_list:                             #绘出粒子
        pygame.draw.circle(screen,(255,255,255),(int(i.pos[0]),int(i.pos[1])),i.radius)
        
    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    if pressed_mouse[0]==1: 
        print(calculate_kenel(mouse_pos))

    nearest_dot_tem(mouse_pos)

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))
    screen.blit(mouse_pos_show,(0,0))                                           #显示当前鼠标位置

    pygame.draw.circle(screen,(255,255,255),mouse_pos,int(smooth_length),1)     # smooth_length 的网格间距画圆
    pygame.display.update()


#验证了光滑函数求偏导的可行性，第一核函数完全可行，下一步验证不规则粒子分布情况下是否仍然成立
#第一个核函数一直怀疑其准确性，日后都应使用2，3核函数
#由于程序模拟并未考虑与实际长度单位进行联系，所以h，h**2等运算需要自己处理数值
#v1.2  添加了求垂直于液面的向量的函数，目前运行良好，下一步添加判定其到底位于液面还是液内的函数，在下一步添加表面张力，设法合并两个函数
#v1.4  添加了表面张力的计算，测试运行良好。下一步根据q值进行液面粒子和液体内部粒子判定，再将其整合到主函数中。
#v1.5  完善了部分计算，应该可以添加进主函数了，但未添加判断粒子是否处于表面的函数