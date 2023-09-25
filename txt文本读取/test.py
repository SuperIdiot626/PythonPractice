import os
TargetDir=input('请输入目标文件所在路径：')
midterm=''
TargetDir=TargetDir.split('\\')        #将源文件名字按照‘\’进行分割
for i in TargetDir:
    midterm=midterm+i+r'\\'
TargetDir=midterm[:-2]

os.chdir(TargetDir)
print(os.getcwd())