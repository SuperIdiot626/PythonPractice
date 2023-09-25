import os
print('***文件截取并求平均数程序***')


TargetDir=input('请输入目标文件所在路径：')

midterm=''
TargetDir=TargetDir.split('\\')        #将源文件名字按照‘\’进行分割
for i in TargetDir:
    midterm=midterm+i+r'\\'
TargetDir=midterm[:-2]
os.chdir(TargetDir)

OldFile=input('请输入目标文件名称，带后缀： ')
file=open(OldFile,'r')
time_limit_left=input('请输入截取时间左边界： ')
time_limit_right=input('请输入截取时间右边界： ')
switch=input('请输入截取数据来源：1为扫描阀，2为来流测压 ')

wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt
wholeTxt=wholeTxt[6:]                           #截取哪几行
broken=1                                        #用来判断是否中途推出循环
dataNumber=''                                   #数据中的单独数字
lines=[]                                        #一次性读取源文件的每一行
average=[0]                                     #用于储存平均数
number_of_lines=len(wholeTxt)                   #记录数据行数
g=open('cut'+OldFile,'w')                       #新建文件
time_limit_left=float(time_limit_left)
time_limit_right=float(time_limit_right)
switch=int(switch)


def data_needed(data):                          #截取哪几列
    if switch==1:
        return data[:24]                        #截取前24列         用于扫描阀
    elif switch==2:
        return [data[0],data[7]]                #选择第1列和第8列   用于来流测压
    #return data                                #全部选取


for n in wholeTxt:
    broken=0
    for i in n:
        if i=='\n':
            lines.append(float(dataNumber))     #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
            dataNumber=''
            break
        if i==' ':
            if dataNumber!='':
                if len(lines)==0:
                    dataNumber=float(dataNumber)
                    if dataNumber<time_limit_left or dataNumber>time_limit_right:         #若超过左右界限                                              
                        dataNumber=''
                        broken=1
                        number_of_lines-=1
                        break
                lines.append(float(dataNumber))             #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
                dataNumber=''
        else:
            dataNumber=dataNumber+i

    if broken==0:
        lines=data_needed(lines)
        if len(average)==1:
            average=average*len(lines)                      #建立目标长度的0链表
        for i in lines:
            index=lines.index(i)
            average[index]=average[index]+lines[index]      #两个链表对应值相加
    
        for i in lines:
            g.write(str(i)+'  ')     
        g.write('\n')        
        lines=[]

g.write('total:\n')                                         #求总值
for i in average:
    g.write(str(i)+'  ') 
g.write('\n')
for i in average:
    index=average.index(i)
    average[index]/=number_of_lines
g.write('average:\n')                                       #求平均值
for i in average:
    g.write(str(i)+'  ') 
g.write('\n') 
  

file.close
g.close

for i in average:
    if average.index(i)==0:
        continue
    print(average.index(i),i)




k=1.4                                   #空气gamma值1.4
pressure_data=[]                        #用于储存压力的列表
n=0                                     #用于记次
         
def pressure_ratio_calcu(M):            #马赫数计算程序
    upper=((k+1)*M*M/(2+(k-1)*M*M))**(k/(k-1))
    down=(2*k/(k+1)*M*M-(k-1)/(k+1))**(1/(k-1))
    return upper/down

#pessue_str=input('请输入压力测量点读数,数据以空格为间隔')  #参照了前一个程序的输出格式，可以直接复制过来使用
atmosphere=input('请输入当前大气压力（参照手持式压力计，单位kPa）：')
pessue_income=input('请输入来流总压（参照控制终端数据读数，单位atm）：')

#pessue_str=pessue_str.split(' ')       #将str数据按两个空格划分为独立数字
atmosphere=float(atmosphere)            #将str转换为float
pessue_income=float(pessue_income)      #将str转换为float
pessue_income*=101.3                    #将来流压力转换为kPa单位
pessue_income+=atmosphere               #将来流压力加上大气压
#while '' in pessue_str:                #将数据中多余的空格删掉
    #pessue_str.remove('')    


#调试用数字
#pessue_str='100  200  300  400  500  600  500  400  300  200  100'
#atmosphere=0
#pessue_income=1000



for i in average[1:]:
    pressure_data.append(i+atmosphere)
    
print(pressure_data)
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
a=input('\nPress N to exit. Otherwise a Mach number file will be created automaticly')
if a!='N' or a!='n':
    file=open('MachNumber.txt','w')
    for i in Mach:
        
        words='第'+str(Mach.index(i)+1)+'路，马赫数为'+str(i)+'\n'
        file.write(words)
    file.close
    a=input('All done! Check the desktop. Press any key to exit')
    
#'第%2d路，马赫数为%.5f\n',























