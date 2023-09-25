#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

# Author WangYizhuang
# 2021年11月24日12:02:59

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

def choose01(myList,order=1):
    length=len(myList)
    times=0
    for i in range(length):
        pass
    if order!=1:
        myList.reverse()
    pass

def check(myList):
    a=0
    for i in myList:
        print('%4d'%i,end=' ')
        a+=1
        if a%10==0:
            print('')
    if a<=10:
        print('')

#choose01(myList100)
#choose02(myList100)
#choose03(myList100)
choose_standard(myList100)


#经验：将所有的while循环改为for循环，能减少代码量