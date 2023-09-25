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
        return data[:20]                        #截取前20列         用于扫描阀
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
input('press any key to exit')
