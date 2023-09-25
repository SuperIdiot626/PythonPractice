print('***文件截取程序***')
OldFile=input('请输入目标文件名称，带后缀： ')
time_limit_left=input('请输入截取时间左边界： ')
time_limit_right=input('请输入截取时间右边界： ')





file=open(OldFile,'r')
wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt
wholeTxt=wholeTxt[6:]                           #取第6行之后的文本
broken=1                                        #用来判断是否中途推出循环
dataNumber=''                                   #数据中的单独数字
lines=[]                                        #一次性读取源文件的每一行，
average=[0]                                     #用于储存平均数
g=open('cut'+OldFile,'w')                       #新建文件
number_of_lines=len(wholeTxt)                   #记录数据行数


def data_needed(data):                          #读取有用数据，表明了每一行的第几个需要记录
    return data                                 #全部选取
    #return [data[0],data[7]]                   #选择第1列和第8列


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
                lines.append(float(dataNumber))         #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
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

g.write('total:\n')                                     #求总值
for i in average:
    g.write(str(i)+'  ') 
g.write('\n')
for i in average:
    index=average.index(i)
    average[index]/=number_of_lines
g.write('average:\n')                                   #求平均值
for i in average:
    g.write(str(i)+'  ') 
g.write('\n') 
  

file.close
g.close