#!/usr/bin/env python
# -*- coding: utf-8 -*-

targetfilename='infout1f.inp'  
file=open(targetfilename,'w')

BeginEnd="#------------------------\n"

StrEntryNum=1
StrEntryBegin='entry'+str(StrEntryNum)+' begin\n'

StrOutput='output coefficients\n'


Strifdim_1="ifdim 0\nnbcsel 1\n"
Strifdim_2="ifdim 0\nnbcsel 2\n"

#完整版
Strnbcsel_1=[11,12,13,14,15,16,                     #先6个喷口
            1,2,3,4]                                #后4个套筒

Strnbcsel_2=[ '11\n12','13\n14','15\n16',           #双喷喷口*3
                '1\n2','3\n4']                      #双喷套筒*2


#由于7，8喷管算的不好，因此把这部分删去 #共9个部件，该部分为9，10，11，12四个喷管和2个套筒
Strnbcsel_1=[13,14,15,16,                           #先4个喷口
            3,4]                                    #后2个套筒

Strnbcsel_2=[   '13\n14','15\n16',                  #双喷喷口*2
                '3\n4']                             #双喷套筒*1


#单独的7，8喷口
Strnbcsel_1=[5,6,                                   #先2个喷口
            1,2,]                                   #后2个套筒

Strnbcsel_2=[ '5\n6',                               #双喷喷口*1
                '1\n2',]                            #双喷套筒*1

#单独的9，10号喷管
Strnbcsel_1=[3,4]                                   #先2个喷口#后0个套筒

Strnbcsel_2=['3\n4',]                               #双喷喷口*2双喷套筒*1

# #单独的11，12喷口
# Strnbcsel_1=[5,6,                                   #先2个喷口
#             1,2,]                                   #后2个套筒

# Strnbcsel_2=[ '5\n6',                               #双喷喷口*1
#                 '1\n2',]                            #双喷套筒*1


StrMomentCenter="xcen 0.0\nycen 0.0\nzcen 0.0\n"

StrPRho=["pref 1.052\nrref 1.844110E-05\n",         #80  #与高度有关
         "pref 0.184\nrref 3.428600E-06\n",         #90
         "pref 0.032\nrref 5.711837e-07\n"]         #100

StrVelocity=[   1977.7660, 1917.0540, 1958.734,     #7Ma 80km 90km 100km
                2260.3014, 2190.9190, 2238.554,]    #8Ma 80km 90km 100km

StrLARef=r'''lxref 24.75
lyref 24.75
lzref 24.75
axref 84.3
ayref 84.3
azref 84.3
'''

StrAOA=["alpha 00\n","alpha 10\n","alpha 20\n","alpha 30\n","alpha 40\n",]

StrPlane="plane xy\n"

StrEntryEnd='entry'+str(StrEntryNum)+' end\n'

MachNumber=[0,1]

for JetsNum in [0,1]:
    if JetsNum==0:
        Strnbcsel=Strnbcsel_1
        Strifdim =Strifdim_1
    elif JetsNum==1:
        Strnbcsel=Strnbcsel_2
        Strifdim =Strifdim_2
    for part in Strnbcsel:              #先循环零部件
        for H in range(len(StrPRho)):               #再循环高度
            for Ma in MachNumber:     #马赫数
                for AOA in StrAOA:      #攻角
                    
                    StrEntryBegin='entry'+str(StrEntryNum)+' begin\n'
                    StrEntryEnd='entry'+str(StrEntryNum)+' end\n'
                    file.write(BeginEnd)
                    
                    file.write(StrEntryBegin)
                    file.write(StrOutput)
                    file.write(Strifdim)

                    file.write(str(part)+'\n')           #可能需要str转化

                    file.write(StrMomentCenter)

                    file.write(StrPRho[H])
                    vel=str(StrVelocity[H+3*Ma] )        #可能需要str转化
                    vel='uref '+vel+'\n'
                    file.write(vel)

                    file.write(StrLARef)

                    file.write(AOA)

                    file.write(StrPlane)
                    file.write(StrEntryEnd)
                    file.write(BeginEnd+'\n')
                    StrEntryNum+=1