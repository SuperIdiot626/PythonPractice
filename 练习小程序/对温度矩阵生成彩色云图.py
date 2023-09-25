import os
import pygame
pygame.init()


print('***输出温度云图***')


TargetDir=input('请输入目标文件所在路径：')

midterm=''
TargetDir=TargetDir.split('\\')                 #将源文件名字按照‘\’进行分割
for i in TargetDir:
    midterm=midterm+i+r'\\'
TargetDir=midterm[:-2]
os.chdir('D:\Code\C')
#os.chdir(TargetDir)



dataFile='7.dat'
file=open(dataFile,'r')                         #读取名为file.dat的文件
wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt,每一行为一个数组
broken=1                                        #用来判断是否中途推出循环
dataNumber=''                                   #数据中的单独数字
lines=[]                                        #一次性读取源文件的每一行

nDof=len(wholeTxt)                              #读取行数，即自由度
maxTemPos=nDof//2                               #温度最高点的位置，位于温度场中心

print(maxTemPos)


j=0
for n in wholeTxt:
    lines.append([])                            #添加新行用于储存数据
    for i in n:
        if i=='\n':                             #遇到换行符，说明一行结束
            j=j+1                               #换行
            dataNumber=''
            break                               #进入下一个循环
        if i==' ':                              #遇到空格，说明一个数字结束
            if dataNumber!='':                  #如果已读取数据不为空，则说明一个数据读取完毕，反之则继续
                lines[j].append(float(dataNumber))             #如果dataNumber为空格，则说明这一个数据已经到头了，对起进行记录并清空
                dataNumber=''
        else:
            dataNumber=dataNumber+i             #先记录每行的数字

maxTem=lines[maxTemPos][maxTemPos]
print(maxTem)
file.close






color_table=pygame.Surface((nDof,nDof),depth=24)
for x in range(nDof):
    for y in range(nDof):
        color_ratio=lines[x][y]/maxTem
        if color_ratio<0.25:
            r=0
            g=0
            b=(0.5-color_ratio)/0.5*255
        elif color_ratio<0.5:
            r=0
            g=(color_ratio-0.25)/0.25*255
            b=(0.5-color_ratio)/0.5*255
        elif color_ratio<0.75:
            r=(color_ratio-0.5)/0.5*255
            g=(0.75-color_ratio)/0.25*255
            b=0
        else:
            r=(color_ratio-0.5)/0.5*255
            g=0
            b=0
        r=int(r)
        g=int(g)
        b=int(b)
        print(r,g,b)
        color_table.set_at((x,y), (r, g, b))
pygame.image.save(color_table, dataFile+".png")


