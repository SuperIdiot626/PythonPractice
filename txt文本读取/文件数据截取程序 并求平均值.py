print('***文件截取程序***')
#OldFile=input('请输入目标文件名称，带后缀： ')
OldFile='1.txt'
file=open(OldFile,'r')
wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt
wholeTxt=wholeTxt[6:]                           #取第6行之后的文本
dataNumber=''                                   #数据中的单独数字
lines=[]                                        #一次性读取源文件的每一行，
average=[0]                                     #用于储存平均数
g=open('cut'+OldFile,'w')                       #新建文件
number_of_lines=len(wholeTxt)                   #记录数据行数


def data_needed(data):                          #读取有用数据，表明了每一行的第几个需要记录
    return data                                 #全部选取
    #return [data[0],data[7]]                   #选择第1列和第8列


for n in wholeTxt:
    for i in n:
        if i=='\n':
            lines.append(float(dataNumber))     #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
            dataNumber=''
            break
        if i==' ':
            if dataNumber!='':
                lines.append(float(dataNumber))         #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
                dataNumber=''
        else:
            dataNumber=dataNumber+i
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
    average[index]/=(number_of_lines-1)
g.write('average:\n')                                   #求平均值
for i in average:
    g.write(str(i)+'  ') 
g.write('\n') 
  

file.close
g.close