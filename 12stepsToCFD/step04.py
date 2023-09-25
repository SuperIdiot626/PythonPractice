# -*- coding: utf-8 -*-
import  numpy,sympy,time, sys          # load some utilities
from matplotlib import pyplot as plt   # here we load matplotlib
from sympy import init_printing
from sympy.utilities.lambdify import lambdify
init_printing(use_latex=True)



def showlist(list,linenumber):                      #自己定义了个函数，用于输出某一向量
    for i,j in enumerate(list) :                    #每行五个，先输出u
        if i%linenumber==0:
            print('\nline %2d:'%(i//5+1),end=' ')   
        print('%.5f'%float(j),end='  ')             #<class 'numpy.float64'>无法使用%f等格式直接输出，需要先进行格式转化
        if i==0:
            continue


x, nu, t = sympy.symbols('x nu t')                  #set x, nu, t variable symbols, which can be used in LaTex
phi = (
        sympy.exp(-(x-4*t)**2/(4*nu*(t+1))) +       #phi=Φ, pi=π 
        sympy.exp(
                    -(x-4*t-2*sympy.pi)**2/(4*nu*(t+1))
                 )
       )
phiprime=phi.diff(x)                                #direct partial derivative !!! 非常牛逼的功能，自动求导
print(phiprime)
u = -2 * nu * (phiprime/phi) + 4
ufunc = lambdify((t, x, nu), u)                     #匿名函数，将t，x，nu代入得到u，如u定义式，x，t，nu现为字母变量，无具体值
#print(ufunc(1, 4, 3))                              #将1,4,3作为参数代入t,x,nu得到的u值为3.49070664...



###variable declarations    #在作为字母变量使用过后，重新赋值即可正常使用
tot_length = 2*numpy.pi     # total length of computation space
tot_time   = 0.5

nx =201                     # space discretion number    在nx取值过大时，会出现发散情况，max395，min386
#nt = 5000                  # total time steps
nu = 0.01                   # the value of viscosity

dx = tot_length/(nx-1)      # distance of each grid points      
dt = 0.00001                  #???
#dt = sigma * dx**2 / nu    # dt is defined using sigma ... more later!
#sigma = 0.2                # sigma is a parameter, we'll learn more about it later ???

nt =int(tot_time/dt)+1      # total time steps
print('dt=%f, nt=%f'%(dt,nt))


x = numpy.linspace(0, 2 * numpy.pi, nx)         #生成长度为nx，最小值0，最大值2pi的均匀分布的<class 'numpy.ndarray'>格式数据，与list相似。其元素格式为<class 'numpy.float64'>可被float、int等转化
un = numpy.empty(nx)                            #生成长度为nx的空numpy.ndarray，仅分配了储存空间，并未赋值，因此其中的值均为乱码，无法直接使用
t = 0
u = numpy.array([ufunc(t,x0,nu) for x0 in x])   #asarray作用类似指针，会随原始数据的变化而变化，但array会生成新的数据，即不碎原始数据的变化而变化。此处使用两者皆可
#plt.plot(x,u, marker='v', lw=1)                #将初始u值进行画图，以倒三角为标志
#showlist(u,5)



for n in range(nt):         #进行循环计算，即最后一个网格点的数据等于第一个网格点的数据。
    un = u.copy()
    for i in range(1, nx-1):
        u[i] =  (un[i]
                    - un[i]*dt/dx*(un[ i ] - un[i-1])
                    + nu*dt/dx**2*(un[i+1] - 2*un[i] + un[i-1])
                )
    u[0] =  (un[0]
                - un[0]*dt/dx*(un[0] - un[-2]) 
                + nu*dt/dx**2*(un[1] - 2*un[0] + un[-2])   #上中下三行为周期边界条件的计算，注释以取消周期边界条件
            )
    u[-1] = u[0]

    if n%50==0 and n>=500000:          #decide when to save a pic
        print(n)
        plt.plot(x,u, marker='o', lw=1)
        #plt.plot(numpy.linspace(0, tot_length, nx), u)

u_analytical = numpy.asarray([ufunc(nt * dt, xi, nu) for xi in x])  #对un进行又一次计算，用ufunc

plt.figure(figsize=(10, 10), dpi=100)
plt.plot(x,u,            marker='o', lw=4, label='Computational')   #label即图例名称，但需要配合plt.legend()进行显示
plt.plot(x,u_analytical, marker='^', lw=1, label='Analytical')
plt.legend()                    #显示图例
plt.show()