print('******石头剪刀布*****')
import random

l={1:'石头',2:'剪刀',3:'布  '}

def f(x,y):
    if x==y:
        return '赢了！'
    elif  (x==1 and y==2)or(x==2 and y==3)or(x==3 and y==1):
        return '输了！'
    else:
        return '平局！'
        
while 1:
    x=int(input('1石头 2剪刀 3布 请输入您的选择：'))%3+1
    y=random.randint(1,3)
    print('电脑出的是%s %s '%(l[y],f(x,y)))