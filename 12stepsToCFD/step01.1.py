# -*- coding: utf-8 -*-
import  numpy                       #here we load numpy
import  time, sys                   #and load some utilities
from    matplotlib import pyplot as plt   #here we load matplotlib

nx = 200                 # space discretion number       
#IF nx is too big, the wave would be quicker than calculation, which causes divergence
length=2                # total length of computation space
dx = length / (nx-1)    # distance of each grid points      
nt = 20                 # total time steps
sigma=0.5
c = 1                   # wavespeed of c = 1
dt = sigma*dx/c               # time interval


u = numpy.ones(nx)      #numpy function ones()  create a vector full of 1
u[int(0.25*length /dx):int(0.5*length/dx + 1)] = 2  #setting u = 2 between 1/4 and 1/2 of total length as I.C.s
print(u)                #output for check


un = numpy.ones(nx)     #initialize a temporary array

for n in range(nt):     #time 
    un = u.copy()       #copy the existing values of u into un
    for i in range(1, nx):      #space
    #for i in range(nx):        #if 1 included the calculation will be a loop,f
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        #print(un[-1])
    if n%10==0:
        plt.plot(numpy.linspace(0, 2, nx), u)
        plt.savefig('41.jpg',bbox_inches='tight')   
    print(n) 

plt.plot(numpy.linspace(0, 2, nx), u)
plt.show()              #show the pic