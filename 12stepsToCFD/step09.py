from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots
import time


import numpy
from matplotlib import pyplot, cm
#%matplotlib inline  #???

###variable declarations

convec_term =1      #对流项 零和一分别对应无和有
diffus_term =1      #扩散项 零和一分别对应无和有
calcu_u=1           #是否计算u，一般设为1不变
calcu_v=0           #是否计算v，看情况设为0或1


x_length =1
y_length =1

nx = 31    # x grid points number
ny = 31    # x grid points number
nt = 1000     # time steps
c = 1       # wave speed
nu = 0.01   #viscousity
dx = x_length / (nx - 1)   #grid length in x
dy = y_length / (ny - 1)   #gird length in y
sigma = 0.0009
dt = sigma * dx*dy/nu  #

x = numpy.linspace(0, x_length, nx) #长度nx，最大最小值分别为0，x_length的线性分布向量
y = numpy.linspace(0, y_length, ny) 

u   = numpy.ones((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为1
un  = numpy.ones((ny, nx))      ##     
v   = numpy.ones((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为1
vn  = numpy.ones((ny, nx))      
p   = numpy.zeros((ny, nx))  
pn  = numpy.zeros((ny, nx))           
X,Y = numpy.meshgrid(x, y)      #XY为输出的坐标矩阵，x,y为横纵坐标的数量值

###Assign initial conditions
##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2

u[int(.5/dy):int(1/dy+1),int(.5/dx):int(1/dx+1)] = 2 
v[int(.5/dy):int(1/dy+1),int(.5/dx):int(1/dx+1)] = 2

p[:, 0] = 0         #p=0 @ x=0
p[:,-1] = y         #p=y @ x=1
p[ 0,:] = p[ 1,:]   # dp/dy = 0 @ y = 0 因为最外边的一圈实际上未参与计算，所以要对外圈进行赋值
p[-1,:] = p[-2,:]   # dp/dy = 0 @ y = 1

fig1 = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig1.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, p, cmap=cm.viridis, rstride=1, cstride=1)
#ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')


time_start=time.time()



for n in range(nt + 1):         ##新的循环项，大大降低了运算时间。
    un = u.copy()
    vn = v.copy()
    pn = p.copy()

    '''u[1:-1, 1:-1] = (un[1:-1, 1:-1]
                        - un[1:-1,1:-1]*dt/dx* (un[1:-1,1:-1]-un[1:-1,0:-2])*convec_term          #运算解析：uu[1:, 1:]代表横纵坐标都从1开始直到最后一个，可以1：-1，从第一个到最后一个（不包含），或者0:从第0个到最后一个（包含）
                        - vn[1:-1,1:-1]*dt/dy* (un[1:-1,1:-1]-un[0:-2,1:-1])*convec_term
                        + nu*dt/dx**2*(un[1:-1,0:-2] +un[1:-1,2:  ] -2*un[1:-1,1:-1])*diffus_term  #循环不会在某一个遍历完成后自动结束，因此参与循环的各项参数数量必须一致
                        + nu*dt/dy**2*(un[0:-2,1:-1] +un[2:  ,1:-1] -2*un[1:-1,1:-1])*diffus_term  #扩散项，由于要用到空间上的前一项和后一项，所以要对u的范围进行限定，对应的un也要进行范围调整
                        )                                                                           #注意，在代码中，下标*从右往左*为xyz，与数学习惯写法相反

    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] 
                        - un[1:-1,1:-1]*dt/dx* (vn[1:-1,1:-1]-vn[1:-1,0:-2])*convec_term
                        - vn[1:-1,1:-1]*dt/dy* (vn[1:-1,1:-1]-vn[0:-2,1:-1])*convec_term
                        + nu*dt/dx**2*(vn[1:-1,0:-2] +vn[1:-1,2:  ] -2*vn[1:-1,1:-1])*diffus_term  #循环应该会在某一个遍历结束后自动结束，这样就不用指定un[1:,1:]的右边界了
                        + nu*dt/dy**2*(vn[0:-2,1:-1] +vn[2:  ,1:-1] -2*vn[1:-1,1:-1])*diffus_term
                        )'''

    p[1:-1, 1:-1] = (1/2/(dx**2+dy**2)*(
                        dx**2*(pn[0:-2, 1:-1]+pn[2:  , 1:-1])+
                        dy**2*(pn[1:-1, 0:-2]+pn[1:-1, 2:  ]))
                        )

    u[ 0, :] = 1    ##设置四条边界上都是1，用处？？？,u和v的边界设定值与计算新值是否有先后顺序？
    u[-1, :] = 1
    u[ :, 0] = 1
    u[ :,-1] = 1

    v[ :, 0] = 1    # v=1 while x=0
    v[ :,-1] = 1    # v=1 while x=2
    v[ 0, :] = 1    # v=1 while y=0
    v[-1, :] = 1    # v=1 while y=2
    

    p[:, 0] = 0         #p=0 @ x=0
    p[:,-1] = y         #p=y @ x=1
    p[ 0,:] = p[ 1,:]   #dp/dy=0 @ y=0
    p[-1,:] = p[-2,:]   #dp/dy=0 @ y=1

time_end=time.time()
print('totally cost',time_end-time_start)


fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, p, cmap=cm.viridis, rstride=1, cstride=1)
#ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')


###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
                       

pyplot.show()