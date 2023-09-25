import os
import numpy as np
import matplotlib.pylab as plt
import math

def plotAndPoints(objFilePath,showPic=1):
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

    Xmax=-np.Infinity
    pointIndex=0
    for i in range(len(result)):
        if points[result[i]-1][1]>0:
            if points[result[i]-1][0]>Xmax:
                Xmax=points[result[i]-1][0]
                pointIndex=result[i]-1

    result.pop()
    result01=[]
    while 1:
        a=result.pop()
        result01.append(a)
        if a==pointIndex+1 or (not result):
            break
    result=result[::-1]+result01

    pointsresult=[]
    for i in result:
        pointsresult.append(points[i-1])

    pointsresult = np.array(pointsresult)
    
    if showPic==1:
        plt.scatter(pointsresult[:,0],pointsresult[:,1])
        plt.plot   (pointsresult[:,0],pointsresult[:,1])
        plt.show()
    return pointsresult



Path = r'D:\Code\Python\练习小程序\李姚的测试代码\newGeometry01.obj'
plotAndPoints(Path)
Path = r'D:\Code\Python\练习小程序\李姚的测试代码\newGeometry02.obj'
plotAndPoints(Path)