print('***文件写入删除程序***')
#OldFile=input('请输入目标文件名称，带后缀： ')
OldFile='h0_1_PressureIncome_original-copy.txt'
file=open(OldFile,'r')
wholeTxt=file.readlines()                       #将整个文本读取并写入wholeTxt
wholeTxt=wholeTxt[6:]                           #取第6行之后的文本
dataNumber=''                                   #数据中的单独数字
lines=[]                                        #一次性读取源文件的每一行，

g=open('copy'+OldFile,'w')                      #新建文件

def data_needed(data):                          #读取有用数据，表明了每一行的第几个需要记录
    return data                                 #全部选取
    #return [data[0],data[7]]                   #选择第1列和第7列


for n in wholeTxt:
    for i in n:
        if i=='\n':
            lines.append(float(dataNumber))     #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
            dataNumber=''
            break
        if i==' ':
            if dataNumber!='':
                lines.append(float(dataNumber))     #如果dataNumber不为空，则说明这一个数据已经到头了，对起进行记录并清空
                dataNumber=''
        else:
            dataNumber=dataNumber+i
    lines=data_needed(lines)

    for i in lines:
        g.write(str(i)+'  ')     
    g.write('\n')        
    lines=[]




file.close
g.close