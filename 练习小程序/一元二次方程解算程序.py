print('***一元二次方程求解***')
def solve(a,b,c):
    d=b**2-4*a*c
    if a==0 and b==0:
        print('该式子不是方程')
    elif a==0:
        print('此方程为一次方程，解为：%.5f'%(-c/b))
    elif d<0:
        print('方程无实数解')
    elif d==0:
        print('方程有两个相同解:%.5f'%(-b/4/a))
    elif d>0:
        print('方程有两个不同解:%.5f,%.5f'%((-b+d**0.5)/2/a,(-b-d**0.5)/2/a))
        
while 1:
    x=int(input('请输入二次项系数：'))
    y=int(input('请输入一次项系数：'))
    z=int(input('请输入常数项系数：'))
    solve(x,y,z)