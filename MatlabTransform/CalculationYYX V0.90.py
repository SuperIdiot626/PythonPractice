#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

# Author WangYizhuang
# Generated with SMOP  0.41

from typing import List
from numpy import *


V=[[0,0,0]]          #income flow velocity

# Data import
########################################来流条件输入开始########################################
'''V[0][0]=input('Vx:')
V[0][1]=input('Vy:')
V[0][2]=input('Vz:')
Ma=input('Ma:')
midu=input('来流密度：')
p_lailiu=input('来流压力：')
S_can=input('参考面积：')
L_can=input('参考长度：')
AttackAngle=input('攻角：')'''


V[0][0]=4871.833604
V[0][1]=0
V[0][2]=859.0098528
Ma=15
midu=0.00102688
p_lailiu=79.7791
AttackAngle=10
########################################来流条件输入结束########################################

top_folder='C:\\Users\\WYZ\\Desktop\\test'


########################################输入设计变量########################################
#定义设计变量因素
L=5                 #飞行器长度
number=1            #样本序号
n0=100
n1=50
Duozhui_N=number ** 11          #总排列组合数
qidongxishu=zeros((Duozhui_N,6))



print('样本数：%d'%Duozhui_N)
# L=input('行器总长:');
# number=input('请输入设计变量的水平数:');
L_can=L                         #参考长度=x方向长度

Wmax=zeros(Duozhui_N)           #每个截面的最大宽度
L1=zeros(Duozhui_N)             #多椎体第一锥的长度
L2=zeros(Duozhui_N)             #多椎体第二锥的长度


theta_u_1_deg=zeros(Duozhui_N)  #degree 
theta_l_1_deg=zeros(Duozhui_N)
theta_u_2_deg=zeros(Duozhui_N)
theta_l_2_deg=zeros(Duozhui_N)

theta_u_1=zeros(Duozhui_N)      #rad
theta_l_1=zeros(Duozhui_N)
theta_u_2=zeros(Duozhui_N)
theta_l_2=zeros(Duozhui_N)

Nc_u_1=zeros(Duozhui_N)         #上下表面型线参数  u为上表面，l为下表面，1,2为锥面号
Nc_l_1=zeros(Duozhui_N)
Nc_u_2=zeros(Duozhui_N)
Nc_l_2=zeros(Duozhui_N)

n=zeros(Duozhui_N)              #轮廓曲线控制参数


W1=zeros(n1)                    #第一锥每个截面宽度
Hu1=zeros(n1)                   #上高度
Hl1=zeros(n1)                   #下高度
y1=zeros((n1,n0))               #第一锥，各截面点y坐标  展向
x1=zeros(n1)                    #第一锥，各截面点x坐标  轴向
zu1=zeros((n1,n0))              #第一锥，各截面点z坐标  法向上
zl1=zeros((n1,n0))              #第一锥，各截面点z坐标  法向下

W2=zeros(n1)
Hu2=zeros(n1)
Hl2=zeros(n1)
y2=zeros((n1,n0))
x2=zeros(n1)
zu2=zeros((n1,n0))
zl2=zeros((n1,n0))

a_left=zeros(n0)
b_right=zeros(n0)
h=zeros(n0)
S_each=zeros(n0)



# test.m:31
for i in range(0,number):
    Wmax[i]=1.8
    L1[i]=1
    theta_u_1_deg[i]=3
    theta_l_1_deg[i]=1
    theta_u_2_deg[i]=6.5
    theta_l_2_deg[i]=3.5
    theta_u_1[i]=theta_u_1_deg[i]/180*pi
    theta_l_1[i]=theta_l_1_deg[i]/180*pi
    theta_u_2[i]=theta_u_2_deg[i]/180*pi
    theta_l_2[i]=theta_l_2_deg[i]/180*pi
    Nc_u_1[i]=3
    Nc_l_1[i]=0.5
    Nc_u_2[i]=0.5
    Nc_l_2[i]=2
    n[i]=0.55




# test.m:48
'''
for i in range(0,number):
    Wmax(i)= input('飞行器宽度:')
    L1(i)= input('第一锥长度:')
    theta_u_1_deg(i)= input('第一锥上半锥角(deg):')
    theta_l_1_deg(i)= input('第一锥下半锥角(deg):')
    theta_u_2_deg(i)= input('第二锥上半锥角(deg):')
    theta_l_2_deg(i)= input('第二锥下半锥角(deg):')
    #转化为弧度制
    theta_u_1[i]=theta_u_1[i]/180*pi
    theta_l_1[i]=theta_l_1[i]/180*pi
    theta_u_2[i]=theta_u_2[i]/180*pi
    theta_l_2[i]=theta_l_2[i]/180*pi

    Nc_u_1(i)= input('第一锥上表面型线控制参数:')
    Nc_l_1(i)= input('第一锥下表面型线控制参数:')
    Nc_u_2(i)= input('第二锥上表面型线控制参数:')
    Nc_l_2(i)= input('第二锥下表面型线控制参数:')
    n(i)=input('轮廓曲线控制参数:')'''



Duozhui_N=number ** 11          #总排列组合数
YangBen=zeros((Duozhui_N,11))   #

Duozhui_N_k=0
for i1 in range(0,number):
    for i2 in range(0,number):
        for i3 in range(0,number):
            for i4 in range(0,number):
                for i5 in range(0,number):
                    for i6 in range(0,number):
                        for i7 in range(0,number):
                            for i8 in range(0,number):
                                for i9 in range(0,number):
                                    for i10 in range(0,number):
                                        for i11 in range(0,number):
                                            YangBen[Duozhui_N_k]=[  Wmax[i1],
                                                                    L1[i2],
                                                                    theta_u_1[i3],
                                                                    theta_l_1[i4],
                                                                    theta_u_2[i5],
                                                                    theta_l_2[i6],
                                                                    Nc_u_1[i7],
                                                                    Nc_l_1[i8],
                                                                    Nc_u_2[i9],
                                                                    Nc_l_2[i10],
                                                                    n[i11]]
                                            Duozhui_N_k+=1
#print(YangBen)
###########x、y方向分别分成多少份###########



# test.m:100
############################################################滑翔升力体参数化############################################################
for i0 in range(0,Duozhui_N):
    ##########其他参数计算##########
    ###锥体剩余参数计算
    L2[i0]=L - YangBen[i0][1]
    Wmax1=YangBen[i0][0]/(L**YangBen[i0][10])*YangBen[i0][1]**YangBen[i0][10]
    ###划分截面所需的参数计算
    l=linspace(0,L,2*n1)
    l1=linspace(0,YangBen[i0][1],n1)
    l2=linspace(YangBen[i0][1],L,n1)
    x=zeros((2*n1,n0))
    ##########其他参数计算完成##########

    #.m116
    #第一、二锥飞行器参数化
    for i in range(0,n1):
        W1[i]=(YangBen[i0][0]
                /L    **YangBen[i0][10]
                *l1[i]**YangBen[i0][10]     #计算各截面宽度 
                )
        W2[i]=(Wmax                         #计算各截面宽度   ???
                /L    **YangBen[i0][10]
                *l2[i]**YangBen[i0][10]
                )  

        Hu1[i]=tan(YangBen[i0][2])* l1[i]   #计算各截面上曲线的高度
        Hl1[i]=tan(YangBen[i0][3])* l1[i]   #计算各截面下曲线的高度
        Hu2[i]=tan(YangBen[i0][4])*(l2[i]-YangBen[i0][1])  #计算各截面上曲线的高度
        Hl2[i]=tan(YangBen[i0][5])*(l2[i]-YangBen[i0][1])  #计算各截面下曲线的高度
        

        y1[i]=linspace(-W1[i]/2,W1[i]/2,n0)
        x1[i]=l1[i]
        y2[i]=linspace(-W2[i]/2,W2[i]/2,n0)
        x2[i]=l2[i]

        zu1[i]=(+Hu1[i]
                *(+y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][6]
                *(-y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][6]  
                *2.0**(2.0*YangBen[i0][6])
                )

        zl1[i]=(-Hl1[i]
                *(+y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][7]
                *(-y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][7]
                *2.0**(2.0*YangBen[i0][7])
                )

        zu2[i]=(Hu2[i]
                *(+y2[i]/W2[i] + 0.5*ones(n0))**(YangBen[i0][8])
                *(-y2[i]/W2[i] + 0.5*ones(n0))**(YangBen[i0][8])
                *2.0**(2.0*YangBen[i0][8])
                +zu1[n1-1]
                )

        zl2[i]=(-Hl2[i]
                *(+y2[i]/W2[i] + 0.5*ones(n0))**(YangBen[i0][9])
                *(-y2[i]/W2[i] + 0.5*ones(n0))**(YangBen[i0][9])
                *2.0**(2.0*YangBen[i0][9])
                +zl1[n1-1]
                )

        zu1[i][isnan(zu1[i])]=0             #替换NaN为0
        zl1[i][isnan(zl1[i])]=0
        zu2[i][isnan(zu2[i])]=0             #替换NaN为0
        zl2[i][isnan(zl2[i])]=0
    
    #.m132
    #第二锥飞行器参数化
        
    '''for i in range(0,n1):
        W1 [i]=(YangBen[i0][0]
                /L**YangBen[i0][10]
                *l1[i]**(YangBen[i0][10]) #计算各截面宽度 
                )
        Hu1[i]=tan(YangBen[i0][2])*l1[i]  #计算各截面上曲线的高度
        Hl1[i]=tan(YangBen[i0][3])*l1[i]  #计算各截面下曲线的高度
        y1[i]=linspace(-W1[i]/2,W1[i]/2,n0)
        x1[i]=l1[i]        
        zu1[i]=(+Hu1[i]
                *(+y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][6]
                *(-y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][6]  
                *2.0**(2.0*YangBen[i0][6])
                )
        
        zl1[i]=(-Hl1[i]
                *(+y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][7]
                *(-y1[i]/W1[i] + 0.5*ones(n0))**YangBen[i0][7]
                *2.0**(2.0*YangBen[i0][7])
                )

        zu1[i][isnan(zu1[i])]=0             #替换NaN为0
        zl1[i][isnan(zl1[i])]=0

    #.m132
    #第二锥飞行器参数化
    for i in range(0,n1):
        W2[i]=(Wmax                         #计算各截面宽度   ???
                /L**YangBen[i0][10]
                *l2[i]**YangBen[i0][10]
                )  
        Hu2[i]=tan(YangBen[i0][4])*(l2[i]-YangBen[i0][1])  #计算各截面上曲线的高度
        Hl2[i]=tan(YangBen[i0][5])*(l2[i]-YangBen[i0][1])  #计算各截面下曲线的高度
        y2[i]=linspace(-W2[i]/2,W2[i]/2,n0)
        x2[i]=l2[i]
        zu2[i]=(Hu2[i]
                *(+y2[i]/W2[i]+0.5*ones(n0))**(YangBen[i0][8])
                *(-y2[i]/W2[i]+0.5*ones(n0))**(YangBen[i0][8])
                *2.0**2.0*YangBen[i0][8]
                +zu1[n1-1]
                )

        zl2[i]=(Hl2[i]
                *(+y2[i]/W2[i]+0.5*ones(n0))**(YangBen[i0][9])
                *(-y2[i]/W2[i]+0.5*ones(n0))**(YangBen[i0][9])
                *2.0**2.0*YangBen[i0][8]
                +zl1[n1-1]
                )

        zu2[i][isnan(zu2[i])]=0             #替换NaN为0
        zl2[i][isnan(zl2[i])]=0'''


    #把第一锥和第二锥的数组粘合到一起   ？？？x1和x2为一维向量，x是二维？
    x =append(x1,x2)
    y =concatenate((y1,y2)  ,axis=0)    #y为二维矩阵，因此需要进行拼接，横向拼接
    zu=concatenate((zu1,zu2),axis=0)
    zl=concatenate((zl1,zl2),axis=0)
    # x=x1.extend(x2)   
    # y=y1.extend(y2)
    # zu=zu1.extend(zu2)
    # zl=zl1.extend(zl2)

    # UG格式输出
    # 记录上下表面的三维坐标
    B1=zeros((2* n1   *n0,3))           
    B2=zeros((2* n1   *n0,3))
    #print(B1)
    #print(len(y))
    for j1 in range(0,n0):
        for k1 in range(0,2*n1):
            B1[2* n1   *(j1)+k1][0]=x [k1]
            B1[2* n1   *(j1)+k1][1]=y [k1][j1]
            B1[2* n1   *(j1)+k1][2]=zu[k1][j1]
            B2[2* n1   *(j1)+k1][0]=x [k1]
            B2[2* n1   *(j1)+k1][1]=y [k1][j1]
            B2[2* n1   *(j1)+k1][2]=zl[k1][j1]
    
    #插值，生成底面
#     zc1=ones(2*n1,n0);
#     zc2=ones(2*n1,n0);
#     zc3=ones(2*n1,n0);
#     zc1=(zu+zl)/2;
#     zc2=(zu+zc1)/2;
#     zc3=(zl+zc1)/2;
#     B3=zeros(5*(n0-2),3);
#     for j1=1:n0
#         for k1=1:5
#             B3(5*(j1-1)+k1,1)=x(2*n1);
#             B3(5*(j1-1)+k1,2)=y(2*n1,j1);
#             if mod(k1,5)==1
#                B3(5*(j1-1)+k1,3)=zu(2*n1,j1);
#             elseif mod(k1,5)==2
#                B3(5*(j1-1)+k1,3)=zc2(2*n1,j1);
#             elseif mod(k1,5)==3
#                B3(5*(j1-1)+k1,3)=zc1(2*n1,j1);
#             elseif mod(k1,5)==4
#                B3(5*(j1-1)+k1,3)=zc3(2*n1,j1);
#             elseif mod(k1,5)==0
#                B3(5*(j1-1)+k1,3)=zl(2*n1,j1);
#             end
#         end
#     end
# 
#     ######????????????????######    
#     
#     #????????
#     second_folder=sprintf('#s#s',top_folder,int2str(i0));
#     mkdir(second_folder);
#   
#     #?????
#     UP=sprintf('#s#s',second_folder,'\up.dat');
#     fid = fopen(UP,'wt');
#     for m=1:n0
#         fprintf(fid,'#s\n','ROW');
#         fprintf(fid,'#f #f #f \n',B1(1+2* n1   * m   :m*2*n1,:)');
#     end   
#     fclose(fid);
#     #?��???   
#     DOWN=sprintf('#s#s',second_folder,'\down.dat');
#     fid = fopen(DOWN,'wt');
#     for m=1:n0
#         fprintf(fid,'#s\n','ROW');
#         fprintf(fid,'#f #f #f \n',B2(1+2* n1   * m   :m*2*n1,:)');
#     end
#     fclose(fid);
#      #????
#     under=sprintf('#s#s',second_folder,'\udersurface.dat');
#     fid=fopen(under,'wt')
#     for m=2:(n0-1)
#         fprintf(fid,'#s\n','ROW');
#         fprintf(fid,'#f #f #f \n',B3(5*m-4:5*m,:)');
#     end
#     fclose(fid);

    #求参考面积
    for k in range(0,n0-1):
        a_left [k]=zu[2*n1-1][k  ] - zl[2*n1-1][k  ] 
        b_right[k]=zu[2*n1-1][k+1] - zl[2*n1-1][k+1]
        h      [k]=y [2*n1-1][k+1] - y [2*n1-1][k  ]

        S_each[k]=(a_left[k]+b_right[k])*h[k]*0.5   #上低加下低乘高除以二
    S_can=sum(ravel(S_each))
    #print(S_can)
    # yucezhi=GCGS(n0,n1,B1,B2,V,p_lailiu,S_can,L_can,AttackAngle,Ma,midu)

#     qidongxishu(i0,1)=yucezhi(1);
#     qidongxishu(i0,2)=yucezhi(2);
#     qidongxishu(i0,3)=yucezhi(3);
#     qidongxishu(i0,4)=yucezhi(4);
#     qidongxishu(i0,5)=yucezhi(5);
#     qidongxishu(i0,6)=yucezhi(6);
    
    ############################################################???????????????????############################################################
    
    ############################################################???????############################################################


T1_up       =zeros(((2*n1-1)*(n0-1),3))     #T1这些值数量应该比n1*n0少一圈
T2_up       =zeros(((2*n1-1)*(n0-1),3))
T1_down     =zeros(((2*n1-1)*(n0-1),3))     #T1这些值数量应该比n1*n0少一圈
T2_down     =zeros(((2*n1-1)*(n0-1),3))
N_B1        =zeros(((2*n1-1)*(n0-1),3))
N_B1_fanshu =zeros( (2*n1-1)*(n0-1)   )
N_B1_danwei =zeros(((2*n1-1)*(n0-1),3))
N_B2        =zeros(((2*n1-1)*(n0-1),3))
N_B2_fanshu =zeros( (2*n1-1)*(n0-1)   )
N_B2_danwei =zeros(((2*n1-1)*(n0-1),3))
Average_B1  =zeros(((2*n1-1)*(n0-1),3))     #T1这些值数量应该比n1*n0少一圈
Average_B2  =zeros(((2*n1-1)*(n0-1),3))
B1_tou      =zeros(((2*n1-1)*(n0-1),3))
B2_tou      =zeros(((2*n1-1)*(n0-1),3))
B1_myx      =zeros(((2*n1  )*(n0  ),3))
B2_myx      =zeros(((2*n1  )*(n0  ),3))
A_up        =zeros( (2*n1-1)*(n0-1)   )
A_down      =zeros( (2*n1-1)*(n0-1)   )

T1_up_fanshu    =zeros( (2*n1-1)*(n0-1)   )
T1_up_danwei    =zeros(((2*n1-1)*(n0-1),3))
T1_down_fanshu  =zeros( (2*n1-1)*(n0-1)   )
T1_down_danwei  =zeros(((2*n1-1)*(n0-1),3))
m_danwei_up     =zeros(((2*n1-1)*(n0-1),3))
m_danwei_down   =zeros(((2*n1-1)*(n0-1),3))



ZhiXin_up       =zeros(((2*n1-1)*(n0-1),3))
Zhixin_up_fxqzbx=zeros(((2*n1-1)*(n0-1),3))

zhuangjijiao_up =zeros( (2*n1-1)*(n0-1)   )

F_up            =zeros(((2*n1-1)*(n0-1),3))
Cp_up           =zeros( (2*n1-1)*(n0-1)   )
CA_up           =zeros( (2*n1-1)*(n0-1)   )
CN_up           =zeros( (2*n1-1)*(n0-1)   )
CZ_up           =zeros( (2*n1-1)*(n0-1)   )
Cl_up           =zeros( (2*n1-1)*(n0-1)   )
Cd_up           =zeros( (2*n1-1)*(n0-1)   )

ZhiXin_down       =zeros(((2*n1-1)*(n0-1),3))
Zhixin_down_fxqzbx=zeros(((2*n1-1)*(n0-1),3))

zhuangjijiao_down =zeros( (2*n1-1)*(n0-1)   )

F_down            =zeros(((2*n1-1)*(n0-1),3))
Cp_down           =zeros( (2*n1-1)*(n0-1)   )
CA_down           =zeros( (2*n1-1)*(n0-1)   )
CN_down           =zeros( (2*n1-1)*(n0-1)   )
CZ_down           =zeros( (2*n1-1)*(n0-1)   )
Cl_down           =zeros( (2*n1-1)*(n0-1)   )
Cd_down           =zeros( (2*n1-1)*(n0-1)   )

#@function
def GCGS(   n0=None,
            n1=None,
            B1=None,
            B2=None,
            V=None,
            p_lailiu=None,
            S_can=None,
            L_can=None,
            AttackAngle=None,
            Ma=None,
            midu=None,
            *args,
            **kwargs):
    #varargin = GCGS.varargin
    #nargin = GCGS.nargin

    ###########?????###########
    
    ###############################################################?????###############################################################
    for m in range(0,n0-1):
        ####################一锥########## ##########
        for p in range(0,n1-1):                     #m横坐标向右，p横坐标向上为例
            T1_up   [2*(n1-1)* m   +p  ]=(
                + B1[2*(n1-1)*(m+1)+p+1]            #右上
                - B1[2*(n1-1)* m   +p  ]            #左下
                )
            T2_up   [2*(n1-1)* m   +p  ]=(
                + B1[2*(n1-1)* m   +p+1]            #左上
                - B1[2*(n1-1)*(m+1)+p  ]            #右下
                )
            
            N_B1     [2*(n1-1)* m   +p  ]=(cross(  
                T2_up[2*(n1-1)* m   +p  ],
                T1_up[2*(n1-1)* m   +p  ]
                ))

            N_B1_fanshu[2*(n1-1)* m   +p  ]=linalg.linalg.norm(N_B1[2*(n1-1)* m   +p  ])
            N_B1_danwei[2*(n1-1)* m   +p  ]=(           N_B1[2*(n1-1)* m   +p  ]
                                                /N_B1_fanshu[2*(n1-1)* m   +p  ]
                                            )
            
            Average_B1 [2*(n1-1)* m   +p  ]=(0.25*(
                    B1 [2*(n1-1)* m   +p  ] 
                +   B1 [2*(n1-1)* m   +p+1] 
                +   B1 [2*(n1-1)*(m+1)+p  ] 
                +   B1 [2*(n1-1)*(m+1)+p+1]
                ))

            #起始右上左
            #将四个角点投影到面元平面上     问题，公式中dk应该是一个数，此处dk对应什么？ 与参考文献不同注意修改
            B1_tou[2* n1   * m   +p  ]=B1[2* n1   * m   +p  ] + N_B1_danwei[2*(n1-1)* m   +p  ]*(Average_B1[2*(n1-1)* m   +p  ] - B1[2* n1   * m   +p  ])
            B1_tou[2* n1   *(m+1)+p  ]=B1[2* n1   *(m+1)+p  ] + N_B1_danwei[2*(n1-1)* m   +p  ]*(Average_B1[2*(n1-1)* m   +p  ] - B1[2* n1   *(m+1)+p  ])
            B1_tou[2* n1   *(m+1)+p+1]=B1[2* n1   *(m+1)+p+1] + N_B1_danwei[2*(n1-1)* m   +p  ]*(Average_B1[2*(n1-1)* m   +p  ] - B1[2* n1   *(m+1)+p+1])
            B1_tou[2* n1   * m   +p+1]=B1[2* n1   * m   +p+1] + N_B1_danwei[2*(n1-1)* m   +p  ]*(Average_B1[2*(n1-1)* m   +p  ] - B1[2* n1   * m   +p+1])

            #建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1,y轴平行于m，z轴平行于n
            T1_up_fanshu[2*(n1-1)* m   +p  ]=linalg.linalg.norm(T1_up[2*(n1-1)* m   +p  ])
            T1_up_danwei[2*(n1-1)* m   +p  ]=           (T1_up[2*(n1-1)* m   +p  ]
                                                 /T1_up_fanshu[2*(n1-1)* m   +p  ])
            m_danwei_up [2*(n1-1)* m   +p  ]=cross(N_B1_danwei[2*(n1-1)* m   +p  ],
                                                  T1_up_danwei[2*(n1-1)* m   +p  ])

            #把投影点从飞行器坐标系转换到面元坐标系
            #x
            B1_myx[2* n1   * m   +p  ][0]=(T1_up_danwei[2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   *(m+1)+p  ][0]=(T1_up_danwei[2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   *(m+1)+p  ][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   *(m+1)+p  ][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   *(m+1)+p  ][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   *(m+1)+p+1][0]=(T1_up_danwei[2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   *(m+1)+p+1][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   *(m+1)+p+1][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   *(m+1)+p+1][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   * m   +p+1][0]=(T1_up_danwei[2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   * m   +p+1][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   * m   +p+1][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   * m   +p+1][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            #y
            B1_myx[2* n1   * m   +p  ][1]=(m_danwei_up [2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   *(m+1)+p  ][1]=(m_danwei_up [2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   *(m+1)+p  ][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   *(m+1)+p  ][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   *(m+1)+p  ][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   *(m+1)+p+1][1]=(m_danwei_up [2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   *(m+1)+p+1][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   *(m+1)+p+1][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   *(m+1)+p+1][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            B1_myx[2* n1   * m   +p+1][1]=(m_danwei_up [2*(n1-1)* m   +p  ][0]*(B1_tou[2* n1   * m   +p+1][0] - Average_B1[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][1]*(B1_tou[2* n1   * m   +p+1][1] - Average_B1[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_up [2*(n1-1)* m   +p  ][2]*(B1_tou[2* n1   * m   +p+1][2] - Average_B1[2*(n1-1)* m   +p  ][2])
                                        )
            #z
            B1_myx[2* n1   * m   +p  ][2]=0
            B1_myx[2* n1   *(m+1)+p  ][2]=0
            B1_myx[2* n1   *(m+1)+p+1][2]=0
            B1_myx[2* n1   * m   +p+1][2]=0

            
            #求面元的面积△A         问题，两个横坐标之差乘积除以二？
            A_up[2*(n1-1)* m   +p  ]=(0.5*(B1_myx[2* n1   *(m+1)+p+1][0] - B1_myx[2* n1   * m   +p  ][0])
                                         *(B1_myx[2* n1   *(m+1)+p  ][0] - B1_myx[2* n1   * m   +p+1][0])
                                        )
            #求面元质心的坐标        问题，1/3/(右下y-左上y)*  (  左上x*(左下y-右下y) +  右下x*(左上y-左下y)  )
            ZhiXin_up[2*(n1-1)* m   +p  ][0]=(1/3/(B1_myx[2* n1   *(m+1)+p  ][1] - B1_myx[2* n1   * m   +p+1][1])
                                                *(
                                                +  B1_myx[2* n1   * m   +p+1][0]
                                                 *(B1_myx[2* n1   * m   +p  ][1] - B1_myx[2* n1   *(m+1)+p  ][1])
                                                +  B1_myx[2* n1   *(m+1)+p  ][0]
                                                 *(B1_myx[2* n1   * m   +p+1][1] - B1_myx[2* n1   * m   +p  ][1])
                                                )
                                                )
            ZhiXin_up[2*(n1-1)* m   +p  ][1]=(-1/3)*B1_myx[2* n1   * m   +p  ][1]
            ZhiXin_up[2*(n1-1)* m   +p  ][2]=0

            #质心在飞行器坐标系中的质心坐标  面元坐标系转飞行器坐标系
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p  ][0]=(   Average_B1[2*(n1-1)* m   +p  ][0] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p  ][0]*ZhiXin_up[2*(n1-1)* m   +p  ][0]
                                                    + m_danwei_up [2*(n1-1)* m   +p  ][0]*ZhiXin_up[2*(n1-1)* m   +p  ][1]
                                                    )
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p  ][1]=(   Average_B1[2*(n1-1)* m   +p  ][1] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p  ][1]*ZhiXin_up[2*(n1-1)* m   +p  ][0]
                                                    + m_danwei_up [2*(n1-1)* m   +p  ][1]*ZhiXin_up[2*(n1-1)* m   +p  ][1]
                                                    )
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p  ][2]=(   Average_B1[2*(n1-1)* m   +p  ][2] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p  ][2]*ZhiXin_up[2*(n1-1)* m   +p  ][0]
                                                    + m_danwei_up [2*(n1-1)* m   +p  ][2]*ZhiXin_up[2*(n1-1)* m   +p  ][1]
                                                    )
            #撞击角
            zhuangjijiao_up [2*(n1-1)* m   +p  ]=pi/2-arccos(-(dot(N_B1_danwei[2*(n1-1)* m   +p  ],V[0])))/ linalg.linalg.norm(V[0])
            Cp_up[2*(n1-1)* m   +p  ]=Newton1(zhuangjijiao_up[2*(n1-1)* m   +p  ],V[0][0],V[0][1],V[0][2],Ma)
            #求作用力

            F_up [2*(n1-1)* m   +p  ]=( A_up [2*(n1-1)* m   +p  ]*
                                      ( Cp_up[2*(n1-1)* m   +p  ]
                                            *0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)    #1/2*rho*V**2   dynamic Pressure
                                            +p_lailiu)
                                        )
            CA_up[2*(n1-1)* m   +p  ]=F_up [2*(n1-1)* m   +p  ][0]*N_B1_danwei[2*(n1-1)* m   +p  ][0] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CN_up[2*(n1-1)* m   +p  ]=F_up [2*(n1-1)* m   +p  ][2]*N_B1_danwei[2*(n1-1)* m   +p  ][2] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CZ_up[2*(n1-1)* m   +p  ]=F_up [2*(n1-1)* m   +p  ][1]*N_B1_danwei[2*(n1-1)* m   +p  ][1] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)

            Cl_up[2*(n1-1)* m   +p  ]=CN_up[2*(n1-1)* m   +p  ]*cos(AttackAngle) - CA_up[2*(n1-1)* m   +p  ]*sin(AttackAngle)
            Cd_up[2*(n1-1)* m   +p  ]=CN_up[2*(n1-1)* m   +p  ]*sin(AttackAngle) + CA_up[2*(n1-1)* m   +p  ]*cos(AttackAngle)
        ####################一锥结束####################

        # test.m:334
        ####################二锥####################
        for p in range(n1-1,2*n1-1):
            T1_up   [2*(n1-1)* m   +p-1]=(
                + B1[2*(n1-1)* m   +p+1]
                - B1[2*(n1-1)* m   +p  ]
                )
            T2_up   [2*(n1-1)* m   +p-1]=(
                + B1[2*(n1-1)* m   +p+1]
                - B1[2*(n1-1)* m   +p  ]
                )
            N_B1    [2*(n1-1)* m   +p-1]=(cross(
               T2_up[2*(n1-1)* m   +p-1],
               T1_up[2*(n1-1)* m   +p-1]
                ))


            N_B1_fanshu[2*(n1-1)* m   +p-1]=linalg.linalg.norm(N_B1[2*(n1-1)* m   +p-1])
            N_B1_danwei[2*(n1-1)* m   +p-1]=(           N_B1[2*(n1-1)* m   +p-1] 
                                                /N_B1_fanshu[2*(n1-1)* m   +p-1]
                                            )
    
            Average_B1 [2*(n1-1)* m   +p-1]=(0.25*(
                +   B1 [2*(n1-1)* m   +p  ]
                +   B1 [2*(n1-1)* m   +p  ]
                +   B1 [2*(n1-1)* m   +p+1]
                +   B1 [2*(n1-1)* m   +p+1]
                ))

            #将四个角点投影到面元平面上     问题，为什么是p-1
            B1_tou[2* n1   * m   +p  ]=B1[2* n1   * m   +p  ] + N_B1_danwei[2*(n1-1)* m   +p-1]*(Average_B1[2*(n1-1)* m   +p-1] - B1[2*(n1-1)* m   +p  ])
            B1_tou[2* n1   *(m+1)+p  ]=B1[2* n1   *(m+1)+p  ] + N_B1_danwei[2*(n1-1)* m   +p-1]*(Average_B1[2*(n1-1)* m   +p-1] - B1[2*(n1-1)*(m+1)+p  ])
            B1_tou[2* n1   *(m+1)+p+1]=B1[2* n1   *(m+1)+p+1] + N_B1_danwei[2*(n1-1)* m   +p-1]*(Average_B1[2*(n1-1)* m   +p-1] - B1[2*(n1-1)*(m+1)+p+1])
            B1_tou[2* n1   * m   +p+1]=B1[2* n1   * m   +p+1] + N_B1_danwei[2*(n1-1)* m   +p-1]*(Average_B1[2*(n1-1)* m   +p-1] - B1[2*(n1-1)* m   +p+1])
            
            #建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1_up,y轴平行于m，z轴平行于n
            T1_up_fanshu[2*(n1-1)* m   +p-1]=linalg.linalg.norm(T1_up[2*(n1-1)* m   +p-1])
            T1_up_danwei[2*(n1-1)* m   +p-1]=           (T1_up[2*(n1-1)* m   +p-1] 
                                                 /T1_up_fanshu[2*(n1-1)* m   +p-1])
            m_danwei_up [2*(n1-1)* m   +p-1]=cross(N_B1_danwei[2*(n1-1)* m   +p-1],
                                                  T1_up_danwei[2*(n1-1)* m   +p-1])
            #??????????????????????????????
            #x
            B1_myx[2* n1   * m   +p  ][0]=(T1_up_danwei[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   *(m+1)+p  ][1]=(T1_up_danwei[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   *(m+1)+p+1][0]=(T1_up_danwei[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   *(m+1)+p+1][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   *(m+1)+p+1][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   *(m+1)+p+1][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   * m   +p+1][0]=(T1_up_danwei[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p+1][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p+1][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         + T1_up_danwei[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p+1][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )

            #y
            B1_myx[2* n1   * m   +p  ][1]=( m_danwei_up[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   *(m+1)+p  ][1]=( m_danwei_up[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p  ][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p  ][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p  ][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   *(m+1)+p+1][1]=( m_danwei_up[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   *(m+1)+p+1][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   *(m+1)+p+1][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   *(m+1)+p+1][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            B1_myx[2* n1   * m   +p+1][1]=( m_danwei_up[2*(n1-1)* m   +p-1][0]*(B1_tou[2* n1   * m   +p+1][0] - Average_B1[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][1]*(B1_tou[2* n1   * m   +p+1][1] - Average_B1[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_up[2*(n1-1)* m   +p-1][2]*(B1_tou[2* n1   * m   +p+1][2] - Average_B1[2*(n1-1)* m   +p-1][2])
                                        )
            #z
            B1_myx[2* n1   * m   +p  ][2]=0
            B1_myx[2* n1   *(m+1)+p  ][2]=0
            B1_myx[2* n1   *(m+1)+p+1][2]=0
            B1_myx[2* n1   * m   +p+1][2]=0

            
            #求面元的面积△A
            A_up[2*(n1-1)* m   +p-1]=(0.5*(B1_myx[2* n1   *(m+1)+p+1][0] - B1_myx[2* n1   * m   +p  ][0])
                                         *(B1_myx[2* n1   *(m+1)+p  ][0] - B1_myx[2* n1   * m   +p+1][0])
                                        )
            
            #求面元质心的坐标
            ZhiXin_up[2*(n1-1)* m   +p-1][0]=(1/3/(B1_myx[2* n1   *(m+1)+p  ][1] - B1_myx[2* n1   * m   +p+1][1])
                                                *(
                                                +  B1_myx[2* n1   * m   +p+1][0]
                                                * (B1_myx[2* n1   * m   +p  ][1] - B1_myx[2* n1   *(m+1)+p  ][1])
                                                +  B1_myx[2* n1   *(m+1)+p  ][0]
                                                * (B1_myx[2* n1   * m   +p+1][1] - B1_myx[2* n1   * m   +p  ][1])
                                                )
                                                )
            ZhiXin_up[2*(n1-1)* m   +p-1][1]=(-1/3)*B1_myx[2* n1   * m   +p+1][1]
            ZhiXin_up[2*(n1-1)* m   +p-1][1]=0      #问题，bug
            #质心在飞行器坐标系中的质心坐标
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p-1][0]=(   Average_B1[2*(n1-1)* m   +p-1][0] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p-1][0]*ZhiXin_up[2*(n1-1)* m   +p-1][0] 
                                                    +  m_danwei_up[2*(n1-1)* m   +p-1][0]*ZhiXin_up[2*(n1-1)* m   +p-1][1]
                                                    )
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p-1][1]=(   Average_B1[2*(n1-1)* m   +p-1][1] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p-1][1]*ZhiXin_up[2*(n1-1)* m   +p-1][0]
                                                    +  m_danwei_up[2*(n1-1)* m   +p-1][1]*ZhiXin_up[2*(n1-1)* m   +p-1][1]
                                                    )
            Zhixin_up_fxqzbx[2*(n1-1)* m   +p-1][2]=(   Average_B1[2*(n1-1)* m   +p-1][2] 
                                                    + T1_up_danwei[2*(n1-1)* m   +p-1][2]*ZhiXin_up[2*(n1-1)* m   +p-1][0]
                                                    +  m_danwei_up[2*(n1-1)* m   +p-1][2]*ZhiXin_up[2*(n1-1)* m   +p-1][1]
                                                    )#问题，bug为什么都是010101
            #撞击角
            zhuangjijiao_up [2*(n1-1)* m   +p-1]=pi/2-arccos(-(dot(N_B1_danwei[2*(n1-1)* m   +p-1],V[0])))/ linalg.linalg.norm(V[0])
            Cp_up[2*(n1-1)* m   +p-1]=Newton1(zhuangjijiao_up[2*(n1-1)* m   +p-1],V[0][0],V[0][1],V[0][2],Ma)
            
            #????????
            F_up [2*(n1-1)* m   +p-1]=( A_up [2*(n1-1)* m   +p-1]*
                                      ( Cp_up[2*(n1-1)* m   +p-1]
                                            *0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)    #1/2*rho*V**2   dynamic Pressure
                                            +p_lailiu)
                                        )

            CA_up[2*(n1-1)* m   +p-1]=F_up [2*(n1-1)* m   +p-1]*N_B1_danwei[2*(n1-1)* m   +p-1][0] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CN_up[2*(n1-1)* m   +p-1]=F_up [2*(n1-1)* m   +p-1]*N_B1_danwei[2*(n1-1)* m   +p-1][2] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CZ_up[2*(n1-1)* m   +p-1]=F_up [2*(n1-1)* m   +p-1]*N_B1_danwei[2*(n1-1)* m   +p-1][1] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)

            Cl_up[2*(n1-1)* m   +p-1]=CN_up[2*(n1-1)* m   +p-1]*cos(AttackAngle) - CA_up[2*(n1-1)* m   +p-1]*sin(AttackAngle)
            Cd_up[2*(n1-1)* m   +p-1]=CN_up[2*(n1-1)* m   +p-1]*sin(AttackAngle) + CA_up[2*(n1-1)* m   +p-1]*cos(AttackAngle)
        ####################二锥结束####################
    
    ###############################################################上表面结束###############################################################
   
   
    ###############################################################下表面###############################################################
    for m in range(0,n0 - 1):
        ####################一锥########## ##########
        for p in range(0,n1 - 1):
            T1_down [2*(n1-1)* m   +p  ]=(
                + B2[2*(n1-1)*(m+1)+p+1]
                - B2[2*(n1-1)* m   +p  ]
                )
            T2_down [2*(n1-1)* m   +p  ]=(
                + B2[2*(n1-1)* m   +p+1]
                - B2[2*(n1-1)*(m+1)+p  ])

            N_B2    [2*(n1-1)* m   +p  ]=cross(
             T2_down[2*(n1-1)* m   +p  ],
             T1_down[2*(n1-1)* m   +p  ])

            N_B2_fanshu[2*(n1-1)* m   +p  ]=linalg.linalg.norm(N_B2[2*(n1-1)* m   +p  ])
            N_B2_danwei[2*(n1-1)* m   +p  ]=(         - N_B2[2*(n1-1)* m   +p  ] #问题，为何有负号
                                                /N_B2_fanshu[2*(n1-1)* m   +p  ]
                                            )
            Average_B2[2*(n1-1)* m   +p  ]=(0.25*(
                  + B2[2*(n1-1)* m   +p  ]
                  + B2[2*(n1-1)*(m+1)+p  ]
                  + B2[2*(n1-1)*(m+1)+p+1]
                  + B2[2*(n1-1)* m   +p+1]
                  ))


            #将四个角点投影到面元平面上
            B2_tou[2* n1   * m   +p  ]=B2[2*(n1-1)* m   +p  ] + N_B2_danwei[2*(n1-1)* m   +p  ]*(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)* m   +p  ])
            B2_tou[2* n1   *(m+1)+p  ]=B2[2*(n1-1)*(m+1)+p  ] + N_B2_danwei[2*(n1-1)* m   +p  ]*(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)*(m+1)+p  ])
            B2_tou[2* n1   *(m+1)+p+1]=B2[2*(n1-1)*(m+1)+p+1] + N_B2_danwei[2*(n1-1)* m   +p  ]*(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)*(m+1)+p+1])
            B2_tou[2* n1   * m   +p+1]=B2[2*(n1-1)* m   +p+1] + N_B2_danwei[2*(n1-1)* m   +p  ]*(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)* m   +p+1])
            
            
            #建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1,y轴平行于m，z轴平行于n
            T1_down_fanshu[2*(n1-1)* m   +p  ]=linalg.linalg.norm(T1_down[2*(n1-1)* m   +p  ])
            T1_down_danwei[2*(n1-1)* m   +p  ]=(           T1_down[2*(n1-1)* m   +p  ] 
                                                   /T1_down_fanshu[2*(n1-1)* m   +p  ])
            m_danwei_down [2*(n1-1)* m   +p  ]=cross(  N_B2_danwei[2*(n1-1)* m   +p  ],
                                                    T1_down_danwei[2*(n1-1)* m   +p  ])
            #把投影点从飞行器坐标系转换到面元坐标系
            #x
            B2_myx[2* n1   * m   +p  ][0]=(T1_down_danwei[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   * m   +p  ][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   *(m+1)+p  ][0]=(T1_down_danwei[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   *(m+1)+p  ][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   *(m+1)+p  ][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   *(m+1)+p  ][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   *(m+1)+p+1][0]=(T1_down_danwei[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   *(m+1)+p+1][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   *(m+1)+p+1][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   *(m+1)+p+1][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   * m   +p+1][0]=(T1_down_danwei[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   * m   +p+1][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   * m   +p+1][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + T1_down_danwei[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   * m   +p+1][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            #y
            B2_myx[2* n1   * m   +p  ][1]=(m_danwei_down[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   * m   +p+1][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   *(m+1)+p  ][1]=(m_danwei_down[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   *(m+1)+p  ][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   *(m+1)+p  ][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   *(m+1)+p  ][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   *(m+1)+p+1][1]=(m_danwei_down[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   *(m+1)+p+1][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   *(m+1)+p+1][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   *(m+1)+p+1][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            B2_myx[2* n1   * m   +p+1][1]=(m_danwei_down[2*(n1-1)* m   +p  ][0]*(B2_tou[2* n1   * m   +p+1][0] - Average_B2[2*(n1-1)* m   +p  ][0])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][1],(B2_tou[2* n1   * m   +p+1][1] - Average_B2[2*(n1-1)* m   +p  ][1])
                                         + m_danwei_down[2*(n1-1)* m   +p  ][2],(B2_tou[2* n1   * m   +p+1][2] - Average_B2[2*(n1-1)* m   +p  ][2])
                                        )
            #z
            B2_myx[2* n1   * m   +p  ][2]=0
            B2_myx[2* n1   *(m+1)+p  ][2]=0
            B2_myx[2* n1   *(m+1)+p+1][2]=0
            B2_myx[2* n1   * m   +p+1][2]=0
            
            #求面元的面积△A
            A_down[2*(n1-1)* m   +p  ]=(0.5 *(B2_myx[2* n1   *(m+1)+p+1][0] - B2_myx[2* n1   * m   +p  ][0])
                                            *(B2_myx[2* n1   *(m+1)+p  ][0] - B2_myx[2* n1   * m   +p+1][0])
                                            )
            #求面元质心的坐标
            ZhiXin_down[2*(n1-1)* m   +p  ][0]=(1/3/( B2_myx[2* n1   *(m+1)+p  ][1] - B2_myx[2* n1   * m   +p+1][1])
                                                    *(
                                                    + B2_myx[2* n1   * m   +p+1][0]
                                                    *(B2_myx[2* n1   * m   +p  ][1] - B2_myx[2* n1   *(m+1)+p  ][1])
                                                    + B2_myx[2* n1   *(m+1)+p  ][0]
                                                    *(B2_myx[2* n1   * m   +p+1][1] - B2_myx[2* n1   * m   +p  ][1])
                                                )
                                                )
            ZhiXin_down[2*(n1-1)* m   +p  ][1]=(-1/3)*B2_myx[2* n1   * m   +p  ][1]
            ZhiXin_down[2*(n1-1)* m   +p  ][2]=0

            #质心在飞行器坐标系中的质心坐标
            Zhixin_down_fxqzbx[2*(n1-1)* m   +p  ][0]=(Average_B2[2*(n1-1)* m   +p  ][0]
                                                +  T1_down_danwei[2*(n1-1)* m   +p  ][0]*ZhiXin_down[2*(n1-1)* m   +p  ][0]
                                                +   m_danwei_down[2*(n1-1)* m   +p  ][0]*ZhiXin_down[2*(n1-1)* m   +p  ][1]
                                                )
            Zhixin_down_fxqzbx[2*(n1-1)* m   +p  ][1]=(Average_B2[2*(n1-1)* m   +p  ][1]
                                                +  T1_down_danwei[2*(n1-1)* m   +p  ][1]*ZhiXin_down[2*(n1-1)* m   +p  ][0]
                                                +   m_danwei_down[2*(n1-1)* m   +p  ][1]*ZhiXin_down[2*(n1-1)* m   +p  ][1]
                                                )
            Zhixin_down_fxqzbx[2*(n1-1)* m   +p  ][2]=(Average_B2[2*(n1-1)* m   +p  ][2]
                                                +  T1_down_danwei[2*(n1-1)* m   +p  ][2]*ZhiXin_down[2*(n1-1)* m   +p  ][0]
                                                +   m_danwei_down[2*(n1-1)* m   +p  ][2]*ZhiXin_down[2*(n1-1)* m   +p  ][1]
                                                )

            zhuangjijiao_down [2*(n1-1)* m   +p  ]=pi/2-arccos(-(dot(N_B2_danwei[2*(n1-1)* m   +p  ],V[0])))/ linalg.linalg.norm(V[0])
            if zhuangjijiao_down[2*(n1-1)* m   +p  ] >= 0:
                Cp_down[2*(n1-1)* m   +p  ]=Newton1(zhuangjijiao_down[2*(n1-1)* m   +p  ][0],V[0][0],V[0][1],V[0][2],Ma)
            if zhuangjijiao_down[2*(n1-1)* m   +p  ] < 0:
                Cp_down[2*(n1-1)* m   +p  ]=Qie2   (zhuangjijiao_down[2*(n1-1)* m   +p  ][0],V[0][0],V[0][1],V[0][2],Ma)
            #求作用力
            F_down [2*(n1-1)* m   +p  ]=( A_down[2*(n1-1)* m   +p  ]*
                                        (Cp_down[2*(n1-1)* m   +p  ]
                                            *0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)
                                            +p_lailiu)
                                        )
            CA_down[2*(n1-1)* m   +p  ]=F_down[2*(n1-1)* m   +p  ][0]*N_B1_danwei[2*(n1-1)* m   +p  ][0] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CN_down[2*(n1-1)* m   +p  ]=F_down[2*(n1-1)* m   +p  ][2]*N_B1_danwei[2*(n1-1)* m   +p  ][2] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CZ_down[2*(n1-1)* m   +p  ]=F_down[2*(n1-1)* m   +p  ][1]*N_B1_danwei[2*(n1-1)* m   +p  ][1] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)

            Cl_down[2*(n1-1)* m   +p  ]=CN_down[2*(n1-1)* m   +p  ]*cos(AttackAngle) - (CA_down[2*(n1-1)* m   +p  ],sin(AttackAngle))
            Cd_down[2*(n1-1)* m   +p  ]=CN_down[2*(n1-1)* m   +p  ]*sin(AttackAngle) + (CA_down[2*(n1-1)* m   +p  ],cos(AttackAngle))
        # test.m:482
        ####################一锥结束####################
        ####################二锥####################
        for p in range((n1 + 1),(dot(2,n1) - 1)).reshape(-1):
            T1_down  [2*(n1-1)* m   +p-1]=(
                +  B2[2*(n1-1)*(m+1)+p+1]
                -  B2[2*(n1-1)* m   +p  ]
                )
            T2_down  [2*(n1-1)* m   +p-1]=(
                +  B2[2*(n1-1)* m   +p+1]
                -  B2[2*(n1-1)*(m+1)+p  ]
                )
            N_B2     [2*(n1-1)* m   +p-1]=cross(
              T2_down[2*(n1-1)* m   +p-1],
              T1_down[2*(n1-1)* m   +p-1]
              )

            N_B2_fanshu[2*(n1-1)* m   +p-1]=linalg.linalg.norm(N_B2[2*(n1-1)* m   +p-1])
            N_B2_danwei[2*(n1-1)* m   +p-1]=-(          N_B2[2*(n1-1)* m   +p-1]
                                                /N_B2_fanshu[2*(n1-1)* m   +p-1]
                                             )
            Average_B2[2*(n1-1)* m   +p-1]=(0.25*(
                + B2[2*(n1-1)* m   +p  ]
                + B2[2*(n1-1)*(m+1)+p  ]
                + B2[2*(n1-1)*(m+1)+p+1]
                + B2[2*(n1-1)* m   +p+1]
                ))
            
            #将四个角点投影到面元平面上
            B2_tou[2* n1   * m   +p  ]=B2[2*(n1-1)* m   +p  ] + N_B2_danwei[2*(n1-1)* m   +p-1]*(Average_B2[2*(n1-1)* m   +p-1] - B2[2*(n1-1)* m   +p  ])
            B2_tou[2* n1   *(m+1)+p  ]=B2[2*(n1-1)*(m+1)+p  ] + N_B2_danwei[2*(n1-1)* m   +p-1]*(Average_B2[2*(n1-1)* m   +p-1] - B2[2*(n1-1)*(m+1)+p  ])
            B2_tou[2* n1   *(m+1)+p+1]=B2[2*(n1-1)*(m+1)+p+1] + N_B2_danwei[2*(n1-1)* m   +p-1]*(Average_B2[2*(n1-1)* m   +p-1] - B2[2*(n1-1)*(m+1)+p+1])
            B2_tou[2* n1   * m   +p+1]=B2[2*(n1-1)* m   +p+1] + N_B2_danwei[2*(n1-1)* m   +p-1]*(Average_B2[2*(n1-1)* m   +p-1] - B2[2*(n1-1)* m   +p+1])
            
            #建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1_down,y轴平行于m，z轴平行于n
            T1_down_fanshu[2*(n1-1)* m   +p-1]=linalg.norm(T1_down[2*(n1-1)* m   +p-1])
            T1_down_danwei[2*(n1-1)* m   +p-1]=           (T1_down[2*(n1-1)* m   +p-1] 
                                                   /T1_down_fanshu[2*(n1-1)* m   +p-1])
            m_danwei_down [2*(n1-1)* m   +p-1]=cross(  N_B2_danwei[2*(n1-1)* m   +p-1],
                                                    T1_down_danwei[2*(n1-1)* m   +p-1])

            #把投影点从飞行器坐标系转换到面元坐标系
            #x
            #问题 此处有bug
            B2_myx[2* n1   * m   +p  ][0]=(T1_down_danwei[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p  ][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                            )
            B2_myx[2* n1   *(m+1)+p  ][0]=(T1_down_danwei[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p  ][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            B2_myx[2* n1   *(m+1)+p+1][0]=(T1_down_danwei[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   *(m+1)+p+1][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   *(m+1)+p+1][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   *(m+1)+p+1][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            B2_myx[2* n1   * m   +p+1][0]=(T1_down_danwei[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p+1][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p+1][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                        +  T1_down_danwei[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p+1][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            #y
            B2_myx[2* n1   * m   +p  ][1]=( m_danwei_down[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p  ][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            B2_myx[2* n1   *(m+1)+p  ][1]=( m_danwei_down[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p  ][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p  ][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p  ][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            B2_myx[2* n1   *(m+1)+p+1][1]=( m_danwei_down[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   *(m+1)+p+1][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   *(m+1)+p+1][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   *(m+1)+p+1][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            B2_myx[2* n1   * m   +p+1][1]=( m_danwei_down[2*(n1-1)* m   +p-1][0]*(B2_tou[2* n1   * m   +p+1][0] - Average_B2[2*(n1-1)* m   +p-1][0])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][1]*(B2_tou[2* n1   * m   +p+1][1] - Average_B2[2*(n1-1)* m   +p-1][1])
                                         +  m_danwei_down[2*(n1-1)* m   +p-1][2]*(B2_tou[2* n1   * m   +p+1][2] - Average_B2[2*(n1-1)* m   +p-1][2])
                                        )
            #z
            B2_myx[2* n1   * m   +p  ][2]=0
            B2_myx[2* n1   *(m+1)+p  ][2]=0
            B2_myx[2* n1   *(m+1)+p+1][2]=0
            B2_myx[2* n1   * m   +p+1][2]=0

            #求面元的面积△A
            A_down[2*(n1-1)* m   +p-1]=(0.5*(B2_myx[2* n1   *(m+1)+p+1] - B2_myx[2* n1   * m   +p  ])
                                           *(B2_myx[2* n1   *(m+1)+p  ] - B2_myx[2* n1   * m   +p+1])
                                           )

            ZhiXin_down[2*(n1-1)* m   +p-1][0]=(1/3/(B2_myx[2* n1   *(m+1)+p  ][1] - B2_myx[2* n1   * m   +p+1][1])
                                                *(
                                                +    B2_myx[2* n1   * m   +p+1][0]
                                                   *(B2_myx[2* n1   * m   +p  ][1] - B2_myx[2* n1   *(m+1)+p  ][1])
                                                +    B2_myx[2* n1   *(m+1)+p  ][0]
                                                   *(B2_myx[2* n1   * m   +p+1][1] - B2_myx[2* n1   * m   +p  ][1])
                                                )
                                                )
            ZhiXin_down[2*(n1-1)* m   +p-1][1]=multiply(- (1 / 3),B2_myx[2* n1   * m   +p+1][1])
            ZhiXin_down[2*(n1-1)* m   +p-1][1]=0        #问题 bug

            Zhixin_down_fxqzbx[2*(n1-1)* m   +p-1][0]=(    Average_B2[2*(n1-1)* m   +p-1][0]
                                                      +T1_down_danwei[2*(n1-1)* m   +p-1][0]*ZhiXin_down[2*(n1-1)* m   +p-1][0]
                                                      + m_danwei_down[2*(n1-1)* m   +p-1][0]*ZhiXin_down[2*(n1-1)* m   +p-1][1]
                                                      )
            Zhixin_down_fxqzbx[2*(n1-1)* m   +p-1][1]=(    Average_B2[2*(n1-1)* m   +p-1][1]
                                                      +T1_down_danwei[2*(n1-1)* m   +p-1][1]*ZhiXin_down[2*(n1-1)* m   +p-1][0]
                                                      + m_danwei_down[2*(n1-1)* m   +p-1][1]*ZhiXin_down[2*(n1-1)* m   +p-1][1]
                                                      )
            Zhixin_down_fxqzbx[2*(n1-1)* m   +p-1][2]=(    Average_B2[2*(n1-1)* m   +p-1][2]
                                                      +T1_down_danwei[2*(n1-1)* m   +p-1][2]*ZhiXin_down[2*(n1-1)* m   +p-1][0]
                                                      + m_danwei_down[2*(n1-1)* m   +p-1][2]*ZhiXin_down[2*(n1-1)* m   +p-1][1]
                                                      )
            zhuangjijiao_down [2*(n1-1)* m   +p-1]=pi/2-arccos(-(dot(N_B2_danwei[2*(n1-1)* m   +p-1],V[0]))/ linalg.norm(V[0]))
            if zhuangjijiao_down[2*(n1-1)* m   +p-1] >= 0:
                Cp_down[2*(n1-1)* m   +p-1]=Newton1(zhuangjijiao_down[2*(n1-1)* m   +p-1],V[0][0],V[0][1],V[0][2],Ma)
            if zhuangjijiao_down[2*(n1-1)* m   +p-1] < 0:
                Cp_down[2*(n1-1)* m   +p-1]=Newton1(zhuangjijiao_down[2*(n1-1)* m   +p-1],V[0][0],V[0][1],V[0][2],Ma)
            #求作用力
            F_down [2*(n1-1)* m   +p-1]=(  A_down [2*(n1-1)* m   +p-1]*
                                        (  Cp_down[2*(n1-1)* m   +p-1]
                                                *0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2))
                                                +p_lailiu
                                        )

            CA_down[2*(n1-1)* m   +p-1]=F_down [2*(n1-1)* m   +p-1][0]*N_B1_danwei[2*(n1-1)* m   +p-1][0] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CN_down[2*(n1-1)* m   +p-1]=F_down [2*(n1-1)* m   +p-1][2]*N_B1_danwei[2*(n1-1)* m   +p-1][2] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            CZ_down[2*(n1-1)* m   +p-1]=F_down [2*(n1-1)* m   +p-1][1]*N_B1_danwei[2*(n1-1)* m   +p-1][1] / (0.5*midu*(V[0][0]**2+V[0][1]**2+V[0][2]**2)*S_can)
            Cl_down[2*(n1-1)* m   +p-1]=CN_down[2*(n1-1)* m   +p-1]*cos(AttackAngle) - CA_down[2*(n1-1)* m   +p-1]*sin(AttackAngle)
            Cd_down[2*(n1-1)* m   +p-1]=CN_down[2*(n1-1)* m   +p-1]*sin(AttackAngle) + CA_down[2*(n1-1)* m   +p-1]*cos(AttackAngle)
        ####################二锥结束####################
    
    ###############################################################End-下表面###############################################################
    
    ###############################################################求力矩系数###############################################################
    
    #?????????
    CA=sum(ravel(CA_up)) + sum(ravel(CA_down))
    #?????????
    CN=sum(ravel(CN_up)) + sum(ravel(CN_down))
    #?????????
    CZ=sum(ravel(CZ_up)) + sum(ravel(CZ_down))
    #???????
    Cl=sum(ravel(Cl_up)) + sum(ravel(Cl_down))
    #???????
    Cd=sum(ravel(Cd_up)) + sum(ravel(Cd_down))
    #?????
    K=Cl / Cd
    #???????????
    Gusuan[1]=CA
    Gusuan[2]=CN
    Gusuan[3]=CZ
    Gusuan[4]=Cl
    Gusuan[5]=Cd
    Gusuan[6]=K
    ###############################################################End-???????###############################################################
    return zhuangjijiao_up
    
    ############################################################???????????????############################################################
# 修正牛顿法-ACM-1-文献19
def Newton1(zhuangjijiao,Vx,Vy,Vz,Ma,*args,**kwargs):
    if zhuangjijiao >= 0:
        r=1.4
        K=(2/(r*Ma*Ma)*(
                         ((r+1)**2*Ma*Ma /(4*r*Ma*Ma-2*(r-1)))**(r/(r-1))
                        *((1-r+2*r*Ma*Ma)/(r+1))-1
                        )
                    )
        Cp=K*sin(zhuangjijiao)**2
    if zhuangjijiao < 0:
        Cp=0
    return Cp

# 修正牛顿法-ACM-2-文献19
def Newton2(zhuangjijiao,Vx,Vy,Vz,Ma,*args,**kwargs):
    if zhuangjijiao >= 0:
        r=1.4
        K=(2*(r+1)*(r+7))/(r+3)**2
        Cp=K*sin(zhuangjijiao)**2
    if zhuangjijiao < 0:
        Cp=0
    return Cp
    #??��/?????1-????4
    

def Qie1(zhuangjijiao=None,Vx=None,Vy=None,Vz=None,Ma=None,*args,**kwargs):
    varargin = Qie1.varargin
    nargin = Qie1.nargin
    yita=multiply(sin(zhuangjijiao),log(sqrt(Ma ** 2 - 1)))
    e=0.18145 - multiply(0.20923,yita) + multiply(0.09092,(yita ** 2)) + multiply(0.006876,(yita ** 3)) - multiply(0.006225,(yita ** 4)) - multiply(0.000971,(yita ** 5))
    Cp=multiply(dot(2.0,exp(e)),(sin(zhuangjijiao)) ** 2)
    return Cp
    #??��/?????1-????5
    

def Qie2(zhuangjijiao=None,Vx=None,Vy=None,Vz=None,Ma=None,*args,**kwargs):
    varargin = Qie2.varargin
    nargin = Qie2.nargin
    Cp=(multiply(dot(4.0,(sin(zhuangjijiao) ** 2)),(2.5 + multiply(dot(8,sin(zhuangjijiao)),(sqrt(Ma ** 2 - 1)))))) / (1 + multiply(dot(16.0,sin(zhuangjijiao)),(sqrt(Ma ** 2 - 1))))
    return Cp

    ############################################################End---???????????????############################################################
'''
GCGS(   n0=n0,
        n1=n1,
        B1= B1,
        B2=B2,
        V=V,
        p_lailiu=p_lailiu,
        S_can=S_can,
        L_can=L_can,
        AttackAngle=AttackAngle,
        Ma= Ma,
        midu=midu,
        )
'''