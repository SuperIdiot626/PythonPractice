import os
import numpy as np
import matplotlib.pylab as plt
import math

##将点集按顺序排列
def length(x,y):
    d1=((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
    return d1


chord = 0.5334

objFilePath = r'D:\Code\Python\练习小程序\李姚的测试代码\newGeometry02.obj'
##从obj提取出冰形坐标
with open(objFilePath) as file:
    points = []
    rectangles=[]
    while 1:
        line = file.readline()
        if not line:
            break
        strs = line.split(" ")
        if strs[0] == "v":
            points.append((float(strs[1]), float(strs[2]), float(strs[3])))
        if strs[0] == "f":
            rectangles.append([int(strs[1]), int(strs[2])])
        if strs[0] == "vt":
            break



# for i in range(len(points)):
#     print('v',end=' ')
#     for j in points[i]:
#         print("%.10f"%j,end=' ')
#     print('')

# for i in range(len(rectangles)):
#     print('f',end=' ')
#     for j in rectangles[i]:
#         print("%4d"%j,end=' ')
#     print('')

# for i in range(len(rectangles)):
#     print(rectangles[i])

# for i in range(len(rectangles)):
#     #print(rectangles[i][-4])
#     print(points[rectangles[i][-4]-1][-1])
#     # if not (points[rectangles[i][0]-1][-4]>0):
#     #     print(rectangles[i][0]-1)
#     #     print('False')

# print(          rectangles[0][0]-1 )
# print(   points[rectangles[0][0]-1])
result =rectangles[0].copy()
while len(rectangles)!=1:
    for i in rectangles:
        if i[0]==result[-1]:
            result.append(i[-1])
            rectangles.remove(i)
            break
    for i in rectangles:
        if i[-1]==result[0]:
            result.insert(0,i[0])
            rectangles.remove(i)
            break        
            
print(result)
pointsresult=[]
for i in result:
    pointsresult.append(points[i-1])
print(pointsresult)

pointsresult = np.array(pointsresult)#处于乱序分布

plt.scatter(pointsresult[:,0],pointsresult[:,1])
plt.plot(pointsresult[:,0],pointsresult[:,1])
plt.show()