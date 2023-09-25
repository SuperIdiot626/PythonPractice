#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *

#以下为调试用参数                                    #1个像素=1cm 其他均为m kg s 

width,height=400,400        
smooth_length=50            
gravity=[0,1000]             
miu=-5                    #运动中的阻力项
ball_radius=2                #粒子半径
layer_thick=20               #边界层厚度，与具体厚度呈负相关
kenel_function_choose=3      #核函数选择，
renew_freq=5                 #刷新间隔帧数，最小为1
check=1                      #是否追随粒子，并进行检测
how_to_cal=2                 #1为欧拉法，2为蛙跳法
mass=1                       #每个粒子的质量 单位kg
time_pass=0.01               #时间步长 

#以下四行可根据不同液体进行更换


rho0=1000                                           #参考密度，水为1000
viscosity=0.001                                     #水的粘性
gamma=7                                             #对于水，gamma=7
B=100000                                            #B=c*c*rho0/gamma 但绝大多数情况下可设置为初始压力
sigma=100

#以下为中间参数，无需改动
alpha_D1 = 5/math.pi/(smooth_length/100)**2         #红皮书 3.43
alpha_D2 = 15/7/math.pi/(smooth_length/100)**2      #部分数据红皮书与学姐论文不相符，推测学姐写错了
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
#screen=pygame.display.set_mode((width,height),FULLSCREEN)
pygame.display.set_caption('New Try of SPH')


class balls(object):


    def __init__(self,pos,vel,tem,color):
        self.pos=pos                                
        self.vel=vel                                   
        self.acce=[0,0]                             
        self.rho=rho0                                
        self.pressure=B                             
        self.tem=tem                                
        self.radius=ball_radius                   
        self.color=color                           
        self.id=len(ball_list)                   
        ball_list.append(self)                     
        
        


        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                         
        self.near_dots=[]                          
        self.nearest_dots=[]                        
        balls_in_grid_list[grid_list.index(self.in_grid)].append(self.id)    


        

        self.first_cal=1                            #蛙跳算法的第一次运算检测
        

    


    def acce_compute(self):                                                     
        self.acce=plus(gravity,times(self.vel,miu))                        
        for i in self.nearest_dots:
            i=ball_list[i]
            d_pos=divide(minus(self.pos,i.pos),100)                            
            d_vel=divide(minus(self.vel,i.vel),100)                         
            mid_term1=nabla_kenel(self.pos,i.pos,smooth_length)               
            mid_term2=self.pressure/self.rho**2+i.pressure/i.rho**2            
            mid_term3=2*viscosity/i.rho*dot_product(d_pos,d_vel)/magenititude(d_pos)
            acc_viscosity = times(mid_term1,mid_term3)                         
            acc_pressure  = times(mid_term1,mid_term2)                      
            acc_addition  = plus(acc_viscosity,acc_pressure)
            #self.acce=plus(self.acce,self.surface_tension())                 
            self.acce=plus(self.acce,acc_addition)




    def surface_tension(self):
        surface_force=[0,0]
        ni=[0,0]
        curvature=0
        Csi=0
        if len(self.nearest_dots)  == 0:
            return [0,0]                                                 
        else:                                                            
            for i in self.nearest_dots:                                  
                i=ball_list[i]
                Csi += norma_kenel(self.pos,i.pos,smooth_length)/i.rho   
            Csi-=1
            for i in self.nearest_dots:                                  
                i=ball_list[i]                                           
                mid_term1 = nabla_kenel(self.pos,i.pos,smooth_length)
                d_pos=divide(minus(self.pos,i.pos),100)                   
                mid_term2=2/i.rho*Csi/magenititude_simple(d_pos)
                mid_term3=dot_product(d_pos,mid_term1)
                mid_term1 = times(mid_term1,Csi)
                ni  = plus(ni,mid_term1)                                 
                curvature+= mid_term2*mid_term3                         
            ni=divide(ni,self.rho)
            ni_leng=magenititude(ni)
            ni_unit=divide(ni,ni_leng)
            if ni_leng>=layer_thick:                                     
                surface_force=times(ni_unit,-curvature*sigma)             
                return surface_force
            else:
                return [0,0]                                          


    '''
    '''

    def find_near_grids_dots(self):                 
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          
        self.near_dots=[]                          
        x=-1
        y=-1
        while y<=1:
            while x<=1:                            
                try:                                
                    n=grid_list.index([self.in_grid[0]+x*smooth_length,self.in_grid[1]+y*smooth_length])
                except ValueError:
                    x+=1
                    continue
                else:
                    x+=1
                    self.near_grids.append(n)               
                    self.near_dots+=balls_in_grid_list[n]   
            x=-1
            y+=1



    def find_nearest_dots(self):                    
        self.nearest_dots=[]                       
        for i in self.near_dots:
            i=ball_list[i]
            distance=magenititude(minus(self.pos,i.pos))
            if distance>smooth_length or self.id == i.id:
                continue
            else:
                self.nearest_dots.append(i.id)     

  
  
    def compute_rho(self):                          
        for i in self.nearest_dots:             
            i=ball_list[i]                          
            mid_term1 = nabla_kenel(self.pos,i.pos,smooth_length)
            mid_term2 = divide(minus(self.vel,i.vel),100)   
            self.rho+=dot_product(mid_term1,mid_term2)*time_pass
  


    def compute_pressure(self):                   
        self.pressure=B*(self.rho/rho0)**gamma     
  
  
    


    def punch_boundary(self):                       
        punched=0                                   
        if self.pos[1]<=self.radius:                
            self.pos[1]=self.radius                
            self.vel[1]=-self.vel[1]
            punched=1                               
        if self.pos[1]>=height-self.radius:        
            self.pos[1]=height-self.radius   
            self.vel[1]=-self.vel[1]
            punched=1                               
        if self.pos[0]<=self.radius:              
            self.pos[0]=self.radius          
            self.vel[0]=-self.vel[0]
            punched=1                               
        if self.pos[0]>=width-self.radius:          
            self.pos[0]=width-self.radius    
            self.vel[0]=-self.vel[0]
            punched=1                               
        if punched==1:
            self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
    
    


    def punch_particle(self):                      
        for i in self.nearest_dots:                 
            i=ball_list[i]                          
            if 1:                                 
                next_pos_self=plus(self.pos,times(self.vel,time_pass))
                next_pos_i=plus(i.pos,times(i.vel,time_pass))
                distance_vec=minus(next_pos_self,next_pos_i)
            else:
                distance_vec=minus(self.pos,i.pos)
            dx=abs(distance_vec[0])                 
            dy=abs(distance_vec[1])
            if dx<self.radius+i.radius and dy<self.radius+i.radius:
                self.vel[1]=-self.vel[1]           
                i.vel[1]=-i.vel[1]
                distance_vec[1]=-distance_vec[1]   
                degree=float(angle_to_horizontal(distance_vec))
                new_self_vel=rotate_CCS(self.vel,degree)
                new_i_vel=rotate_CCS(i.vel,degree)
                new_self_vel[0],new_i_vel[0]=new_i_vel[0],new_self_vel[0]       
                self.vel=rotate_CCS(new_self_vel,0-degree)
                i.vel=rotate_CCS(new_i_vel,0-degree)
                self.vel[1]=-self.vel[1]
                i.vel[1]=-i.vel[1]                  
       



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



    def renew(self):          
        self.find_nearest_dots()
        self.compute_rho()
        self.compute_pressure()
        self.punch_boundary()
        self.punch_particle()
        self.new_pos_vel()


def norma_kenel(X,X1,h):                            #核函数，待测试
    q=magenititude(minus(X,X1))/h

    if kenel_function_choose==0:                    # 1
        if q>1:
            return 0
        else:
            return 1   

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:
            return 0
        else:
            return  alpha_D1*(1+3*q-q**3-3*q**4)

    if kenel_function_choose==2:                    # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:
            return alpha_D2*(2/3-q**2+q**3/2)
        elif q<=2:
            return alpha_D2*(2-q)**3/6
        else:
            return 0

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:
            return alpha_D3*(2/3-q**2+q**3/2)*3/2
        elif q<=2:
            return alpha_D3*(2-q)**3/4
        else:
            return 0
def nabla_kenel(X,X1,h):                            #结果为向量
    q=magenititude(minus(X,X1))/h

    if kenel_function_choose==0:                    # 1
        if q>1:
            return (0,0)
        else:
            return (0,0)  

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:
            return (0,0)
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
            return (0,0)

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:
            return times(minus(X,X1),alpha_D3*(-2+3/2*q)*3/2)
        elif q<=2:
            return times(minus(X,X1),alpha_D3*(-(2-q)**2)/q*3/4)
        else:
            return (0,0)
def lapla_kenel(X,X1,h):                            #二次偏导
    q=magenititude(minus(X,X1))/h

    if kenel_function_choose==0:                    # 1
        if q>1:
            return 0
        else:
            return 0  

    if kenel_function_choose==1:                    # Lucy’s Quartic Kernel
        if q>1:                                    
            return 0
        else:
            return (3/q-9*q-48*q**2)*alpha_D1

    if kenel_function_choose==2:                    # Cubic Spline Kernel    又称为 B-样条型核函数
        q*=2
        if q<=1:  
            return (9/2*q-4)*alpha_D2
        elif q<=2:
            return (-3/2*q-2/q+4)*alpha_D2
        else:
            return 0

    if kenel_function_choose==3:                    # unit Cubic Spline Kernel    单位B-样条型核函数 三次样条曲线
        q*=2
        if q<=1:  
            return (9/2*q-4)*alpha_D3
        elif q<=2:
            return (-3/2*q-2/q+4)*alpha_D3
        else:
            return 0


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


def create_balls_rectan(m):                         
    apex1=(0,0.5*height)                            
    apex2=(0.25*width,height)                       
    start=(min(apex1[0],apex2[0]),min(apex1[1],apex2[1]))
    end=(max(apex1[0],apex2[0]),max(apex1[1],apex2[1]))
    x,y,n=start[0],start[1],1                       
    while y<=end[1]:
        while x<=end[0]:
            '''if n==2:                                
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
        i=ball_list[i]
        pygame.draw.circle(screen,(255,0,0),converse_int(i.pos),ball_radius)                            #红色标出 影响域方框内粒子
    for i in ball_list[check_id].nearest_dots:
        i=ball_list[i]
        pygame.draw.circle(screen,(0,255,0),converse_int(i.pos),ball_radius+2)                          #绿色标出 影响域圆 内粒子

    mouse_pos=pygame.mouse.get_pos()                                                                    #得到鼠标位置
    show_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]         #寻找鼠标所在的格子
    pygame.draw.rect(screen,(255,255,255), (show_grid,(smooth_length,smooth_length)), 2)                #画出鼠标所在的格子
    for i in balls_in_grid_list[grid_list.index(show_grid)]:                                            #显示鼠标所在格子的粒子
        i=ball_list[i]
        pygame.draw.circle(screen,(0,255,0),converse_int(i.pos),ball_radius+1)                          #绿色标出 影响域圆 内粒子

    pygame.draw.circle(screen,(0,255,255),converse_int(ball_list[check_id].pos),10,2)                   #显示目前选中粒子的位置
    check_id_show=pygame.font.Font('freesansbold.ttf',30).render(str(check_id),1,(200,0,0))             #显示当前查看粒子的id
    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))           #显示鼠标位置
    screen.blit(check_id_show,(0,30))
    screen.blit(mouse_pos_show,(0,0))
    #print(ball_list[check_id].acce)


def balls_in_grid_renew():
    for i in balls_in_grid_list:
        i.clear()                                   #每次调用，清空原始数据
    for i in ball_list:
        a=grid_list.index(i.in_grid)
        balls_in_grid_list[a].append(i.id)



def generate_grids():                               #网格生成函数   为界面外多生成一圈格子，防止粒子跑到外边
    #x,y=0,0                                         #使用这一参数，仅在界面内生成网格
    x,y=-smooth_length,-smooth_length              #注释掉的这两行用于在界面以外生成额外一圈格子
    while y<height+smooth_length:                   #生成网格并记录左上角顶点坐标
        while x<width+smooth_length:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=smooth_length
        y+=smooth_length
        #x=0
        x=-smooth_length


generate_grids()

def initialize():
    for i in ball_list:
        i.find_near_grids_dots()                                         
        dy=(i.pos[1]-ball_list[0].pos[1])/100                                   
        i.rho=rho0*(1+rho0*magenititude(gravity)/100*dy/B)**(1/gamma)          


#create_balls_random(10)
create_balls_rectan(15)
initialize()

while 1:
    screen.fill((0,0,0))                            
    time_pass=0.01                                  
    for i in ball_list:                            
        i.renew()               
        pygame.draw.circle(screen,i.color,converse_int(i.pos),i.radius)
    renew_ready=(renew_ready+1)%renew_freq         
    if renew_ready==0:                             
        balls_in_grid_renew()
        for i in ball_list:
            i.find_near_grids_dots()               
    pygame.display.update()                       
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    pressed_mouse=pygame.mouse.get_pressed()       
    if pressed_mouse[0]==1:                         
        check_ball()




    



#v2.0               增加了粘性项、压力项的计算，将大部分单位进行了标准化转换，但仍有部分未发现
#v2.1               各项的计算公式基本正确且无重大bug，现在存在的问题是速度方面的单位没有进行标准化转换
#v2.2               除了祖传bug之外，仍有粒子超界的bug，这个应该好解决，另外需要在显示上动动手脚，让粒子间距小一点，另外初始化生成也要修改

#存在问题：
#①粒子黏着，祖传bug了           #v1.0出现
#②粒子密度多次运算后会逐个归零   #v2.0出现  v2.1解决
#④速度单位未进行标准化转换       #v2.1出现  v2.2解决

#改进：
#将蛙跳积分初始化这一步写入initialize()中 未实现
#或许在屏幕外多生成一层格子没有必要  确实有必要
#显示上做做手脚，初始化时距离变大一些