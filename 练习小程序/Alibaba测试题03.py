#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import A


xielvSum={}
lineNum=0

lineIndexSum=[]

lineNum=int(input())
for _ in range(lineNum):
    lineIndex=input().split()
    lineIndex=list(lineIndex)
    for __ in range(3):
        lineIndex[__]=int(lineIndex[__])
    lineIndexSum.append(lineIndex)
    xielv=lineIndex[1]/lineIndex[0]
    if xielvSum.get(xielv):
        xielvSum[xielv]+=1
    else:
        xielvSum[xielv]=1
num_xielv=len(xielvSum)
result=num_xielv*(num_xielv-1)/2
print(xielvSum)
for value in xielvSum.values():
    if value!=1:
        a=(value-1)*(lineNum-value)
        result+=a
        print(a)
print(result)