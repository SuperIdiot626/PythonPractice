import numpy,time
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots
#%matplotlib inline  #???

###variable declarations

convec_term =1      #对流项 零和一分别对应无和有
diffus_term =1      #扩散项 零和一分别对应无和有


c   = 1     # wave speed
rho = 1     # density
nu  = 0.1   # viscousity
dt  = 0.001 # time interval 

x_length =2
y_length =2

nx = 41     # x grid points number
ny = 41     # x grid points number
nt = 10000    # steps for time intergral
nit= 50     # steps for pressure space intergral

dx = x_length / (nx - 1)   #grid length in x
dy = y_length / (ny - 1)   #gird length in y

#sigma = 0.0009
#dt = sigma * dx*dy/nu  #

x = numpy.linspace(0, x_length, nx) #长度nx，最大最小值分别为0，x_length的线性分布向量
y = numpy.linspace(0, y_length, ny) 

u   = numpy.zeros((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为0
v   = numpy.zeros((ny, nx))      ##create a 1xn vector of 1's,创建ny*nx的矩阵，矩阵元素均为0
p   = numpy.zeros((ny, nx))
b   = numpy.zeros((ny, nx)) 

X,Y = numpy.meshgrid(x, y)      #XY为输出的坐标矩阵，x,y为横纵坐标的数量值


def build_up_b(b, rho, dt, u, v, dx, dy):
    b[1:-1, 1:-1] = (rho*
                        (
                        1/dt*(            #此处已经乘了-1
                            + (u[1:-1,2:  ] - u[1:-1,0:-2])/(2*dx) 
                            + (v[2:  ,1:-1] - v[0:-2,1:-1])/(2*dy)
                            ) 
                        -((u[1:-1,2:  ] - u[1:-1,0:-2])/(2*dx))**2
                        -((v[2:  ,1:-1] - v[0:-2,1:-1])/(2*dy))**2
                        -2*(
                            (u[2:  ,1:-1] - u[0:-2,1:-1])/(2*dy)*
                            (v[1:-1,2:  ] - v[1:-1,0:-2])/(2*dx)
                            )
                        )
                    )
    '''b[1:-1, 1:-1] = (rho*(1/dt*(
                    + (u[1:-1, 2:] - u[1:-1, 0:-2]) /(2 * dx) 
                    + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) 
                    -((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 
                    -((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2)
                    -2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                           (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx))
                    )'''
                    
    return b

def pressure_poisson(p, dx, dy, b):
    pn = numpy.empty_like(p)    #???
    pn = p.copy()
    for q in range(nit): 
        pn = p.copy()
        p[1:-1, 1:-1] = (1/2/(dx**2+dy**2)*
                            (
                            + dx**2*(pn[0:-2, 1:-1]+pn[2:  , 1:-1])
                            + dy**2*(pn[1:-1, 0:-2]+pn[1:-1, 2:  ])
                            - dx**2*dy**2*b[1:-1,1:-1]
                            )
                        )
        p[ :, -1] = p[ : ,-2 ]  # dp/dx = 0 at x = 2
        p[ 0, : ] = p[ 1 , : ]  # dp/dy = 0 at y = 0
        p[ :, 0 ] = p[ : , 1 ]  # dp/dx = 0 at x = 0
        p[-1, : ] = 0           # p = 0 at y = 2

    return p                    


def cavity_flow(nt, u, v, dt, dx, dy, p, rho, nu):
    global b   
    for n in range(nt + 1):         ##新的循环项，大大降低了运算时间。
        #print('%d/%d'%(n,nt))
        un = u.copy()
        vn = v.copy()  
        b = build_up_b(b, rho, dt, u, v, dx, dy)
        p = pressure_poisson(p, dx, dy, b)

        u[1:-1, 1:-1] = (un[1:-1, 1:-1]
                            - un[1:-1,1:-1]*dt/dx* (un[1:-1,1:-1]-un[1:-1,0:-2])*convec_term            #运算解析：uu[1:, 1:]代表横纵坐标都从1开始直到最后一个，可以1：-1，从第一个到最后一个（不包含），或者0:从第0个到最后一个（包含）
                            - vn[1:-1,1:-1]*dt/dy* (un[1:-1,1:-1]-un[0:-2,1:-1])*convec_term
                            + nu*dt/dx**2*(un[1:-1,2:  ] -2*un[1:-1,1:-1] +un[1:-1,0:-2])*diffus_term  #循环不会在某一个遍历完成后自动结束，因此参与循环的各项参数数量必须一致
                            + nu*dt/dy**2*(un[2:  ,1:-1] -2*un[1:-1,1:-1] +un[0:-2,1:-1])*diffus_term  #扩散项，由于要用到空间上的前一项和后一项，所以要对u的范围进行限定，对应的un也要进行范围调整
                            - 1/rho*dt/dx*(p[1:-1,2:  ] -p[1:-1,0:-2])/2
                            )                                                                           #注意，在代码中，下标*从右往左*为xyz，与数学习惯写法相反

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] 
                            - un[1:-1,1:-1]*dt/dx* (vn[1:-1,1:-1]-vn[1:-1,0:-2])*convec_term
                            - vn[1:-1,1:-1]*dt/dy* (vn[1:-1,1:-1]-vn[0:-2,1:-1])*convec_term
                            + nu*dt/dx**2*(vn[1:-1,0:-2] +vn[1:-1,2:  ] -2*vn[1:-1,1:-1])*diffus_term  #循环应该会在某一个遍历结束后自动结束，这样就不用指定un[1:,1:]的右边界了
                            + nu*dt/dy**2*(vn[0:-2,1:-1] +vn[2:  ,1:-1] -2*vn[1:-1,1:-1])*diffus_term
                            - 1/rho*dt/dy*(p[2:  ,1:-1] -p[0:-2,1:-1])/2
                            )
        
        u[ :, 0] = 0    # u=0 while x=0
        u[ :,-1] = 0    # u=1 while x=2
        u[ 0, :] = 0    # u=0 while y=0
        u[int(ny*0.4), :] = -1    # u=1 while y=2
        # u[int(ny*0.5), :] = +1    # u=1 while y=2
        u[int(ny*0.6), :] = +1    # u=1 while y=2
        v[ :, 0] = 0    # v=0 while x=0
        v[ :,-1] = 0    # v=0 while x=2
        v[ 0, :] = 0    # v=0 while y=0
        v[-1, :] = 0    # v=0 while y=2
        
    return u,v,p







time_start=time.time()
u, v, p = cavity_flow(nt, u, v, dt, dx, dy, p, rho, nu)
time_end=time.time()
print('totally cost',time_end-time_start)


'''fig = pyplot.figure(figsize=(11,7), dpi=100)
# plotting the pressure field as a contour
pyplot.contourf(X, Y, p, alpha=0.5, cmap=cm.viridis)  
pyplot.colorbar()
# plotting the pressure field outlines
pyplot.contour(X, Y, p, cmap=cm.viridis)  
# plotting velocity field
pyplot.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2]) 
pyplot.xlabel('X')
pyplot.ylabel('Y')'''

fig = pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.contourf(X, Y, p, alpha=0.5, cmap=cm.viridis)
pyplot.colorbar()
pyplot.contour(X, Y, p, cmap=cm.viridis)
pyplot.streamplot(X, Y, u, v)
pyplot.xlabel('X')
pyplot.ylabel('Y')



pyplot.show()