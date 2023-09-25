#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *

#以下为调试用参数  
width,height=500,500                                #界面的长宽
smooth_length=50                                    #光滑长度
gravity=[0,1000]                                    #调整重力的大小及方向
miu=-5.0                                            #运动中的阻力项
ball_radius=2                                       #粒子半径
layer_thick=20                                      #边界层厚度，与具体厚度呈负相关
kenel_function_choose=3                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel
alpha_D1 = 5/3.1415/2.55                            #此处参数因根据实际情况进行调试 这三个值需要根据光滑长度进行调整
alpha_D2 = 15/7/3.1415*5.6                          #部分数据红皮书与学姐论文不相符，需自行调试 
renew_freq=5                                        #刷新间隔帧数，最小为1
check=1                                             #是否追随粒子，并进行检测
how_to_cal=2                                        #1为欧拉法，2为蛙跳法

alpha_D3 = alpha_D2*3/2                             #alpha_D3计算，与alpha_D2呈比例关系，直接计算
grid_list=[]                                        #用于储存网格左上顶点坐标     元素为 列表 坐标 
ball_list=[]                                        #用于储存所有粒子            元素为 粒子
balls_in_grid_list=[]                               #用于储存各个格子中的粒子     元素为 列表，列表内为粒子id
check_id=0                                          #目前所查看粒子的id
key_press_allow=1                                   #是否允许下次按键输入
renew_ready=0                                       #用于计算部分数据是否应该刷新





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
        self.color=color                            #颜色
        self.id=len(ball_list)                      #以ball_list的长度作为id    不需更新
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          #储存临近格子的id   不需即时更新
        self.near_dots=[]                           #储存临近粒子的id   不需即时更新
        self.nearest_dots=[]                        #储存影响域圆内粒子id 需即时更新
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

    def find_nearest_dots(self):                    #找到影响域圆内的粒子id
        self.nearest_dots=[]                        #每次调用需将原始数据清空
        for i in self.near_dots: 
            distance=magenititude(minus(self.pos,ball_list[i].pos))
            if distance>smooth_length or self.id == i:
                continue
            else:
                self.nearest_dots.append(i)

    def acce_compute(self):
        self.acce=plus(gravity,times(self.vel,miu)) #加速度基数为重力加速度与摩擦造成的减速
        gradient=[0,0]
        curvature=0
        Csi=0
         
        if len(self.nearest_dots)  == 0:
            return 0                                #若影响域内无粒子，则直接跳出，无需进一步计算
        else:                                       #否则需进行表面张力的计算
            for i in self.nearest_dots:
                nabla_kenel_result = nabla_kenel(self.pos,ball_list[i].pos,smooth_length)
                if nabla_kenel_result=='0':                                     #有时会出现该距离大于光滑距离的情况，原因未知
                    self.nearest_dots.remove(i)
                    if self.nearest_dots==[]:                                   #有可能影响域圆内只有一个粒子，此时退出当前计算
                        return 0
                    continue
                gradient=plus(gradient,nabla_kenel_result)                      #梯度叠加
                Csi += norma_kenel(self.pos,ball_list[i].pos,smooth_length)     #Csi叠加
            gradient=divide(gradient,len(self.nearest_dots))                    #梯度要最后除以粒子数量
            Csi=Csi/len(self.nearest_dots)-1                                    #计算该粒子的Csi，下一步计算需要Csi-Csj，但所有Csj=0                                                        
            if magenititude_simple(gradient)>=layer_thick:                      #用于判断粒子是否处于表层
                self.color=(100,0,0)                                            #对于处在表层的粒子，颜色变红作为标记
                for i in self.nearest_dots:                                     #仅对存在于影响域内的粒子进行计算
                    vector=minus(self.pos,ball_list[i].pos)                     #这两行是用于计算曲率
                    nabla_kenel_result = nabla_kenel(self.pos,ball_list[i].pos,smooth_length)
                    curvature += 2 * Csi* dot_product(vector,nabla_kenel_result)/magenititude_simple(vector)  
                curvature/=len(self.nearest_dots)                               #曲率要最后除以粒子数量
                self.acce=plus(self.acce,times(gradient,-5*curvature))          #加速度相加即可
            else:
                self.color=(255,255,255)



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
        self.find_nearest_dots()
        self.punch()
        self.new_pos_vel()                      


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


def create_balls_random(n):                         #粒子随机生成函数，n为生成球的数量
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
def create_balls_rectan(m):                         #以方形生成小球
    start=(150,150)                                 #方框左上角
    end=(350,350)                                   #方框右下角
    x,y,n=start[0],start[1],1                       
    while y<=end[1]:
        while x<=end[0]:
            '''if n==2:                                #奇数行小球错开一个身位  可将这三行注释掉，看看区别
                x+=m/2
                n=0  '''
            balls([x,y],[0,0],25,(255,255,255))
            x+=m
        y+=m
        n+=1
        x=start[0]


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
        if pressed_keys[260]:                       #按小键盘4 使 小球id-1
            check_id-=1
        if pressed_keys[261]:                       #按小键盘5 使 小球id-10
            check_id-=10
        if pressed_keys[262]:                       #按小键盘6 使 小球id-100
            check_id-=100
        key_press_allow=0
        check_id%=len(ball_list)
    if   sum(pressed_keys[257:263])==0:
        key_press_allow=1
    pygame.draw.circle(screen,(0,0,255),converse_int(ball_list[check_id].pos),smooth_length,2)          #画出影响域圆
    for i in ball_list[check_id].near_grids:
        pygame.draw.rect(screen,(255,0,0), (grid_list[i],(smooth_length,smooth_length)), 2)             #红色显示附近格子
    for i in ball_list[check_id].near_dots:
        pygame.draw.circle(screen,(255,0,0),converse_int(ball_list[i].pos),ball_radius)                 #红色标出 影响域方框内粒子
    for i in ball_list[check_id].nearest_dots:
        pygame.draw.circle(screen,(0,255,0),converse_int(ball_list[i].pos),ball_radius+2)               #绿色标出 影响域圆 内粒子
    
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    show_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]         #寻找鼠标所在的格子
    pygame.draw.rect(screen,(255,255,255), (show_grid,(smooth_length,smooth_length)), 2)                #画出鼠标所在的格子
    for i in balls_in_grid_list[grid_list.index(show_grid)]:                                            #显示鼠标所在格子的粒子
        pygame.draw.circle(screen,(0,255,0),converse_int(ball_list[i].pos),ball_radius+1)               #绿色标出 影响域圆 内粒子

    pygame.draw.circle(screen,(0,255,255),converse_int(ball_list[check_id].pos),10,2)                   #显示目前选中粒子的位置
    check_id_show=pygame.font.Font('freesansbold.ttf',30).render(str(check_id),1,(200,0,0))             #显示当前查看粒子的id
    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))           #显示鼠标位置
    screen.blit(check_id_show,(0,30))
    screen.blit(mouse_pos_show,(0,0))
    #print(ball_list[check_id].acce)
    

def balls_in_grid_renew():
    for i in balls_in_grid_list:
        i.clear()                                   ###为什么 i=[] 不能用？
    for i in ball_list:
        balls_in_grid_list[grid_list.index(i.in_grid)].append(i.id)

def generate_grids():                              #网格生成函数   为界面外多生成一圈格子，防止粒子跑到外边
    x,y=-smooth_length,-smooth_length
    while y<height+smooth_length:                  #生成网格并记录左上角顶点坐标
        while x<width+smooth_length:
            grid_list.append([x,y])                #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])          #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=smooth_length
        y+=smooth_length
        x=-smooth_length
generate_grids()


#create_balls_random(10)
create_balls_rectan(20)
while 1:
    screen.fill((0,0,0))
    
    #time_pass=clock.tick()/1000                     #过去的实际时间
    time_pass=0.01                                   #设定的时间
         
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
#④部分情况下程序会崩溃，但原因未知
#⑤仍有粒子跑出边界，准备通过跑出错误解决。

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
#V1.5       增加了书上的表面张力算法，但还未添加粒子是否处于表面的判定，且目前效果仍旧不理想，许多参数需要进一步调试。
#V1.6       增加了表面层判定，但目前状态下四个角的加速度并不对称，原因未知，需进一步查明
#V1.7       123为增加，456为减少   查明了上个版本的bug 目前来说运行良好，最大的问题就是碰撞检测，粒子总是黏在一起