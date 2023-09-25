import time

Tot=[{'name': 'alex mecer', 'sex': '男', 'phone': '11012     ', 'numb': 1},
     {'name': 'micheal   ', 'sex': '女', 'phone': '119521    ', 'numb': 2},
     {'name': 'sweetysam ', 'sex': '男', 'phone': '6668889   ', 'numb': 3},
     {'name': 'Joy       ', 'sex': '男', 'phone': '23333312  ', 'numb': 4},
     {'name': 'mike      ', 'sex': '男', 'phone': '9998-8882 ', 'numb': 5}]

def main_menu():
    print('='*20)
    print('学生管理系统 V 1.00')
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

    global Tot
    stu={'name':'','sex':'','phone':'','numb':''}
    stu['name']=(input('请输入姓名:')).ljust(10,' ')
    sex=input('请输入性别(男1/女2):')
    stu['phone']=input('请输入电话:')
    stu['numb']=len(Tot)+1
    if sex=='1':
        stu['sex']='男'
    else:
        stu['sex']='女'

    print('新学生信息：')
    print_single(stu)
    a=input('上述信息是否正确？是1 否2： ')
    if a=='1':
        Tot.append(stu)
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
        if  a>0 and a<len(Tot)+1:
            i=Tot[a-1]
            print('序号   姓名        性别  电话')
            print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))
            print('*'*20)
            b=input('删除该学生信息，是否确认？  是1/否2： ')
            if b=='1':
                Tot.pop(a-1)
                refresh()
                print('学生信息删除成功！即将返回主菜单') 
            else:
                print('指令取消，返回主菜单')
            main_menu()
        else:
            print('超出范围，请重新输入！')
            continue

def func3():
    print('*'*20)
    print('3. 修改学生信息')
    def set_new():
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
            i['phone']=input('请输入新电话：')
            print('学生电话修改成功！') 
        else:
            print('超出范围，请重新输入！')
            set_new()
        b=input('是否继续修改？ 是1/否2： ')
        if b=='1':
            set_new()
        else:
            print('修改完毕，修改后学生信息如下：')
            print_single(i)
            print('即将返回主菜单')
            time.sleep(2)
            main_menu()
    
    while 1:
        a=int(input('请输入所要修改学生的序号： '))
        if  a>0 and a<len(Tot)+1:
            i=Tot[a-1]
            print_single(i)
            print('*'*20)
            set_new()
        else:
            print('超出范围，请重新输入！')
            continue

def func4():
    print('4. 显示所有学生信息')
    print('*'*20)
    print('序号   姓名        性别  电话')

    global Tot

    for i in Tot:
        print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))
    print('所有学生信息输出完毕，即将返回主菜单')
    main_menu()

def func0():
    print('*'*20)
    print('感谢使用管理系统，再见！')
    exit()

def refresh():
    i=1
    global Tot
    for x in Tot:
        x['numb']=i
        i=i+1

def print_single(i):
    print('序号   姓名        性别  电话')
    print('%03d   %10s %4s   %s'%(i['numb'],i['name'],i['sex'],i['phone']))

main_menu()