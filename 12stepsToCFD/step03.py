# -*- coding: utf-8 -*-
import  numpy                       #here we load numpy
import  time, sys                   #and load some utilities
from    matplotlib import pyplot as plt   #here we load matplotlib

nx = 41                 # space discretion number
length = 2              # total length of computation space
dx = length / (nx-1)    # distance of each grid points      
nt = 20                 # total time steps
nu = 0.3                # the value of viscosity
sigma = 0.2             # sigma is a parameter, we'll learn more about it later ???
dt = sigma * dx**2 / nu # dt is defined using sigma ... more later!
print('dt=%f'%dt)




u = numpy.ones(nx)      #numpy function ones()  create a vector full of 1
u[int(0.5 /dx):int(1/dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as I.C.s
print(u)                #output for check


un = numpy.ones(nx)     #initialize a temporary array

for n in range(nt):     #time 
    un = u.copy()       #copy the existing values of u into un
    for i in range(1, nx-1):      #space, if not -1, index would exceed, which causes error
        u[i] = un[i]+nu*dt/dx**2*(un[i+1] + un[i-1] - 2*un[i] )
    
    if n%5==0:          #decide where to save a pic
        plt.plot(numpy.linspace(0, 2, nx), u)
        plt.savefig('41.jpg',bbox_inches='tight')   
    print(n) 

plt.plot(numpy.linspace(0, 2, nx), u)
plt.show()              #show the pic