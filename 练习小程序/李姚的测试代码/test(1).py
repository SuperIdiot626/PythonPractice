import symbol as sym

# for i in range(3):
#     x = zone_data[i, variables.index('X')]
#     y = zone_data[i, variables.index('Y')]
#     z = zone_data[i, variables.index('Z')]
#     Point_Position.append(jd.Sphere_or_Cone(x, y, z))
#     if Point_Position[i][2] == 'Sphere':
#         Gaussian_Curvature.append(bl.Gauss_Value((Point_Position[i][0], Point_Position[i][1], Rt)))




def Gauss_Value(x1, x2, R_Ball):
    # 自变量声明
    Rt = sym.Symbol('Rt')
    fai = sym.Symbol('fai')
    theta = sym.Symbol('theta')
    K_Gauss = f_Gauss()
    Value = K_Gauss.evalf(subs={fai: x1, theta: x2, Rt: R_Ball})
    return Value


#Gauss_Value((Point_Position[i][0], Point_Position[i][1], Rt))
a =Gauss_Value(0.1, 0.2, 0.03)