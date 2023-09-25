from datetime import date
import sympy as sym
import numpy as np


# 给定函数式
def r_Up():
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')
    #计算过程量
    a = sym.tan(theta_up)
    b = 1/(0.5*(Wmax/(Lmax**n)))

    # x、y、z函数定义
    r_x = x
    r_y = y
    r_z = a*x*(1+b*y/(x**n))**N1*(1-(b*y/(x**n)))**N1
    r = [r_x, r_y, r_z]
    return r

# 给定函数真值
def Up_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    r = r_Up()
    Value = []
    for i in r:
        i = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        Value.append(i)
    return Value

# 求导的函数
def Differentiate():
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    r = r_Up()
    dr_x1 = []
    dr_x2 = []
    for i in r:
        d_x1 = sym.diff(i, x)
        d_x2 = sym.diff(i, y)
        dr_x1.append(d_x1)
        dr_x2.append(d_x2)
    dr = [dr_x1, dr_x2]
    return dr


# 求导数的值
def Diff_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    dr = Differentiate()
    dr_x1 = []
    dr_x2 = []
    for i in dr[0]:
        d_x1 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        dr_x1.append(d_x1)
    for i in dr[1]:
        d_x2 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        dr_x2.append(d_x2)
    dr_value = [dr_x1, dr_x2]
    return dr_value


# 求二阶导数的函数
def Second_Differentiate():
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    dr = Differentiate()
    ddr_x1_x1 = []
    ddr_x1_x2 = []
    ddr_x2_x1 = []
    ddr_x2_x2 = []
    for i in dr[0]:
        d_x1_x1 = sym.diff(i, x)
        d_x1_x2 = sym.diff(i, y)
        ddr_x1_x1.append(d_x1_x1)
        ddr_x1_x2.append(d_x1_x2)
    for i in dr[1]:
        d_x2_x1 = sym.diff(i, x)
        d_x2_x2 = sym.diff(i, y)
        ddr_x2_x1.append(d_x2_x1)
        ddr_x2_x2.append(d_x2_x2)
    ddr = [ddr_x1_x1, ddr_x1_x2, ddr_x2_x1, ddr_x2_x2]
    return ddr


# 求二阶导数的值
def Second_Differentiate_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    ddr = Second_Differentiate()
    ddr_x1_x1 = []
    ddr_x1_x2 = []
    ddr_x2_x1 = []
    ddr_x2_x2 = []

    for i in ddr[0]:
        dd_x1_x1 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        ddr_x1_x1.append(dd_x1_x1)
    for i in ddr[1]:
        dd_x1_x2 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        ddr_x1_x2.append(dd_x1_x2)
    for i in ddr[2]:
        dd_x2_x1 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        ddr_x2_x1.append(dd_x2_x1)
    for i in ddr[3]:
        dd_x2_x2 = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        ddr_x2_x2.append(dd_x2_x2)
    ddr_value = [ddr_x1_x1, ddr_x1_x2, ddr_x2_x1, ddr_x2_x2]
    return ddr_value

# 求第一基本量的函数
def f_I():
    dr = Differentiate()
    dr = np.array(dr)
    E = dr[0].dot(dr[0])
    G = dr[1].dot(dr[1])
    F = dr[0].dot(dr[1])
    I = [E, G, F]
    return I

# 求第二基本量的函数
def f_II():
    dr = Differentiate()
    ddr = Second_Differentiate()
    I = f_I()

    sqrt_EG_F2 = (I[0] * I[1] - I[2] * I[2]) ** 0.5

    mix_l = np.dot(np.cross(ddr[0], dr[0]), dr[1])
    mix_n = np.dot(np.cross(ddr[3], dr[0]), dr[1])
    mix_m = np.dot(np.cross(ddr[1], dr[0]), dr[1])
    L = mix_l / sqrt_EG_F2
    N = mix_n / sqrt_EG_F2
    M = mix_m / sqrt_EG_F2

    II = [L, N, M]
    return II

# 求第一基本量的值
def I_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    I = f_I()
    Value = []
    for i in I:
        i = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        Value.append(i)
    return Value

# 求第二基本量的值
def II_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    II = f_II()
    Value = []
    for i in II:
        i = i.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
        Value.append(i)
    return Value

# 高斯曲率表达式
def f_Gauss():
    I = f_I()
    II = f_II()
    molecule = II[0] * II[1] - II[2] ** 2
    denominator = I[0] * I[1] - I[2] ** 2
    K_Gauss = (molecule) / (denominator)
    return K_Gauss

# 高斯曲率的值
def Gauss_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n123 = sym.Symbol('n123')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    K_Gauss = f_Gauss()
    print(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    
    # x1=float(x1)
    # x2=float(x2)
    # W_max=float( W_max)
    # L_max=float(L_max)
    # print(type(x1))
    # print(type(x2))
    # print(type(theta_1))
    # print(type(Nc1))
    # print(type(n_value))
    # print(type(W_max))
    # print(type(L_max))

    # Value = K_Gauss.evalf(subs={x:  0, y: 0, theta_up: 0.05235987755982988, N1: 1.5, n: 0.5, Wmax: 2400, Lmax: 5000})
    # print(type(Value))
    # if Value==sym.core.numbers.NaN:
    #     print('asdaasdas')
    #     Value=0
    a=float(x1)
    b=float(x2)
    c=float(theta_1)
    d=float(Nc1)
    e=float(n_value)
    f=int(W_max)
    g=int(L_max)

    x1=a
    x2=b
    theta_1=c
    Nc1=d
    n_value=e
    W_max=f
    L_max=g
    # x1=0
    # x2=0
    # theta_1=0.05
    # Nc1=1.5
    # n_value=0.5
    # W_max=2400
    # L_max=5000
    Value = K_Gauss.evalf(subs={x: a, y: b, theta_up: c, N1:d, n123:e, Wmax:f, Lmax:g})
    
    Value = K_Gauss.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n123: n_value, Wmax: W_max, Lmax: L_max})
    if Value==sym.core.numbers.NaN:
        print('asdaasdas')
        Value=0
    return Value

# 平均曲率表达式
def f_Mean():
    I = f_I()
    II = f_II()
    molecule = I[0] * II[1] - 2 * I[2] * II[2] + I[1] * II[0]
    denominator = 2 * (I[0] * I[1] - I[2] ** 2)
    Mean_Gauss = (molecule) / (denominator)
    return Mean_Gauss

# 平均曲率的值
def Mean_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    # 自变量声明
    x = sym.Symbol('x')
    y = sym.Symbol('y')

    theta_up = sym.Symbol('theta_up')
    N1 = sym.Symbol('N1')
    n = sym.Symbol('n')

    Wmax = sym.Symbol('Wmax')
    Lmax = sym.Symbol('Lmax')

    K_Mean = f_Mean()
    Value = K_Mean.evalf(subs={x: x1, y: x2, theta_up: theta_1, N1: Nc1, n: n_value, Wmax: W_max, Lmax: L_max})
    return Value

#主曲率的值
def Principal_curvature_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    K = Gauss_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    H = Mean_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    c1 = np.float32(H) + np.sqrt(np.float32(H) ** 2 - np.float32(K))
    c2 = np.float32(H) - np.sqrt(np.float32(H) ** 2 - np.float32(K))
    c = [c1, c2]
    sorted_c = sorted(c, key=abs, reverse=True)
    return sorted_c

def Dipan():
    '''基于迪潘指标线判断该点为何类型的点。index=1对应椭圆点，此时曲面上的点都向切平面同一侧弯曲；index=2对应双曲点，曲面上的点一部分向切平面一侧弯曲，另一部分向另一侧弯曲；
    index=3对应抛物点，曲面上的点一部分在某个方向不弯曲，其余的点向同一侧弯曲；index=4对应平点，此时为平面。'''
    II = f_II()
    I2 = II[0] * II[1] - II[2] ** 2
    return I2

def Dipan_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    II = II_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    if II[0] == II[1] == II[2]:
        index = 4
    else:
        I2 = II[0] * II[1] - II[2] ** 2
        if I2 > 0:
            index = 1
        elif I2 < 0:
            index = 2
        else:
            index = 3
    return index

# 单位法向量
def n_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max):
    dr = Diff_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    dr = np.array(dr)
    molecule = np.cross(dr[0], dr[1])
    denominator = (molecule[0] ** 2 + molecule[1] ** 2 + molecule[2] ** 2) ** 0.5
    n = molecule / denominator
    return n

# 法向量与来流夹角
def Angle_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max, Attack, Side):
    '''来流与法向量（法向量方向即为曲面正向）夹角为负，该点属于迎风面，否则属于背风面'''
    n = n_Value(x1, x2, theta_1, Nc1, n_value, W_max, L_max)
    Attack_angle = Attack / 180 * np.pi
    SideSlip_Angle = Side / 180 * np.pi

    ax = np.cos(Attack_angle) * np.cos(SideSlip_Angle)
    ay = np.sin(SideSlip_Angle)
    az = np.sin(Attack_angle) * np.cos(SideSlip_Angle)
    Incoming_flow = [ax, ay, az]
    Incoming_flow = np.array(Incoming_flow)

    molecule = np.dot(n, Incoming_flow)
    denominator = ((n[0] ** 2 + n[1] ** 2 + n[2] ** 2) ** 0.5) * ((ax ** 2 + ay ** 2 + az ** 2) ** 0.5)
    Angle_cos = molecule / denominator
    Angle = np.arccos(float(Angle_cos))
    return Angle

# Wi = 2500/(5000**0.5)*(1000**0.5)
# y=list(np.linspace(-0.5 * Wi, 0.5 * Wi, 50))
# dipan = []
# Gauss = []
# Mean = []
# n = []
# c = []
# Angel_V = []
# for i in y:
#     # dipan.append(Dipan_Value(5000, i, 7/180*np.pi, 3, 0.5, 2500, 5000))
#     # Gauss.append(Gauss_Value(5000, i, 7/180*np.pi, 3, 0.5, 2500, 5000))
#     # Mean.append(Mean_Value(5000, i, 7/180*np.pi, 3, 0.5, 2500, 5000))
#     # c.append(Principal_curvature_Value(1000, i, 7/180*np.pi, 3, 0.5, 2500, 5000))
#     # n.append(n_Value(5000, i, 7/180*np.pi, 3, 0.5, 2500, 5000))
#     Angel_V.append(Angle_Value(5000, i, 7/180*np.pi, 3, 0.5, 2500, 5000, 5, 0))
# # print('迪潘指标线，输出点的类型：\n')
# # print(dipan)
# # print('\n输出高斯曲率：\n')
# # print(Gauss)
# # print('\n输出平均曲率：\n')
# # print(Mean)
# # print('\n输出最大曲率：\n')
# # for i in range(20):
# #     print(max(c[i]))
# # print('\n输出法向量：\n')
# # print(n)
# # print('\n输出主曲率: \n')
# # print(c)
# print(np.float32(Angel_V)/np.pi*180)