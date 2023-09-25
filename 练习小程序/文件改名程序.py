import os
os.mkdir('改名程序练习')
os.chdir('D:\\乱78糟的文件\\python\\New\\改名程序练习')

for i in range(1,6):
    a=open('%s.txt'%i,'w')
    a.close()
l=os.listdir('./')
for i in l:
    os.rename('%s'%i,'[NewName] %s'%i)
l=os.listdir('./')
for i in l:
    print(i)

a=input('删除联系内容？')

for i in l:
    os.remove(i)
os.chdir('../')
os.rmdir('改名程序练习')