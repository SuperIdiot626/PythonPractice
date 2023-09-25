print('***马赫数计算程序***')
print('***请注意单位统一***')
k=1.4

def pressure_ratio_calcu(M):
    upper=((k+1)*M*M/(2+(k-1)*M*M))**(k/(k-1))
    down=(2*k/(k+1)*M*M-(k-1)/(k+1))**(1/(k-1))
    return upper/down



while 1:
    M_max=50
    M_min=0
    a=input('请输入波前总压:')
    b=input('请输入波后总压:')
    a=float(a)
    b=float(b)
    real_pres_ratio=b/a
    while M_max-M_min>=0.00001:
        M_mid=0.5*(M_max+M_min)
        mid_pres_ratio=pressure_ratio_calcu(M_mid)
        if mid_pres_ratio<real_pres_ratio:
            M_max=M_mid
        else:
            M_min=M_mid

    
    print('波前总压%.2f，波后总压%.2f,\n则波前马赫数为%.5f'%(float(a),float(b),float(M_min)))
#为什么一定要运行两次才成功？？



    
