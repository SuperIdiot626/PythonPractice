print('***文件複製程序***')  
OldFile=input('请输入目标文件名称，带后缀： ')
f=open(OldFile,'r')
z=OldFile.split('.')        #将源文件名字按照‘.’进行分割
z[-2]=z[-2]+'-copy'         #文件扩展名前加入‘-copy’    
NewFile=''
for i in z:                 #
   NewFile=NewFile+i+'.'
NewFile=NewFile[0:-1]

g=open(NewFile,'w')         #一次性读取源文件的每一行，
for i in f.readlines():     #一次性读取源文件的每一行，並将源文件每一行数据依次写入新文件
    g.write(i)
f.close
g.close