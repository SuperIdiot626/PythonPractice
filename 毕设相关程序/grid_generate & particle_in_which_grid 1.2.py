#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *


width,height=800,600            #界面的长宽
smooth_length=100                #光滑长度
miu=-0.0                        #运动中的阻力项
                                                            
grid_list=[]                    #用于储存网格左上顶点坐标     元素为 列表 坐标 
ball_list=[]                    #用于储存所有粒子            元素为 粒子
balls_in_grid_list=[]           #用于储存各个格子中的粒子     元素为 列表，列表内为粒子id
check_id=300                    #目前所查看粒子的id
key_press_allow=1               #是否允许下次按键输入


pygame.init()
clock=pygame.time.Clock()       #用于计时
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('New Try of SPH')



class balls(object):
    def __init__(self,pos,vel,tem,color):
        self.pos=pos                                #位置
        self.vel=vel                                #速度       一般也为0
        self.acce=[0,1000]                          #加速度，调整此项可调整重力方向，默认为向下
        self.radius=5
        self.tem=tem                                #暂时无用
        self.color=color
        self.id=len(ball_list)                      #以ball_list的长度作为id
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          #储存临近格子的id
        self.near_dots=[]                           #储存临近粒子的id
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
    
    def positioncompute(self):
        self.pos=plus(times(self.vel,time_pass),self.pos)
    def velocitycompute(self):
        self.vel=plus(times(self.acce,time_pass),self.vel)
    def acceleratecompute(self):
        self.acce=plus(times(self.vel,miu),[0,1000])                            #先计算空气阻力，再加上重力


    def punch(self):                                #边界碰撞检测
        delta_x=self.vel[0]*time_pass
        delta_y=self.vel[1]*time_pass
        if self.pos[1]+delta_y<=self.radius:        #若下一时刻粒子超出 上 边界
            self.pos[1]=self.radius                
            self.vel[1]=-self.vel[1]
        if self.pos[1]+delta_y>=height-self.radius: #若下一时刻粒子超出 下 边界
            self.pos[1]=height-self.radius   
            self.vel[1]=-self.vel[1]
        if self.pos[0]+delta_x<=self.radius:        #若下一时刻粒子超出 左 边界
            self.pos[0]=self.radius          
            self.vel[0]=-self.vel[0]
        if self.pos[0]+delta_x>=width-self.radius:  #若下一时刻粒子超出 右 边界
            self.pos[0]=width-self.radius    
            self.vel[0]=-self.vel[0]
    
    def punch1(self):                               #边界碰撞检测  简化版
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

    def punch2(self):                               #边界碰撞检测  升级版
        delta_x=self.vel[0]*time_pass
        delta_y=self.vel[1]*time_pass
        if self.pos[0]+delta_x<=self.radius:        #若下一时刻粒子超出 左 边界
            self.pos[0]=2*self.radius-self.pos[0]-delta_x 
            self.vel[0]=-self.vel[0]
        if self.pos[0]+delta_x>=width-self.radius:  #若下一时刻粒子超出 右 边界
            self.pos[0]=2*width-2*self.radius-self.pos[0]-delta_x 
            self.vel[0]=-self.vel[0]

        if self.pos[1]+delta_y<=self.radius:        #若下一时刻粒子超出 上 边界
            self.pos[1]=2*self.radius-self.pos[1]-delta_y                
            self.vel[1]=-self.vel[1]

        if self.pos[1]+delta_y>=height-self.radius: #若下一时刻粒子超出 下 边界
            self.pos[1]=2*height-2*self.radius-self.pos[1]-delta_y  
            self.vel[1]=-self.vel[1]


    def renew(self):                                #更新自己数据
        self.find_near_grids_dots() 
        self.acceleratecompute()
        self.velocitycompute()
        self.positioncompute()                         
        self.punch1()

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
    
    check_id_show=pygame.font.Font('freesansbold.ttf',30).render(str(check_id),1,(200,0,0))             #显示当前查看粒子的id
    pygame.draw.circle(screen,(0,255,255),converse_int(ball_list[check_id].pos),10,2)                   #显示目前选中粒子的位置
    screen.blit(check_id_show,(0,30))

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


generate_grids()

create_balls(100)

while 1:
    screen.fill((0,0,0))

    time_pass=clock.tick()/1000                    #过去的实际时间
    #time_pass=0.005                                #设定的时间     

    for event in pygame.event.get():
        if event.type==QUIT:
            exit()

    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    show_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]         #寻找鼠标所在的格子
    pygame.draw.rect(screen,(255,255,255), (show_grid,(smooth_length,smooth_length)), 1)                #画出鼠标所在的格子
    for i in balls_in_grid_list[grid_list.index(show_grid)]:                                            #显示鼠标所在格子的粒子
        pygame.draw.circle(screen,(0,255,0),converse_int(ball_list[i].pos),15,3)


    
    if pressed_mouse[0]==1:                         #点击鼠标左键，进行check动作
        check_ball()
        

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))           #显示鼠标位置
    screen.blit(mouse_pos_show,(0,0)) 

    balls_in_grid_renew()
    for i in ball_list:
        i.renew()
        pygame.draw.circle(screen,i.color,converse_int(i.pos),i.radius)
    pygame.display.update()


#存在问题：
#①仍然存在粒子于边界来回游走的问题
#②无耗散情况下仍然越弹越高或反之，无法保持高度守恒
#改进：
#①添加粒子间碰撞，与吸引力(表面张力)
#②解决现存问题

#现有的碰撞算法在运行时会忽略掉重力在这一时间段内的作用，因此会导致跳跃高度不守恒。而改进
#的话会导致算法变得极其复杂，考虑到四周的边界碰撞与粒子之间的碰撞，这一点先不予考虑。
#直接使用最简单的碰撞函数