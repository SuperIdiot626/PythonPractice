import os
import numpy as np
import matplotlib.pyplot as plt
import math

chord = 0.5334

objFilePath = r'C:\Users\WYZ\Documents\WeChat Files\wxid_jrgz7252a1xb22\FileStorage\File\2022-05\newGeometry.obj'
##从obj提取出冰形坐标
with open(objFilePath) as file:
    points = []
    while 1:
        line = file.readline()
        if not line:
            break
        strs = line.split(" ")
        if strs[0] == "v":
            points.append((float(strs[1]), float(strs[2]), float(strs[3])))
        if strs[0] == "vt":
            break
# points原本为列表，需要转变为矩阵，方便处理        
Points = np.array(points)#处于乱序分布
Points = Points[:,:2]
print(Points)

points = []
for i in range(len(Points[:,0])):
    if Points[i,0]<chord/2:
        points.append(Points[i,:])
        
points = np.array(points)

##将点集按顺序排列
def length(x,y):
    d1=((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
    return d1

#按上下分类
points_up = []
points_down = []
for i in range(len(points[:,0])):
    if points[i,1]>=0:
        points_up.append(points[i,:])
    else:
        points_down.append(points[i,:])
        
points_up = np.array(points_up)
points_down = np.array(points_down)

while 1:
    flag = 0
    for i in range(len(points[:,0])-3):
        p1 = points[i,:]
        p2 = points[i+1,:]
        p3 = points[i+2,:]
        p4 = points[i+3,:]
        p = np.array([p1,p2,p3,p4])
        plt.plot(p[:,0],p[:,1])
        plt.scatter(p[:,0],p[:,1])
        #plt.show()
        d1 = length(p1,p2) + length(p2,p3) + length(p3,p4)
        d2 = length(p1,p3) + length(p2,p3) + length(p2,p4)
        if d1>d2:
            points[[i+1, i+2],:] = points[[i+2, i+1],:]
            flag = 1
            break
    if flag == 0:
        break
#plt.plot(points[:,0],points[:,1])