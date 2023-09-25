print('***马赫数批量计算程序***')
print('***请注意单位统一为kpa***')

k=1.4                                   #空气gamma值1.4


pressure_data=[]                        #用于储存压力的列表
n=0                                     #用于记次
         
def pressure_ratio_calcu(M):            #马赫数计算程序
    upper=((k+1)*M*M/(2+(k-1)*M*M))**(k/(k-1))
    down=(2*k/(k+1)*M*M-(k-1)/(k+1))**(1/(k-1))
    return upper/down

pessue_str=input('请输入压力测量点读数,数据以空格为间隔')  #参照了前一个程序的输出格式，可以直接复制过来使用
atmosphere=input('请输入大气压力：')
pessue_income=input('请输入来流总压：')
pessue_str=pessue_str.split(' ')       #将str数据按两个空格划分为独立数字
atmosphere=float(atmosphere)            #将str转换为float
pessue_income=float(pessue_income)      #将str转换为float
while '' in pessue_str:                 #将数据中多余的空格删掉
    pessue_str.remove('')    


#调试用数字
#pessue_str='100  200  300  400  500  600  500  400  300  200  100'
#atmosphere=0
#pessue_income=1000



for i in pessue_str:
    pressure_data.append(float(i)+atmosphere)

print('大气压为%.2fkpa'%atmosphere)
print('来流总压为%.4fkpa'%pessue_income)

for i in pressure_data:
    n+=1
    M_max=50
    M_min=0
    real_pres_ratio=i/pessue_income
    while M_max-M_min>=0.00001:
        M_mid=0.5*(M_max+M_min)
        mid_pres_ratio=pressure_ratio_calcu(M_mid)
        if mid_pres_ratio<real_pres_ratio:
            M_max=M_mid
        else:
            M_min=M_mid
    print('%.5f     '%(M_min),end='   ')
    #print('\b%.5f     '%(M_min))
    #print('第%3d路  马赫数为%.5f'%(n,M_min))
input('\nany key to exit')
