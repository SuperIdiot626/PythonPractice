#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *


width,height=800,600            #界面的长宽
smooth_length=50                #光滑长度
miu=-2.0                        #运动中的阻力项
renew_freq=5                    #刷新间隔帧数，最小为1
check=1                         #是否追随粒子，并进行检测
how_to_cal=2                    #1为欧拉法，2为蛙跳法
gravity=[0,1000]                 #调整重力的大小及方向
ball_radius=2                   #粒子半径

grid_list=[]                    #用于储存网格左上顶点坐标     元素为 列表 坐标 
ball_list=[]                    #用于储存所有粒子            元素为 粒子
balls_in_grid_list=[]           #用于储存各个格子中的粒子     元素为 列表，列表内为粒子id
check_id=300                    #目前所查看粒子的id
key_press_allow=1               #是否允许下次按键输入
renew_ready=0                   #用于计算部分数据是否应该刷新


pygame.init()
clock=pygame.time.Clock()       #用于计时
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('New Try of SPH')


class balls(object):
    def __init__(self,pos,vel,tem,color):
        self.pos=pos                                #位置   需即时更新
        self.vel=vel                                #速度   需即时更新
        self.acce=[0,0]                             #加速度 需即时更新
        self.radius=ball_radius                     #半径          
        self.tem=tem                                #暂时无用
        self.color=color
        self.id=len(ball_list)                      #以ball_list的长度作为id    不需更新
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          #储存临近格子的id   不需即时更新
        self.near_dots=[]                           #储存临近粒子的id   不需即时更新
        self.first_cal=1                            #蛙跳算法的第一次运算检测
        ball_list.append(self)
        balls_in_grid_list[grid_list.index(self.in_grid)].append(self.id)       #使其所在的格子中记录自己的id   

    def find_near_grids_dots(self):                 #找到其所在格周围的格子 与 粒子
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          #每次调用次函数需将本来的 相邻格子 数据清空
        self.near_dots=[]                           #每次调用次函数需将本来的 相邻粒子 数据清空
        x=-1
        y=-1
        while y<=1:
            while x<=1:                             #利用异常处理了边界格子
                try:                                #将周围格子的id添加入列表
                    n=grid_list.index([self.in_grid[0]+x*smooth_length,self.in_grid[1]+y*smooth_length])
                except ValueError:
                    x+=1
                    continue
                else:
                    x+=1
                    self.near_grids.append(n)                                   #相邻格子id加入列表
                    self.near_dots+=balls_in_grid_list[n]                       #利用格子id查找格子，直接使用list加法得出结果
            x=-1
            y+=1

    def acce_compute(self):
        self.acce=[0,0]                             #先将原来的加速度清零
        n=1
        if n==1:                                    #重力加速度、空气阻力只算一次
            self.acce=plus(self.acce,gravity)
            self.acce=plus(self.acce,times(self.vel,miu))
            n=0

        for i in self.near_dots:
            if i==self.id:                          #与自己的吸引力计算检测直接跳过
                continue
            i=ball_list[i]
            distance_vec=minus(self.pos,i.pos)      
            distance=magenititude(distance_vec)     # minus 为吸引，plus为排斥
            if distance<=0.05*smooth_length:        #粒子间距过近为斥力 
                a=times(distance_vec, 1000*distance**(-2))
                self.acce=plus(self.acce,a)        
            if distance<=smooth_length:             #粒子间距较远为引力 
                a=times(distance_vec, 1000*distance**(-2))
                self.acce=minus(self.acce,a)        

    def new_pos_vel(self):
        
        self.acce_compute()                                                     #不论哪种方法，先计算加速度

        if   how_to_cal==1:                                                     #欧拉积分方法，
            self.vel=plus(times(self.acce,time_pass),self.vel)                  #先算速度，再用新速度算位移
            self.pos=plus(times(self.vel,time_pass),self.pos)
        elif how_to_cal==2:                                                     #蛙跳法
            if self.first_cal==1:                                               #第一步先反推一下上一半时刻的速度
                self.vel=minus(self.vel,times(self.acce,0.5*time_pass))
                self.first_cal=0
            elif self.first_cal==0:                                             #第二步开始，速度比位移慢半个步长
                self.vel=plus(times(self.acce,time_pass),self.vel)  
                self.pos=plus(times(self.vel,time_pass),self.pos)

    def punch(self):                                #边界碰撞检测  简化版
        if self.pos[1]<=self.radius:                #若下一时刻粒子超出 上 边界
            self.pos[1]=self.radius                
            self.vel[1]=-self.vel[1]
        if self.pos[1]>=height-self.radius:         #若下一时刻粒子超出 下 边界
            self.pos[1]=height-self.radius   
            self.vel[1]=-self.vel[1]
        if self.pos[0]<=self.radius:                #若下一时刻粒子超出 左 边界
            self.pos[0]=self.radius          
            self.vel[0]=-self.vel[0]
        if self.pos[0]>=width-self.radius:          #若下一时刻粒子超出 右 边界
            self.pos[0]=width-self.radius    
            self.vel[0]=-self.vel[0]

        for i in self.near_dots:                    #与其他球体的碰撞检测，这里的代码我已经看不懂了，不要动
            if i==self.id:                          #与自己的碰撞检测直接跳过
                continue
            i=ball_list[i]                          #利用下一时刻的位置进行碰撞检测，改善了粒子会黏在一起的现象
            next_pos_self=plus(self.pos,times(self.vel,time_pass))
            next_pos_i=plus(i.pos,times(i.vel,time_pass))
            distance_vec=minus(next_pos_self,next_pos_i)                                    
            distance=magenititude(distance_vec)
            if distance<=self.radius+i.radius:      #用两球圆心距离判断是否相撞
                self.vel[1]=-self.vel[1]   
                i.vel[1]=-i.vel[1]
                distance_vec[1]=-distance_vec[1]    #将两球速度、距离向量转化为右手系
                degree=float(angle_to_horizontal(distance_vec))
                new_self_vel=rotate_CCS(self.vel,degree)
                new_i_vel=rotate_CCS(i.vel,degree)
                new_self_vel[0],new_i_vel[0]=new_i_vel[0],new_self_vel[0]       #连心线方向速度交换，另一方向速度不变
                self.vel=rotate_CCS(new_self_vel,0-degree)
                i.vel=rotate_CCS(new_i_vel,0-degree)
                self.vel[1]=-self.vel[1]
                i.vel[1]=-i.vel[1]                  #将两球速度、距离向量转化为左手系

    def renew(self):                                #更新自己数据  需实时更新的数据
        self.punch()
        self.new_pos_vel()                      
        

def create_balls(n):                                #粒子随机生成函数，n为生成球的数量
    time_pass=clock.tick()/1000
    print('自程序开始以来用时为：%.4f'%time_pass)
    m=0
    while m<n:                                      #随机生成各项参数
        random_pos=[randint(0,width-1),randint(100,height-1)]                   #减1 是由于格子以右上角为基准，有(800,0)的话会出错
        random_tem=randint(0,100)
        random_vel=[randint(-100,100),randint(-100,100)]
        random_color=(randint(0,255),randint(0,255),randint(0,255))
        balls(random_pos,random_vel,random_tem,random_color)
        m+=1
    for i in ball_list:                             #生成小球后立刻对其附近格子与粒子进行更新
        i.find_near_grids_dots()
    time_pass=clock.tick()/1000
    print('生成%d个小球用时：%.4f'%(n,time_pass))

def creat_balls0(n):
    x,y,m=ball_radius,ball_radius,0
    while y<=300:
        while x<=200:
            if n==2:   #奇数行小球错开一个身位  可将这三行注释掉，看看区别
                x+=6
                n=0  
            balls([x,y],[0,0],25,(255,255,255))
            x+=12
        y+=12
        n+=1
        x=ball_radius




def check_ball():                                   #检测并显示粒子
    global check_id,key_press_allow
    pressed_keys = pygame.key.get_pressed()
    if key_press_allow==1:
        if pressed_keys[257]:                       #按小键盘1 使 小球id+1
            check_id+=1
        if pressed_keys[258]:                       #按小键盘2 使 小球id+10
            check_id+=10
        if pressed_keys[259]:                       #按小键盘3 使 小球id+100
            check_id+=100
        key_press_allow=0
        check_id%=len(ball_list)
    if  (not pressed_keys[257]) and (not pressed_keys[258]) and (not pressed_keys[259]):
        key_press_allow=1
    
    for i in ball_list[check_id].near_grids:
        pygame.draw.rect(screen,(255,0,0), (grid_list[i],(smooth_length,smooth_length)), 2)             #红色显示附近格子
    for i in ball_list[check_id].near_dots:
        pygame.draw.circle(screen,(255,255,255),converse_int(ball_list[i].pos),10,2)                    #白色圈出附近粒子
    
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    show_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]         #寻找鼠标所在的格子
    pygame.draw.rect(screen,(255,255,255), (show_grid,(smooth_length,smooth_length)), 1)                #画出鼠标所在的格子
    for i in balls_in_grid_list[grid_list.index(show_grid)]:                                            #显示鼠标所在格子的粒子
        pygame.draw.circle(screen,(0,255,0),converse_int(ball_list[i].pos),15,3)

    pygame.draw.circle(screen,(0,255,255),converse_int(ball_list[check_id].pos),10,2)                   #显示目前选中粒子的位置
    check_id_show=pygame.font.Font('freesansbold.ttf',30).render(str(check_id),1,(200,0,0))             #显示当前查看粒子的id
    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))           #显示鼠标位置
    screen.blit(check_id_show,(0,30))
    screen.blit(mouse_pos_show,(0,0))
    print(ball_list[check_id].acce)
    
def balls_in_grid_renew():
    for i in balls_in_grid_list:
        i.clear()                                   ###为什么 i=[] 不能用？
    for i in ball_list:
        balls_in_grid_list[grid_list.index(i.in_grid)].append(i.id)


def generate_grids():                               #网格生成函数
    x,y=0,0
    while y<height:                                 #生成网格并记录左上角顶点坐标
        while x<width:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=smooth_length
        y+=smooth_length
        x=0
def generate_grids2():                              #网格生成函数   为界面外多生成一圈格子，防止粒子跑到外边
    x,y=-smooth_length,-smooth_length
    while y<height+smooth_length:                   #生成网格并记录左上角顶点坐标
        while x<width+smooth_length:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=smooth_length
        y+=smooth_length
        x=-smooth_length
generate_grids2()


#create_balls(10)
creat_balls0(10)
while 1:
    screen.fill((0,0,0))
    
    #time_pass=clock.tick()/1000                     #过去的实际时间
    time_pass=0.008                                #设定的时间
         
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    if pressed_mouse[0]==1:                         #点击鼠标左键，进行check动作
        check_ball()

    for i in ball_list:
        i.renew()
        pygame.draw.circle(screen,i.color,converse_int(i.pos),i.radius)

    renew_ready=(renew_ready+1)%renew_freq          #每次循环都将此值加1后对刷新频率取余
    if renew_ready==0:                              #对数据更新之前应先进行碰撞检测，防止球体出现在边界之外
        balls_in_grid_renew()
        for i in ball_list:
            i.find_near_grids_dots()
    pygame.display.update()


#存在问题：
#①仍然存在粒子于边界来回游走的问题                           不确定
#②无耗散情况下仍然越弹越高或反之,无法保持高度守恒             确定将之忽略原因见下
#③粒子间碰撞会存在粒子粘在一起的情况，经常出现                待解决,已通过用下一时刻的位置进行碰撞检测解决

#改进：
#①增加吸引力(表面张力)
#②增加另外的速度位移计算方法——蛙跳法  已有欧拉积分法
#③测试数据刷新频率的合适值
#④增加拉框生成球
#⑤增加固定生成球的方法，用来测试
#○解决现存问题

#现有的碰撞算法会忽略加速度在这一时间段内的作用，会使跳跃高度不守恒。而改进将导致计算负担严重增加，鉴于有四个边界
#以及粒子间的‘伪边界’，改进算法不与考虑，直接使用最简单的碰撞函数
#已解决

#实际上，使用蛙跳算法的话，整数的时间步长的速度并不重要，我们计算粒子位移也不需要这一数据，因此可以直接删除，以减少程序运算负担
#已解决

#有一种猜测，粒子黏在一起是由于：如果甲乙两粒子碰撞，两者的速度在甲粒子碰撞就检测时被反向，又再乙的碰撞检测中被反向，
#两次反向导致实际速度并无变化，下一步可以尝试在碰撞检测时只在连心线上反向自己的速度，不管另一个的速度
#已解决

#V1.3       增加了粒子间碰撞的函数，增加了数据刷新控制函数，现在不会每次都刷新一遍相关数据了
#V1.4       增加了粒子间的吸引力与排斥力，增加了固定位置生成粒子，且解决了粒子黏着的问题，初步实现了模拟流动，但效果不好