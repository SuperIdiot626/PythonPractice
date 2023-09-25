#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *

#以下为调试用参数                                    #1个像素=1cm 其他均为m kg s 
width,height=400,400                                #界面的长宽
smooth_length=50                                    #光滑长度
gravity=[0,1000]                                    #调整重力的大小及方向 10m/ss
miu=-5.0                                            #运动中的阻力项
ball_radius=2                                       #粒子半径
layer_thick=20                                      #边界层厚度，与具体厚度呈负相关
kenel_function_choose=3                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel
renew_freq=1                                        #刷新间隔帧数，最小为1
check=1                                             #是否追随粒子，并进行检测
how_to_cal=2                                        #1为欧拉法，2为蛙跳法
mass=1                                              #每个粒子的质量 单位kg
time_pass=0.01                                      #时间步长 如果运算足够快可以替换为实际流逝时间

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
        self.pos=pos                                #位置   需即时更新
        self.vel=vel                                #速度   需即时更新
        self.acce=[0,0]                             #加速度 需即时更新
        self.rho=rho0                               #密度   需即时更新
        self.pressure=B                             #压力   需即时更新 这里是绝对压力

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


    def acce_compute(self):                                                     #加速度计算，包括压力项与粘性项
        self.acce=plus(gravity,times(self.vel,miu))                             #加速度基数为重力加速度与摩擦造成的减速
        for i in self.nearest_dots:
            i=ball_list[i]
            d_pos=divide(minus(self.pos,i.pos),100)                             #位置差，转换为m制
            d_vel=divide(minus(self.vel,i.vel),100)                             #速度差，转换为m制
            mid_term1=nabla_kenel(self.pos,i.pos,smooth_length)                 #中间项
            mid_term2=self.pressure/self.rho**2+i.pressure/i.rho**2             #这里的压力为绝对压力
            mid_term3=2*viscosity/i.rho*dot_product(d_pos,d_vel)/magenititude(d_pos)
            acc_viscosity = times(mid_term1,mid_term3)                          #粘性项
            acc_pressure  = times(mid_term1,mid_term2)                          #压力项
            acc_addition  = plus(acc_viscosity,acc_pressure)
            #self.acce=plus(self.acce,self.surface_tension())                   #表面张力暂时不予考虑
            self.acce=plus(self.acce,acc_addition)
    
    def surface_tension(self):
        surface_force=[0,0]
        ni=[0,0]
        curvature=0
        Csi=0
        if len(self.nearest_dots)  == 0:
            return [0,0]                                                        #若影响域内无粒子，则直接跳出，无需进一步计算
        else:                                                                   #否则需进行表面张力的计算
            for i in self.nearest_dots:                                         #计算自身Csi
                i=ball_list[i]
                Csi += norma_kenel(self.pos,i.pos,smooth_length)/i.rho          #Csi叠加
            Csi-=1
            for i in self.nearest_dots:                                         #计算本身ni，式子3.27
                i=ball_list[i]                                                  #计算Laplace_Csi 式子3.55 3.33
                mid_term1 = nabla_kenel(self.pos,i.pos,smooth_length)
                d_pos=divide(minus(self.pos,i.pos),100)                         #计算△Xij 转换为m制
                mid_term2=2/i.rho*Csi/magenititude_simple(d_pos)
                mid_term3=dot_product(d_pos,mid_term1)
                mid_term1 = times(mid_term1,Csi)
                ni  = plus(ni,mid_term1)                            #梯度叠加
                curvature+= mid_term2*mid_term3                                 #曲率叠加
            ni=divide(ni,self.rho)
            ni_leng=magenititude(ni)
            ni_unit=divide(ni,ni_leng)
            if ni_leng>=layer_thick:                                            #用于判断粒子是否处于表层
                self.color=(100,0,0)                                            #对于处在表层的粒子，颜色变红作为标记
                surface_force=times(ni_unit,-curvature*sigma)                   #式子3.53
                return surface_force
            else:
                self.color=(255,255,255)                                        #不在表层的粒子恢复白色
                return [0,0]                                                    #不在表层，不受表面张力


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
    def find_nearest_dots(self):                    #找到影响域圆内的粒子id,不包括自身id
        self.nearest_dots=[]                        #每次调用需将原始数据清空
        for i in self.near_dots:
            i=ball_list[i]
            distance=magenititude(minus(self.pos,i.pos))
            if distance>smooth_length or self.id == i.id:
                continue
            else:
                self.nearest_dots.append(i.id)      #储存影响域圆内粒子id


    def compute_rho(self):                          #密度更新 式子3.37  比3.36准确
        for i in self.nearest_dots:             
            i=ball_list[i]                          #将粒子id转换为粒子本身
            mid_term1 = nabla_kenel(self.pos,i.pos,smooth_length)
            mid_term2 = divide(minus(self.vel,i.vel),100)   #转换为m制
            self.rho+=dot_product(mid_term1,mid_term2)*time_pass

    def compute_pressure(self):                     #压力更新
        self.pressure=B*(self.rho/rho0)**gamma      #式子2.4 红皮 此处进行了更改，变为总压

    def punch_boundary(self):                       #专门的边界碰撞函数      
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
    def punch_particle(self):                       #专门的粒子碰撞函数
        for i in self.nearest_dots:                 #由于neares中没有自己的id，所以不需考虑自己
            i=ball_list[i]                          
            if 1:                                   #此处可根据需要选择是否使用下一时刻的位置进行碰撞计算
                next_pos_self=plus(self.pos,times(self.vel,time_pass))
                next_pos_i=plus(i.pos,times(i.vel,time_pass))
                distance_vec=minus(next_pos_self,next_pos_i)
            else:
                distance_vec=minus(self.pos,i.pos)
            dx=abs(distance_vec[0])                 #参照学姐代码，这一操作相比之前大大减少了运算量
            dy=abs(distance_vec[1])
            if dx<self.radius+i.radius and dy<self.radius+i.radius:
                self.vel[1]=-self.vel[1]            #与其他球体的碰撞检测，这里的代码我已经看不懂了，不要动
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

    def renew(self):                                #更新自己数据  需实时更新的数据
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
def create_balls_rectan(m):                         #以方形生成小球
    apex1=(0,0.5*height)                            #方框顶点之一
    apex2=(0.25*width,height)                       #方框顶点之二
    #apex1=(100,100)                                #方框顶点之一
    #apex2=(250,250)                                #方框顶点之二
    start=(min(apex1[0],apex2[0]),min(apex1[1],apex2[1]))
    end=(max(apex1[0],apex2[0]),max(apex1[1],apex2[1]))
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
        i.clear()                                   ###为什么 i=[] 不能用？
    for i in ball_list:
        try:
            a=grid_list.index(i.in_grid)            #有可能超过界面，故设置一个错误跑出
        except ValueError:
            i.punch_boundary()
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
        i.find_near_grids_dots()                                                #对周围格子和粒子要初始化
        dy=(i.pos[1]-ball_list[0].pos[1])/100                                   #以最后一个粒子的高度为参照（粒子生成是从上至下的）转换为m制
        i.rho=rho0*(1+rho0*magenititude(gravity)/100*dy/B)**(1/gamma)           #学姐论文 式子4.3  初始化密度


#create_balls_random(10)
create_balls_rectan(10)
initialize()
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



#v2.0               增加了粘性项、压力项的计算，将大部分单位进行了标准化转换，但仍有部分未发现
#v2.1               各项的计算公式基本正确且无重大bug，现在存在的问题是速度方面的单位没有进行标准化转换
#v2.1               除了祖传bug之外，仍有粒子超界的bug，这个应该好解决，另外需要在显示上动动手脚，让粒子间距小一点，另外初始化生成也要修改

#存在问题：
#①粒子黏着，祖传bug了           #v1.0出现
#②粒子密度多次运算后会逐个归零   #v2.0出现  v2.1解决
#④速度单位未进行标准化转换       #v2.0出现  v2.1解决

#改进：
#将蛙跳积分初始化这一步写入initialize()中 未实现
#或许在屏幕外多生成一层格子没有必要  确实有必要
#显示上做做手脚，初始化时距离变大一些