from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots
import time


import numpy
from matplotlib import pyplot, cm
#%matplotlib inline  #???

###variable declarations


x_length=2
y_length=2

nx = 101     # x grid points number
ny = 101     # x grid points number
nt = 80   # time steps
c = 1       # wave speed
dx = x_length / (nx - 1)   #grid length in x
dy = y_length / (ny - 1)   #gird length in y
sigma = 0.2
dt = sigma * dx  #

x = numpy.linspace(0, x_length, nx)
y = numpy.linspace(0, y_length, ny)

u   = numpy.ones((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为1
un  = numpy.ones((ny, nx))      ##     
v   = numpy.ones((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为1
vn  = numpy.ones((ny, nx))               
X,Y = numpy.meshgrid(x, y)      #XY为输出的坐标矩阵，x,y为横纵坐标的数量值

###Assign initial conditions
##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5/dy):int(1/dy+1),int(.5/dx):int(1/dx+1)] = 1.5 
v[int(.5/dy):int(1/dy+1),int(.5/dx):int(1/dx+1)] = 0.5

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)


time_start=time.time()

'''row, col = u.shape              #u.shape得到的是u的横向纵向长度，这一步并不需要放在循环内
for n in range(nt + 1):         ##loop across number of time steps
    un = u.copy()
    vn = v.copy()
    #print('%d/%d'%(n,nt))       #进度条
    for j in range(1, row):     #先循环y坐标
        for i in range(1, col): #循环x坐标
            u[j, i] = (un[j, i] - (un[j, i] * dt / dx * (un[j, i] - un[j, i - 1])) -
                                  (vn[j, i] * dt / dy * (un[j, i] - un[j - 1, i])))
            v[j, i] = (vn[j, i] - (un[j, i] * dt / dx * (vn[j, i] - vn[j, i - 1])) -
                                  (vn[j, i] * dt / dy * (vn[j, i] - vn[j - 1, i])))
            u[ 0, :] = 1        #设置四条边界上都是1，用处？？？,u和v的边界设定值与计算新值是否有先后顺序？
            u[-1, :] = 1
            u[ :, 0] = 1
            u[ :,-1] = 1
            v[ 0, :] = 1
            v[-1, :] = 1
            v[ :, 0] = 1
            v[ :,-1] = 1'''


for n in range(nt + 1):         ##新的循环项，大大降低了运算时间。
    un = u.copy()
    vn = v.copy()
    u[1:, 1:] = (un[1:, 1:] - (un[1:, 1:]*dt/dx* (un[1:, 1:]-un[1:  , 0:-1]))   #运算解析：uu[1:, 1:]代表横纵坐标都从1开始直到最后一个，可以1：-1，从第一个到最后一个（不包含），或者0:从第0个到最后一个（包含）
                            - (vn[1:, 1:]*dt/dy* (un[1:, 1:]-un[0:-1, 1:  ])))
    v[1:, 1:] = (vn[1:, 1:] - (un[1:, 1:]*dt/dx* (vn[1:, 1:]-vn[1:  , 0:-1]))
                            - (vn[1:, 1:]*dt/dy* (vn[1:, 1:]-vn[0:-1, 1:  ])))
    u[ 0, :] = 1                ##设置四条边界上都是1，用处？？？,u和v的边界设定值与计算新值是否有先后顺序？
    u[-1, :] = 1
    u[ :, 0] = 1
    u[ :,-1] = 1
    v[ 0, :] = 1
    v[-1, :] = 1
    v[ :, 0] = 1
    v[ :,-1] = 1

time_end=time.time()
print('totally cost',time_end-time_start)


fig1 = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig1.gca(projection='3d')
surf1 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig2 = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig2.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, v[:], cmap=cm.viridis)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')




###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
                       

pyplot.show()