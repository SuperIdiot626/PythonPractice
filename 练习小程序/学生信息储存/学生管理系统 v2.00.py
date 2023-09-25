import time
import os
import ast

os.chdir('D:\\Code\\Python\\练习小程序\\学生信息储存')

def main_menu():
    print('='*20)
    print('学生管理系统 V 2.00')
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 显示所有学生信息')
    print('0. 退出系统')
    print('='*20)
    a=int(input('请选择您需要的功能：'))
    if a==1:
        func1()
    elif a==2:
        func2()
    elif a==3:
        func3()
    elif a==4:
        func4()
    elif a==0:
        func0()
    else:
        print('输入有误，请重新输入\n\n')
        time.sleep(1)
        main_menu()

def func1():
    print('*'*20)
    print('1. 添加学生信息')
    stu={'name':'','sex':'','phone':'','numb':''}
    stu['name']=(input('请输入姓名:')).ljust(10,' ')
    sex=input('请输入性别(男1/女2):')
    stu['phone']=(input('请输入电话:')).ljust(10,' ')
    f=open('学生信息储存.txt')
    stu['numb']=len(f.readlines())+1
    f.close()
    if sex=='1':
        stu['sex']='男'
    else:
        stu['sex']='女'

    print('新学生信息：')
    print_single(stu)
    a=input('上述信息是否正确？是1 否2： ')

    if a=='1':
        f=open('学生信息储存.txt','a')
        f.write('\n%s'%stu)
        f.close()
        print('已输入学生信息，返回主菜单')
        main_menu()
    else:
        print('***请重新输入***')
        func1()

def func2():
    print('*'*20)
    print('2. 删除学生信息')
    while 1:
        a=int(input('请输入所要删除学生的序号： '))
        f=open('学生信息储存.txt','r') 
        n=f.readlines()
        f.close()
        if  a>0 and a<len(n)+1:
            i=n[a-1]
            i=ast.literal_eval(i)
            print('序号   姓名        性别  电话')
            print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))
            print('*'*20)
            b=input('删除该学生信息，是否确认？  是1/否2： ')


            if b=='1':
                n.pop(a-1)
                g=open('学生信息储存.txt','w')
                for i in n:
                    g.write(i)
                print('学生信息删除成功！即将返回主菜单') 
                g.close()

            else:
                print('指令取消，返回主菜单')
            main_menu()
        else:
            print('超出范围，请重新输入！')
            continue

def func3():
    print('*'*20)
    print('3. 修改学生信息')
    
    def set_new(i):
        b=input('请输入修改项目： 1姓名 2性别 3电话：')
        if b=='1':
            i['name']=(input('请输入新姓名：')).ljust(10,' ')
            print('学生姓名修改成功！') 
        elif b=='2':
            b=input('请输入新性别(男1/女2)：') 
            if b=='1': 
                i['sex']='男'
            else:
                i['sex']='女'
            print('学生性别修改成功！') 
        elif b=='3':
            i['phone']=(input('请输入新电话：')).ljust(10,' ')
            print('学生电话修改成功！') 
        else:
            print('超出范围，请重新输入！')
            set_new(i)
        b=input('是否继续修改？ 是1/否2： ')
        if b=='1':
            set_new(i)
        else:
            print('修改完毕，修改后学生信息如下：')
            print_single(i)
            
    while 1:
        a=int(input('请输入所要修改学生的序号： '))
        f=open('学生信息储存.txt','r')
        n=f.readlines()
        f.close()
        if  a>0 and a<len(n)+1:
            i=ast.literal_eval((n[a-1]).rstrip('\n'))
            print('*'*20)
            set_new(i)
            n[a-1]=str(i)
            g=open('学生信息储存.txt','w')
            for i in n:
                g.write('%s\n'%i)
            g.close()
            print('即将返回主菜单')
            time.sleep(2)
            main_menu()
        else:
            print('超出范围，请重新输入！')
            continue

def func4():
    refresh()
    print('4. 显示所有学生信息')
    print('*'*20)
    print('序号   姓名        性别  电话')
    f=open('学生信息储存.txt','r')
    while 1:
        i=f.readline()
        if i=='':
            break
        i=ast.literal_eval(i.rstrip('\n'))
        print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))
    f.close()
    print('所有学生信息输出完毕，即将返回主菜单')
    time.sleep(1)
    main_menu()

def func0():
    print('*'*20)
    print('感谢使用管理系统，再见！')
    exit()

def refresh():
    a=1
    f=open('学生信息储存.txt','r+')
    g=open('学生信息储存new.txt','w')
    while 1:
        i=f.readline()
        if i=='\n':
            continue
        if i=='':
            break
        i=ast.literal_eval(i.rstrip('\n'))
        i['numb']=a
        i=str(i)
        g.write('%s\n'%i)
        a=a+1
    f.close()
    g.close()
    os.remove('学生信息储存.txt')
    os.rename('学生信息储存new.txt','学生信息储存.txt')

def print_single(i):
    print('序号   姓名        性别  电话')
    print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))

refresh()
main_menu()