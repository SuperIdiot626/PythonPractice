import math

def magenititude_simple(vector):                #(00)求模长平方
    return (vector[0]**2+vector[1]**2)

def magenititude(vector):                       #(01)求模长
    return (vector[0]**2+vector[1]**2)**0.5

def normalize(vector,length=1):                 #(02)求单位向量，length可控制实际长度倍率
    s=magenititude(vector)   
    if s==0:
        return [0,0]
    else: 
        return [vector[0]/s*length,vector[1]/s*length]

def times(vector,h):                            #(03)相乘
    return [vector[0]*h,vector[1]*h]

def divide(vector,h):                           #(04)相除
    return [vector[0]/h,vector[1]/h]

def remainder(vector1,vector2):                 #(04.5)取余
    return [vector1[0]%vector2[0],vector1[1]%vector2[1]]

def quotient(vector1,vector2):                  #(04.6)取商
    return [vector1[0]//vector2[0],vector1[1]//vector2[1]]

def plus(vector1,vector2):                      #(05)向量相加
    return [vector1[0]+vector2[0],vector1[1]+vector2[1]]

def minus(vector1,vector2):                     #(06)向量相减
    return [vector1[0]-vector2[0],vector1[1]-vector2[1]]

def dot_product(vector1,vector2):               #(07)向量点乘
    return (vector1[0]*vector2[0]+vector1[1]*vector2[1])

def cross_product(vector1,vector2):             #(08)向量叉乘
    return [0,0,vector1[0]*vector2[1]-vector1[1]*vector2[0]]

def angle_180(vector1,vector2,radian=0):        #(09)求夹角0-180
    mag_a=magenititude(vector1)
    mag_b=magenititude(vector2)
    if mag_a*mag_b==0:
        return 'Error! zero vector detected'
    else:
        degree=dot_product(vector1,vector2)/mag_a/mag_b
        degree=math.acos(degree)
        if radian==0:
            degree=degree/math.pi*180
        return degree

def angle_to_horizontal(vector,radian=0):       #(10)求与向量(1,0)的夹角，0-360  radian=1输出弧度制
    if vector[0]==0 and vector[1]==0:
        return 'Error! zero vector detected'
    else:
        a=angle_180(vector,(1,0))
        b=angle_180(vector,(0,1))
        if (a<=90 and b<=90) or (a>90 and b<=90):
            degree=a
        elif (a>90 and b>90) or (a<=90 and b>90):
            degree=360-a
        if radian==1:
            degree=degree/180*math.pi
        return degree

def angle_360(vector1,vector2,range=1,radian=0):  #(11)求第一个向量顺时针到第二个向量的角度，0-360  range 决定了范围1为360,0为180
    if (vector1[0]==0 and vector1[1]==0) or (vector2[0]==0 and vector2[1]==0):
        return 'Error! zero vector detected'
    else:
        a=angle_to_horizontal(vector1,radian)
        b=angle_to_horizontal(vector2,radian)
        if a<=b:
            degree=b-a
        else: 
            degree=b-a+360
        if range==0 and degree>=180:
            degree=360-degree
        return degree

def move_CCS(vector,direction):                 #(12)平移坐标系
    return [vector[0]-direction[0],vector[1]-direction[1]]

def rotate_CCS(vector,degree,radian=0):         #(13)旋转坐标系 
    if radian==0:
        degree=degree/180*math.pi
    a=+vector[0]*math.cos(degree)+vector[1]*math.sin(degree)
    b=-vector[0]*math.sin(degree)+vector[1]*math.cos(degree)
    return [a,b]

def another_CCS(vector,direction,degree,radian=0):  #(14)平移+旋转坐标系
    vector=move_CCS(vector,direction)
    vector=rotate_CCS(vector,degree,radian)
    return vector

def into_PCS(vector,radian=0):                      #(15)转化为极坐标系
    length=magenititude(vector)
    angle=angle_to_horizontal(vector,radian)
    return [length,angle]

def converse_int(vector):                           #(16)向量x,y交换位置
    return [int(vector[0]),int(vector[1])]

if __name__ == "__main__":
   a=[3,8]
   b=[7,9]
   
   print(quotient(b,a))
   #print(type(b))