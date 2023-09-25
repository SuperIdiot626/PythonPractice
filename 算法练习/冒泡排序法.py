#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

# Author WangYizhuang
# 2021年11月24日09:38:50

import random

# myList=list(range(100))
# random.shuffle(myList)
# print(myList)
myList5  =[ 56, 20, 84, 66, 13]
myList10 =[  8,  2,  3,  9,  7,  1,  5,  6,  0,  4]
myList100=[ 13, 47, 70, 11, 85, 91, 28, 44, 86, 22, 37, 64, 77, 33, 88, 81,  9, 38, 68, 66,
            74, 61,  2, 31, 67, 83, 35, 79, 40, 26, 53,  4,  1, 90, 18, 82, 51, 14, 15, 97,
            34, 42, 75, 20,  7, 98, 19, 84, 95, 63, 76, 30, 52, 60, 59, 78, 93, 71, 23, 45,
            58, 21, 12,  5, 32, 56, 17, 55, 48, 99, 29, 80, 69, 73,  6, 89, 10,  3, 24, 94,
            36, 16,  0, 65, 92, 41, 72, 62, 49, 96, 87, 39, 27, 25, 57, 43, 54, 46,  8, 50]  



def buble01(myList):                        #针对每个固定元素，比较后交换位置
    #print(myList)
    length=len(myList)                      #先找出长度
    times=0                                 #统计计算次数
    start=0                                 #起始比较的位置
    while start<length:                     #在起始比较位置小于总长度的时候
        i,j=start,start+1                   #i为比较主体，j为被比较对象
        while j<length:                     #在被比较对象取到最后一位之前
            if myList[i]>myList[j]:         #i大于j的时候
                myList[j],myList[i]=myList[i],myList[j] #交换位置
                i=j                         #同时交换下标
                j+=1                        #下一个比较对象还是放在交换之后下一位
            else:
                j+=1                        #如果不做交换，则找下一位比较对象
            times+=1
            #print(myList)                   #输出一下本次排序结果
        if i==start and j==length:          #如果对于某一起始位置，已经排序完毕，则起始位置加一
            start+=1
    #check(myList)                           #输出最后结果以便检查
    print(times)                            #输出计算次数








def buble02(myList):                        #永远比较相邻的两组
    #print(myList)
    length=len(myList)                      #先找出长度
    times=0                                 #统计计算次数

    end=length                              #起始比较的位置
    while end>0:                            #在起始比较位置小于总长度的时候
        i=0
        while i<end-1:                      #在被比较对象取到最后一位之前
            if myList[i]>myList[i+1]:       #i大于j的时候
                myList[i],myList[i+1]=myList[i+1],myList[i] #交换位置
            i+=1
            times+=1
            #print(myList)                  #输出一下本次排序结果
        #times+=1
        end-=1

    #check(myList)                           #输出最后结果以便检查
    print(times)                            #输出计算次数


def buble03(myList):                        #已经与标准算法一致了
    #print(myList)
    length=len(myList)                      #先找出长度
    times=0                                 #统计计算次数

    for end in range(length,-1,-1):     
        for i in range(end-1):              #在被比较对象取到最后一位之前
            if myList[i]>myList[i+1]:       #i大于j的时候
                myList[i],myList[i+1]=myList[i+1],myList[i] #交换位置
            times+=1
            #print(myList)                  #输出一下本次排序结果
        #times+=1

    #check(myList)                           #输出最后结果以便检查
    print(times) 



def buble_standard(myList):                        #永远比较相邻的两组
    #print(myList)
    length=len(myList)                      #先找出长度
    times=0                                 #统计计算次数

    for i in range(length-1,-1,-1):
        for j in range(i):
            if myList[j]>myList[j+1]:       #i大于j的时候
                myList[j],myList[j+1]=myList[j+1],myList[j] #交换位置
            times+=1
            #print(myList)                   #输出一下本次排序结果
        #times+=1

    #check(myList)                           #输出最后结果以便检查
    print(times)                            #输出计算次数


def check(myList):
    a=0
    for i in myList:
        print('%4d'%i,end=' ')
        a+=1
        if a%10==0:
            print('')
    if a<=10:
        print('')

#buble01(myList100)
#buble02(myList100)
#buble03(myList100)
buble_standard(myList100)


#经验：将所有的while循环改为for循环，能减少代码量