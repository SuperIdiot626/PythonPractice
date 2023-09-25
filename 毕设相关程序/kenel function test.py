#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,math,time
from random             import randint
from pygame.locals      import *
from vectorcalculate    import *

#以下为调试用参数  
width,height=800,600                                #界面的长宽
smooth_length=50                                    #光滑长度
gravity=[0,0]                                       #调整重力的大小及方向
miu=0                                               #运动中的阻力项
ball_radius=3                                       #粒子半径
layer_thick=20                                      #表层厚度，与具体厚度呈负相关
kenel_function_choose=3                             #核函数选择，0为1  1为 Lucy’s Quartic Kernel  2为 Cubic Spline Kernel            
gap=5                                               #图像分辨率
draw_tem=0                                          #是否绘制温度分布图  1为是 0为否
draw_screen=1                                       #绘制图像专用
sigma=100                                           #表面张力系数

def f(x):                                           #图像生成函数
    y=250*math.cos(x/200*3.14159)
    return y

alpha_D1 = 5/math.pi/(smooth_length/100)**2         #红皮书 3.43
alpha_D2 = 15/7/math.pi/(smooth_length/100)**2      #部分数据红皮书与学姐论文不相符，推测学姐写错了
alpha_D3 = alpha_D2*3/2                             #alpha_D3计算，与alpha_D2呈比例关系，直接计算
grid_list=[]                                        #用于储存网格左上顶点坐标       元素为 列表 坐标 
ball_list=[]                                        #用于储存所有粒子              元素为 粒子
balls_in_grid_list=[]                               #用于储存各个格子中的粒子       元素为 列表，列表内为粒子id
dots_within_domain=[]                               #用于储存处于影响域内的粒子     元素为 数字，粒子id
check_id=0                                          #目前查看粒子的id，默认初始为零
key_press_allow=1                                   #是否允许下次鼠标点击，初始值不影响


pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height),RESIZABLE|DOUBLEBUF)
pygame.display.set_caption('Kenel Function Test')


class balls(object):
    def __init__(self,pos,vel,tem,color):
        self.pos=pos                                #位置   需即时更新
        self.vel=vel                                #速度   需即时更新
        self.acce=[0,0]                             #加速度 需即时更新

        self.rho=1000                               #密度   rho就是密度rou
        self.mass=1                                 #质量
        self.pressure=1000                          #压力
        self.viscosity=1                            #粘性

        self.radius=ball_radius                     #半径  
        self.tem=tem                                #暂时无用
        self.color=color                            #颜色
        self.id=len(ball_list)                      #以ball_list的长度作为id    不需更新
        self.in_grid=[self.pos[0]-self.pos[0]%smooth_length,self.pos[1]-self.pos[1]%smooth_length]
        self.near_grids=[]                          #储存临近格子的id   不需即时更新
        self.near_dots=[]                           #储存临近粒子的id   不需即时更新
        self.nearest_dots=[]                        #储存影响域圆内粒子id 需即时更新

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
            #Csi-=1
            for i in self.nearest_dots:                                         #计算本身ni，式子3.27
                i=ball_list[i]                                                  #计算Laplace_Csi 式子3.55 3.33
                mid_term1 = nabla_kenel(self.pos,i.pos,smooth_length)
                d_pos=divide(minus(self.pos,i.pos),100)                         #计算△Xij 转换为m制
                mid_term2=2/i.rho*Csi/magenititude_simple(d_pos)
                print(mid_term2)
                exit()
                mid_term3=dot_product(d_pos,mid_term1)
                mid_term1 = times(mid_term1,Csi)
                ni = plus(ni,mid_term1)                                         #梯度叠加
                curvature+= mid_term2*mid_term3                                 #曲率叠加
            ni=divide(ni,self.rho)
            ni_leng=magenititude(ni)
            ni_unit=divide(ni,ni_leng)
            #print(self.id,ni_leng)
            if ni_leng>=layer_thick:                                            #用于判断粒子是否处于表层
                self.color=(100,0,0)                                            #对于处在表层的粒子，颜色变红作为标记
                surface_force=times(ni_unit,-curvature*sigma)                   #式子3.53
                return surface_force

            else:
                self.color=(255,255,255)                                        #不在表层的粒子恢复白色
                return [0,0]                                                    #不在表层，不受表面张力

    def acce_compute_another(self):
        print(self.id)
        self.acce=[0,0]                 #每次调用将原值清零
        for i in self.nearest_dots:
            i=ball_list[i]
            acc_pressure=times(nabla_kenel(self.pos,i.pos,smooth_length),i.mass*(self.pressure/self.rho**2+i.pressure/i.rho**2))
            #print(acc_pressure)
            self.acce=plus(self.acce,acc_pressure)

    def renew(self):                                #更新自己数据  需实时更新的数据
        self.find_near_grids_dots()
        self.find_nearest_dots()
        #self.acce=self.surface_tension()
        self.acce_compute()


def generate_grids():                               #网格生成函数   
    x,y=0,0
    while y<height+smooth_length:                   #生成网格并记录左上角顶点坐标
        while x<width+smooth_length:
            grid_list.append([x,y])                 #先以左上角坐标记录格子，然后生成一个空列表用以日后记录balls
            balls_in_grid_list.append([])           #为每个格子生成一个空列表用于记录其所含有的粒子
            x+=smooth_length
        y+=smooth_length
        x=0
def generate_dots():                                #根据函数绘制各种图形
    time_pass=clock.tick()/1000  
    x,n=0,0                                         #以屏幕最左侧中点为原点
    while x<=width:                                 #x到最右侧截止
        top=height/2-f(x)+f(x)%gap                  #由于pygame坐标系反了，这里函数值要做减法
        y=height
        while y>=0 and y>=top and y<=height:
            balls([x,y],[0,0],n,(255,255,255))
            n+=1
            y-=gap
        x+=gap
    time_pass=clock.tick()/1000  
    print('生成粒子%5d个，共用时%.4f秒'%(len(ball_list),time_pass))
def create_balls_rectan(m):                         #以方形生成小球
    start=(150,150)                                 #方框左上角
    end=(350,350)                                   #方框右下角
    x,y,n=start[0],start[1],1                       
    time_pass=clock.tick()/1000  
    while y<=end[1]:
        while x<=end[0]:
            '''if n==2:                                #奇数行小球错开一个身位  可将这三行注释掉，看看区别
                x+=m/2
                n=0  '''
            balls([x,y],[0,0],1,(255,255,255))
            x+=m
        y+=m
        n+=1
        x=start[0]
    for i in ball_list:
        i.renew()
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

    left_top=[mouse_pos[0]-smooth_length,mouse_pos[1]-smooth_length]                                    #影响域方框左上角坐标
    right_bot=[mouse_pos[0]+smooth_length,mouse_pos[1]+smooth_length]                                   #影响域方框右下角坐标
    left_top=times( quotient(left_top,(smooth_length,smooth_length) ),smooth_length)                    #取左上角的左上的格子顶点
    right_bot=times(quotient(right_bot,(smooth_length,smooth_length)),smooth_length)                    #取右下角的左上的格子顶点
                  
    y=left_top[1]
    while y<=right_bot[1]:                          #找出影响域方框内的点
        x=left_top[0]
        while x<=right_bot[0]:            
            try :                
                a=grid_list.index([x,y])            #如果(x,y)在pos_list中
            except ValueError:
                x+=smooth_length                  
                continue
            else:
                dots_within_domain+=balls_in_grid_list[a]                       #将粒子id添加入内
                x+=smooth_length
        y+=smooth_length

    for i in dots_within_domain:
        pygame.draw.circle(screen,(255,0,0),ball_list[i].pos,3)                 #红色标出 影响域方框 内粒子
        norma_kenel_result = norma_kenel(mouse_pos,ball_list[i].pos,smooth_length)
        if norma_kenel_result=='0' or ball_list[i].pos==list(mouse_pos):        #用于判定粒子是否处于影响域圆   
            continue
        else:
            pygame.draw.circle(screen,(0,255,0),ball_list[i].pos,ball_radius+2) #绿色标出 影响域圆 内粒子
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
    pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,normalize(times( gradient,-curvature ),100) ),5)     #划线
    #pygame.draw.line(screen,(255,255,255),mouse_pos,plus(mouse_pos,times(gradient,-curvature)),5)
    return gradient,final_tem,curvature

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
        pygame.draw.circle(screen,(0,0,255),converse_int(ball_list[i].pos),ball_radius+1)               #蓝色标出 鼠标所在格子 内粒子

    pygame.draw.circle(screen,(0,255,255),converse_int(ball_list[check_id].pos),10,2)                   #显示目前选中粒子的位置
    check_id_show=pygame.font.Font('freesansbold.ttf',30).render(str(check_id),1,(200,0,0))             #显示当前查看粒子的id
    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))           #显示鼠标位置
    screen.blit(check_id_show,(0,30))
    screen.blit(mouse_pos_show,(0,0))
    print(ball_list[check_id].acce)


def nearest_dot_tem(mouse_pos):                     #找到距离鼠标最近点的温度
    mouse_pos=pygame.mouse.get_pos()
    mouse_in_grid=[mouse_pos[0]-mouse_pos[0]%smooth_length,mouse_pos[1]-mouse_pos[1]%smooth_length]
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
#generate_dots()
create_balls_rectan(10)
#draw_tem_profile()
while 1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    for i in ball_list:                             #绘出粒子
        pygame.draw.circle(screen,i.color,(int(i.pos[0]),int(i.pos[1])),i.radius)
        
    pressed_mouse=pygame.mouse.get_pressed()        #得到鼠标按键状态
    mouse_pos=pygame.mouse.get_pos()                #得到鼠标位置
    if pressed_mouse[0]==1: 
        pygame.draw.circle(screen,(255,255,255),mouse_pos,int(smooth_length),1) # smooth_length 的网格间距画圆
        print(calculate_kenel(mouse_pos))
    if pressed_mouse[2]==1: 
        check_ball()

    nearest_dot_tem(mouse_pos)

    mouse_pos_show=pygame.font.Font('freesansbold.ttf',30).render(str(mouse_pos),1,(0,200,0))
    screen.blit(mouse_pos_show,(0,0))                                           #显示当前鼠标位置

    
    pygame.display.update()


#验证了光滑函数求偏导的可行性，第一核函数完全可行，下一步验证不规则粒子分布情况下是否仍然成立
#第一个核函数一直怀疑其准确性，日后都应使用2，3核函数
#由于程序模拟并未考虑与实际长度单位进行联系，所以h，h**2等运算需要自己处理数值
#v1.2  添加了求垂直于液面的向量的函数，目前运行良好，下一步添加判定其到底位于液面还是液内的函数，在下一步添加表面张力，设法合并两个函数
#v1.4  添加了表面张力的计算，测试运行良好。下一步根据q值进行液面粒子和液体内部粒子判定，再将其整合到主函数中。
#v1.5  完善了部分计算，应该可以添加进主函数了，但未添加判断粒子是否处于表面的函数
#v1.6  统一了两个程序所使用的变量与函数，现在可以认为一个是静态调试，另一个是动态调试

#日后希望统一两个程序所用的函数，包括但不限于以下函数
#三个核函数、check_balls、create_balls_rectan、create_balls_random、generate_balls、generate_dots
#统一两个程序所用的变量                                 已完成
#下一步尝试直接将两个程序公用的部分做成库