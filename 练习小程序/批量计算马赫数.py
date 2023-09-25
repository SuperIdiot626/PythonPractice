print('***马赫数批量计算程序***')
#print('***请注意单位统一为kpa***')

k=1.4                                   #空气gamma值1.4


pressure_data=[]                        #用于储存压力的列表
n=0                                     #用于记次
         
def pressure_ratio_calcu(M):            #马赫数计算程序
    upper=((k+1)*M*M/(2+(k-1)*M*M))**(k/(k-1))
    down=(2*k/(k+1)*M*M-(k-1)/(k+1))**(1/(k-1))
    return upper/down

pessue_str=input('请输入压力测量点读数,数据以空格为间隔')  #参照了前一个程序的输出格式，可以直接复制过来使用
atmosphere=input('请输入当前大气压力（参照手持式压力计，单位kPa）：')
pessue_income=input('请输入来流总压（参照控制终端数据读数，单位atm）：')

pessue_str=pessue_str.split(' ')        #将str数据按两个空格划分为独立数字
atmosphere=float(atmosphere)            #将str转换为float
pessue_income=float(pessue_income)      #将str转换为float
pessue_income*=101.3                    #将来流压力转换为kPa单位
pessue_income+=atmosphere               #将来流压力加上大气压
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
Mach=[]
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
    Mach.append(M_max)
    print('%.5f     '%(M_min),end='   ')
    #print('\b%.5f     '%(M_min))
    #print('第%3d路  马赫数为%.5f'%(n,M_min))
a=input('\npress Key A to write the Mach number: ')
if a=='a' or a=='A':
    file=open('MachNumber.txt','w')
    for i in Mach:
        
        words='第'+str(Mach.index(i)+1)+'路，马赫数为'+str(i)+'\n'
        file.write(words)
    file.close
    a=input('All done! Check the desktop. Press any key to exit')
    
#'第%2d路，马赫数为%.5f\n',
