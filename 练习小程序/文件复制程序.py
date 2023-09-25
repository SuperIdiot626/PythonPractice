

print('***文件复制程序***')

import os
dir=input("请输入目标文件路径：")
OldFile=input('请输入目标文件名称，带后缀： ')



os.chdir(dir)



f=open(OldFile,'r')

z=OldFile.split('.')
z.insert(-1,'.copy.')



NewFile=''
for i in z:
   NewFile=NewFile+i



g=open(NewFile,'w')
for i in f.readlines():
    g.write(i)
f.close
g.close