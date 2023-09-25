__author__ = 'Administrator'
import math
from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
M_PI = math.pi
fig = plt.figure(figsize=(6.0,6.0))
def main():
    global rho0,nx,ny,n,h,h2,k,mu,g,dt,DAMP,XMIN,XMAX,YMIN,YMAX,radius,H,C5,rho07
    rho0 = 1000.0
    H = 1
    nx = 20
    ny = 20
    n = nx * ny
    h = 0.5
    h2 = h * h
    k = 1000.0
    mu = 0.1
    g = 9.81
    dt = 0.0001
    DAMP = 0.75
    XMIN = 0.0
    XMAX = 4.0
    YMIN = 0.0
    YMAX = 4.0
    radius = 0.025
    C5 = rho0*200*g*H/7
    rho07 = pow(rho0,7)
    # 初始化位置
    position = init_position()
    # 初始化密度，需要粒子位置信息
    rho = init_compute_density(position)
    # 初始化质量，需要粒子密度信息
    mass = normalize_mass(rho)
    #将所有粒子物理信息储存在粒子列表 particle 中
    particle = []
    for i in range(n):
        p = Particle(mass[i], rho[i], position[2*i+0], position[2*i+1], vhx=0, vhy=0, vx=0,vy=0, ax=0, ay=-g)
        particle.append(p)
        #print(p.mass,p.rho)

    # 计算粒子的受力加速度
    particle = compute_accelation(particle)
    # 计算粒子第一个时间步里面的速度和位移，需要粒子加速度信息
    particle = leapfrog_start(particle)
    # 更新位置，进行位置检测，如果超出边界，则位置就固定在边界上，速度反向
    particle = reflect_bc(particle)

    for i in range(1):
        # 根据更新过的粒子位置，重新计算粒子的密度
        rho = compute_density(particle)
        mass = normalize_mass(rho)
        for i in range(n):
            particle[i].rho = rho[i]
            particle[i].mass = mass[i]
        particle = compute_accelation(particle)
        particle = leapfrog_step(particle)
        particle = reflect_bc(particle)
    ax = fig.add_subplot(111)
    for i in range(n):
        cir1 = Circle(xy = (particle[i].x, particle[i].y), radius=0.025, alpha=1)
#第一个参数为圆心坐标，第二个为半径 #第三个为透明度（0-1）
        ax.add_patch(cir1)
    plt.xlim((0, 4))
    plt.ylim((0, 4))
    plt.xlabel('width')
    plt.ylabel('height')
    my_x_ticks = np.arange(0, 4.2, 0.2)
    my_y_ticks = np.arange(0, 4.2, 0.2)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.show()
def init_position():
    position = []
    for i in range(nx):
        for j in range(ny):
            position.append(0.025+0.05*i) # 初始化粒子 x 坐标
            position.append(0.025+0.05*j) # 初始化粒子 x 坐标
    return position


# 初始化粒子密度
def init_compute_density(position):
    rho = np.ones(n)
    H = 0.5
    for i in range(n):
        y = position[2*i+1]
        B = 1 + 7*(H-y)/(200*H)
        rho[i] *= rho0*pow(B,1/7)
    return rho


def normalize_mass(rho):
    mass = np.ones(n)
    rho2s = 0
    rhos = 0
    for i in range(0,n):
        rho2s += (rho[i])*(rho[i])
        rhos += rho[i]
        mass[i] *= rho0*rhos / rho2s
    return mass


def compute_accelation(p):
    a = np.ones(2*n)
    for m in range(n):
        a[2*m+0] = 0.0
        a[2*m+1] = -g
    for i in range(n):
        xi,yi,rhoi = p[i].x, p[i].y, p[i].rho
        vxi,vyi = p[i].vx, p[i].vy
        psi = C5*(pow((rhoi/rho0),7)-1)
        # 可变光滑长度
        hi = h*pow((rho0/rhoi),0.5)
        for j in range(i+1,n):
            xj, yj, rhoj, massj = p[j].x, p[j].y , p[j].rho, p[j].mass
            vxj, vyj = p[j].vx, p[j].vy
            
            psj = C5*(pow((rhoj/rho0),7)-1)
            psij = psi/(rhoi*rhoi) + psj/(rhoj*rhoj)

            dvx = vxi - vxj     #速度差
            dvy = vyi - vyj

            dx = xi - xj        #位置差
            dy = yi - xj
            r2 = dx*dx + dy*dy  #模长平方
            r = math.sqrt(r2)   #模长
            R = r/hi
            R2 = R*R

            e1 = 4*mu*massj/(rhoi+rhoj) 
            e2 = r2+0.01*hi*hi

            C1 = 15/(7*M_PI*hi*hi)      #核函数αD
            C3 = 15/(14*M_PI*hi*hi)

            if (R>=0) and (R<=1):
                w0 = -massj*psij*C1*(-2*R+1.5*R2)
                w1 = e1*C1*(-2*R+1.5*R2)/(e2*rhoi)
                a[2*i+0] -= (w0 + w1*dvx*dx)
                a[2*i+1] -= (w0 + w1*dvy*dy)
                a[2*j+0] += (w0 + w1*dvx*dx)
                a[2*j+1] += (w0 + w1*dvy*dy)
            if (R>1) and (R<=2):
                w0 = -rhoi*massj*psij*(-C3)*(2-R)*(2-R)
                w1 = e1*(-C3)*(2-R)*(2-R)/(e2*rhoi)
                a[2*i+0] -= (w0 + w1*dvx*dx)
                a[2*i+1] -= (w0 + w1*dvy*dy)
                a[2*j+0] += (w0 + w1*dvx*dx)
                a[2*j+1] += (w0 + w1*dvy*dy)
    for m in range(n):
        p[m].ax = a[2*m+0]
        p[m].ay = a[2*m+1]
    return p


def leapfrog_start(p):
    for i in range(0,n):
        x,y = p[i].x,p[i].y
        vx,vy,vhx,vhy = p[i].vx, p[i].vy, p[i].vhx, p[i].vhy
        ax,ay = p[i].ax, p[i].ay
        vhx = vx + ax * dt/2
        vhy = vy + ay * dt/2
        vx += ax * dt
        vy += ay * dt
        x += vhx * dt
        y += vhy * dt
        p[i].x, p[i].y = x, y
        p[i].vx, p[i].vy, p[i].vhx, p[i].vhy = vx, vy, vhx, vhy
    return p


def leapfrog_step(p):
    for i in range(0,n):
        x,y = p[i].x, p[i].y
        vx,vy,vhx,vhy = p[i].vx, p[i].vy, p[i].vhx, p[i].vhy
        ax,ay = p[i].ax, p[i].ay
        vhx += ax * dt
        vhy += ay * dt
        vx = vhx + ax * dt/2
        vy = vhy + ay * dt/2
        x += vhx * dt
        y += vhy * dt
        p[i].x, p[i].y = x,y
        p[i].vx, p[i].vy, p[i].vhx, p[i].vhy = vx,vy,vhx,vhy
    return p


def compute_density(p):
    rho = np.zeros(n)
    for i in range(0,n):
        for j in range(i+1,n):
            xj, yj = p[j].x, p[j].y
            massj, rhoj = p[j].mass, p[j].rho
            rho[j] = rhoj
            vxj, vyj = p[j].vx, p[j].vy

            dvx = vxi - vxj             #这几行代码 求的是速度差及其模长
            dvy = vyi - vyj
            dv = math.sqrt(dvx*dvx + dvy*dvy)

            dx = xi - xj                #这几行代码是求两粒子之间的距离
            dy = yi - yj                
            r2 = dx*dx + dy*dy          #学姐喜欢用r2 代表 r**2
            r = math.sqrt(r2)           

            R = r/hi                    #hi是光滑长度 R是距离除以光滑长度
            R2 = R*R                       

            z1 = -2*R+1.5*R2            # 核函数的一次偏导  0<r<=1  似乎求错了
            z2 = (2-R)*(2-R)            # 核函数的一次偏导  1<r<=2

            C1 = 15/(7*M_PI*hi*hi)      #核函数前边的 αD 
            C3 = 15/(14*M_PI*hi*hi)     #核函数前边的 αD 

            if (R >= 0)and(R <= 1) :
                rho_ij = C1*massj*z1*rhoi*dv/rhoj   # 核函数的一次偏导
                rho[i] += rho_ij*dt
                rho[j] += rho_ij*dt
            if (R > 1)and(R <= 2):
                rho_ij = -C3*massj*z2*rhoi*dv/rhoj
                rho[i] += rho_ij*dt
                rho[j] += rho_ij*dt
    return rho


def reflect_bc(p):
    for i in range(n):
        x = p[i].x
        y = p[i].y
        vx,vy = p[i].vx,p[i].vy
        vhx,vhy = p[i].vhx,p[i].vhy
        if x <= XMIN+radius-1e-6 :
            x,vx,vhx = damp_reflect(vx,vhx,XMIN+radius-1e-6)
        if x >= XMAX-radius+1e-6:
            x,vx,vhx = damp_reflect(vx,vhx,XMAX-radius+1e-6)
        if y <= YMIN+radius-1e-6 :
            y,vy,vhy = damp_reflect(vy,vhy,YMIN+radius-1e-6)
        if y >= YMAX-radius+1e-6:
            y,vy,vhy = damp_reflect(vy,vhy,YMAX-radius+1e-6)
    p[i].x,p[i].y,p[i].vx,p[i].vy,p[i].vhx,p[i].vhy = x,y,vx,vy,vhx,vhy
    return p


def damp_reflect(v,vh,barrier):
    x = barrier
    v = -v
    vh = -vh
    v *= DAMP
    vh *= DAMP
    return x,v,vh


def reflect_particle(p):
    for i in range(n):
        xi = p[i].x
        yi = p[i].y
        #vxi,vyi = p[i].vx,p[i].vy
        #vhxi,vhyi = p[i].vhx,p[i].vhy
        for j in range(i+1,n):
            xj = p[j].x
            yj = p[j].y
            vxj,vyj = p[j].vx,p[j].vy
            vhxj,vhyj = p[j].vhx,p[j].vhy
            dx = (xi-xj)
            dy = (yi-yj)
            if dx < (2*radius)+1e-20 :
                vxj *= DAMP
                vhxj *= DAMP
                if vxj > 0 :
                    xj -= vxj*0.5*dt
                if vxj < 0 :
                    xj += vxj*0.5*dt
                if vxj == 0 and dx > 0 :
                    xj = xi - (2*radius)
                if vxj == 0 and dx < 0 :
                    xj = xi + (2*radius)
            if dy < (2*radius)+1e-20:
                vyj *= DAMP
                vhyj *= DAMP
                if vyj > 0 :
                    yj -= vyj*0.5*dt
                if vyj < 0 :
                    yj += vyj*0.5*dt
                if vyj == 0 and dy > 0 :
                    yj = yi - (2*radius)
                if vyj == 0 and dy < 0 :
                    yj = yi + (2*radius)
            p[j].x,p[j].y,p[j].vx,p[j].vy,p[j].vhx,p[j].vhy = xj,yj,vxj,vyj,vhxj,vhyj
if __name__ == '__main__':
    main()