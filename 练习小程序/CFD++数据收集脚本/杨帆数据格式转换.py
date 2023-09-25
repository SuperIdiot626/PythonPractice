#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Wyz 

name_before='grid.dat'
name_after='change_grid.dat'





def qucikSort(numsold):                             #时间O(nlog(n))，空间O(1)
    nums=numsold[:]
    length=len(nums)
    if len(nums)<2:                                 #如果长度小于等于1，就直接返回
        return nums
    base=nums[0]                                    #以第一个值为标准值
    less=[]                                         #比标准值小的数列
    more=[]                                         #比标准值大的数列
    for i in nums[1:]:                              #开始对比 
        if i <base:
            less.append(i)                          #比标准值小的
        else:
            more.append(i)                          #比标准值大的
    return qucikSort(less)+[base]+qucikSort(more)   #调用自身，对子数列进行继续排列


file1=open(name_before,'r')
text=file1.readlines()
file1.close()

data=[]
for i in text:
    i=i.split()
    x=list(map(float,i))
    if x[-1]>=0:
        data.append(x)
data.sort(key=lambda data:data[0], reverse=True)



i=0
length=len(data)
file2=open(name_after,'w')

a=data[0]
while i < length-1:
    file2.write("2\n")
    b=data[i+1]
    file2.write("  %15.9e  %15.9e  %15.9e\n"%(a[0],a[1],a[2]))
    file2.write("  %15.9e  %15.9e  %15.9e\n"%(b[0],b[1],b[2]))
    a=b
    i=i+1
file2.close()